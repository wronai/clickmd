# clickmd API Reference

## Core Functions

### `md(text: str) -> None`

Render markdown text with syntax highlighting to stdout.

```python
from clickmd import md

md("""
# Hello World

```python
print("Hello!")
```
""")
```

### `echo(message, file=None, nl=True, err=False, color=None) -> None`

Smart echo function that auto-detects markdown content.

**Parameters:**
- `message` - Text to output (can be None)
- `file` - Output stream (default: stdout)
- `nl` - Add newline at end (default: True)
- `err` - Output to stderr (default: False)
- `color` - Force color on/off (default: auto-detect)

```python
from clickmd import echo

# Auto-detects markdown
echo("## Header")          # Rendered as markdown
echo("Plain text")         # Output as-is
echo("**Bold**")           # Rendered as markdown

# Options
echo("message", nl=False)  # No trailing newline
echo("error", err=True)    # Output to stderr
```

### `render_markdown(text, text_lang="markdown", stream=None, use_colors=True) -> None`

Low-level markdown rendering function with more options.

```python
from clickmd import render_markdown
import sys

render_markdown("# Title", stream=sys.stderr, use_colors=False)
```

### `get_renderer(stream=None, use_colors=True) -> MarkdownRenderer`

Get a `MarkdownRenderer` instance for advanced usage.

```python
from clickmd import get_renderer

renderer = get_renderer(use_colors=True)
renderer.heading(1, "Title")
renderer.codeblock("python", "x = 1")
```

---

## MarkdownRenderer Class

### Constructor

```python
MarkdownRenderer(use_colors: bool = True, stream=None)
```

**Parameters:**
- `use_colors` - Enable ANSI color codes (auto-disabled for non-TTY)
- `stream` - Output stream (default: sys.stdout)

### Methods

#### `heading(level: int, text: str) -> None`

Render a markdown heading.

```python
renderer.heading(1, "Main Title")    # # Main Title
renderer.heading(2, "Section")       # ## Section
```

#### `codeblock(lang: str, content: str) -> None`

Render a fenced code block with syntax highlighting.

```python
renderer.codeblock("python", "def hello(): pass")
renderer.codeblock("json", '{"key": "value"}')
```

#### `render_markdown_with_fences(markdown_text: str, text_lang: str = "markdown") -> None`

Render complete markdown text with code fence detection.

```python
renderer.render_markdown_with_fences("""
# Title

```python
code here
```
""")
```

---

## Click Decorators

Requires `click` package: `pip install clickmd[click]`

### Check Availability

```python
from clickmd import CLICK_AVAILABLE

if CLICK_AVAILABLE:
    print("Click is installed")
```

### Decorators

```python
import clickmd as click

@click.group()
def cli():
    """My CLI"""
    pass

@cli.command()
@click.option("--name", "-n", default="World")
@click.argument("path", type=click.Path(exists=True))
def process(name, path):
    click.md(f"Processing **{path}** for {name}")
```

### Available Decorators

| Decorator | Description |
|-----------|-------------|
| `@group()` | Create command group |
| `@command()` | Create command |
| `@option()` | Add option |
| `@argument()` | Add argument |
| `@pass_context` | Pass Click context |

### Available Types

| Type | Description |
|------|-------------|
| `Choice` | Enumerated choices |
| `Path` | File/directory path |
| `Context` | Click context object |

---

## Syntax Highlighting

### Supported Languages

| Language ID | Aliases | Features |
|-------------|---------|----------|
| `python` | `py` | Keywords, strings, comments, decorators |
| `typescript` | `ts` | Keywords, strings, template literals |
| `javascript` | `js` | Keywords, strings, comments |
| `json` | - | Keys, strings, numbers, booleans, null |
| `yaml` | `yml` | Keys, values, comments, lists |
| `bash` | `sh`, `shell` | Commands, arguments, comments |
| `markdown` | `md` | Headers, bold, links |
| `log` | - | Status emojis, errors, warnings |

### Log Highlighting

The `log` language provides automatic coloring based on content:

| Pattern | Color |
|---------|-------|
| `🛑`, `❌`, `Error`, `Exception` | Red |
| `⚠️`, `warning` | Yellow |
| `✅`, `🚀` | Green |
| `📦`, `💬`, `🔄` | Cyan |
| `📊` | Magenta |
| `→` | Gray |

---

## Tables & Panels (Phase 1)

### `table(headers, rows, style="rounded") -> None`

Render a formatted table.

```python
from clickmd import table

table(
    headers=["Name", "Version"],
    rows=[["clickmd", "1.1.0"], ["click", "8.1.7"]],
)
```

### `panel(content, title=None, style="blue") -> None`

Render a bordered panel.

```python
from clickmd import panel

panel("Deployment complete!", title="Success", style="green")
```

### `blockquote(text) -> None`

Render a blockquote.

### `hr() -> None`

Render a horizontal rule.

### `checklist(items) -> None`

Render a checklist with ✓/✗ markers.

---

## Logger

### `get_logger(name) -> Logger`

Get a markdown-aware logger.

```python
from clickmd import get_logger

log = get_logger("myapp")
log.info("Starting...")
log.success("Done!")
log.warning("Deprecated API")
log.error("Connection failed")
log.action("deploy", "Deploying to production")
```

### Module-level shortcuts

- `log_info(msg)` / `log_success(msg)` / `log_warning(msg)` / `log_error(msg)` / `log_action(action, msg)`

---

## Progress & Spinners (Phase 3)

### `progress(total, label="") -> ProgressBar`

```python
from clickmd import progress

with progress(100, "Downloading") as bar:
    for i in range(100):
        bar.advance(1)
```

### `spinner(label="") -> Spinner`

```python
from clickmd import spinner

with spinner("Loading..."):
    time.sleep(2)
```

### `countdown(seconds, label="") -> None`

Display a countdown timer.

---

## Themes (Phase 4)

### `set_theme(name) -> None`

Switch the active color theme.

### `get_theme() -> Theme`

Get the current theme.

### `list_themes() -> list[str]`

List available theme names.

### `register_theme(name, theme) -> None`

Register a custom theme.

### `is_no_color() -> bool`

Check if `NO_COLOR` environment variable is set.

---

## Developer Tools (Phase 5)

### `debug(value, label=None) -> None`

Pretty-print a value with type information.

### `inspect_obj(obj) -> None`

Show object attributes and methods.

### `diff(old, new) -> None`

Show a side-by-side diff of two strings.

### `tree(path, max_depth=3) -> None`

Display a directory tree.

### `install_excepthook() -> None`

Install pretty exception formatting.

---

## Interactive Prompts

### `menu(title, items, default=1, prompt_text="Select", exit_option="Exit") -> int`

Display a numbered menu and prompt for selection.

```python
import clickmd

choice = clickmd.menu("## Choose", ["Option A", "Option B", "Option C"])
```

Returns 1-based index, 0 for exit, -1 on error.

### `select(prompt_text, items, default=1) -> int`

Inline selection without a title heading.

---

## Utility Functions

### `strip_ansi(text: str) -> str`

Remove ANSI escape codes from text.

```python
from clickmd import strip_ansi

clean = strip_ansi("\x1b[31mred text\x1b[0m")
print(clean)  # "red text"
```
