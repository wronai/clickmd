"""Tests for clickmd.renderer module"""

import io

from clickmd.renderer import (
    _COLORS,
    MarkdownRenderer,
    get_renderer,
    render_markdown,
    strip_ansi,
)


class TestStripAnsi:
    def test_strips_color_codes(self) -> None:
        colored = f"{_COLORS['red']}text{_COLORS['reset']}"
        assert strip_ansi(colored) == "text"

    def test_preserves_plain_text(self) -> None:
        plain = "Hello, World!"
        assert strip_ansi(plain) == plain

    def test_handles_empty_string(self) -> None:
        assert strip_ansi("") == ""


class TestMarkdownRenderer:
    def test_creates_renderer_with_defaults(self) -> None:
        renderer = MarkdownRenderer()
        assert renderer is not None

    def test_creates_renderer_with_stream(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream)
        assert renderer._stream is stream

    def test_disables_colors(self) -> None:
        renderer = MarkdownRenderer(use_colors=False)
        assert renderer._use_colors is False

    def test_heading_output(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)
        renderer.heading(1, "Test Title")
        output = stream.getvalue()
        assert "# Test Title" in output

    def test_heading_levels(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)

        renderer.heading(2, "Level 2")
        output = stream.getvalue()
        assert "## Level 2" in output

    def test_codeblock_output(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)
        renderer.codeblock("python", "print('hello')")
        output = stream.getvalue()
        assert "```python" in output
        assert "print('hello')" in output
        assert output.count("```") == 2

    def test_render_markdown_with_fences(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)

        md_text = """# Title

Some text.

```python
print("code")
```

More text.
"""
        renderer.render_markdown_with_fences(md_text)
        output = stream.getvalue()
        assert "# Title" in output
        assert 'print("code")' in output


class TestHighlighting:
    def test_yaml_highlighting(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)
        result = renderer._highlight_yaml("key: value")
        assert "key" in result
        assert "value" in result

    def test_yaml_comment(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)
        result = renderer._highlight_yaml("# comment")
        assert "comment" in result

    def test_json_highlighting(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)
        result = renderer._highlight_json('{"key": "value"}')
        assert "key" in result
        assert "value" in result

    def test_bash_highlighting(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)
        result = renderer._highlight_bash("echo hello")
        assert "echo" in result
        assert "hello" in result

    def test_js_highlighting(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)
        result = renderer._highlight_js("const x = 'hello'")
        assert "const" in result
        assert "hello" in result

    def test_python_highlighting(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)
        result = renderer._highlight_python("def hello(name: str):")
        assert "def" in result
        assert "hello" in result

    def test_python_decorator(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)
        result = renderer._highlight_python("@dataclass")
        assert "dataclass" in result

    def test_python_comment(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)
        result = renderer._highlight_python("# This is a comment")
        assert "comment" in result

    def test_markdown_heading(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)
        result = renderer._highlight_markdown("## Heading")
        assert "Heading" in result

    def test_markdown_bold(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)
        result = renderer._highlight_markdown("**bold text**")
        assert "bold text" in result

    def test_log_success(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)
        result = renderer._highlight_log("✅ Success!")
        assert "Success" in result

    def test_log_error(self) -> None:
        stream = io.StringIO()
        renderer = MarkdownRenderer(stream=stream, use_colors=False)
        result = renderer._highlight_log("🛑 Error occurred")
        assert "Error" in result


class TestGetRenderer:
    def test_returns_renderer(self) -> None:
        renderer = get_renderer()
        assert isinstance(renderer, MarkdownRenderer)

    def test_with_custom_stream(self) -> None:
        stream = io.StringIO()
        renderer = get_renderer(stream=stream)
        assert renderer._stream is stream


class TestRenderMarkdown:
    def test_renders_to_stream(self) -> None:
        stream = io.StringIO()
        render_markdown("# Hello", stream=stream, use_colors=False)
        output = stream.getvalue()
        assert "Hello" in output

    def test_renders_code_blocks(self) -> None:
        stream = io.StringIO()
        md = """
```python
x = 1
```
"""
        render_markdown(md, stream=stream, use_colors=False)
        output = stream.getvalue()
        assert "x = 1" in output
