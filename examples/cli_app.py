#!/usr/bin/env python3
"""
Full CLI application using clickmd with Click.

Requires: pip install clickmd[click]

Run: python examples/cli_app.py --help
     python examples/cli_app.py hello --name Alice
     python examples/cli_app.py status
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

try:
    import clickmd as click
    
    if not click.CLICK_AVAILABLE:
        print("This example requires Click. Install with: pip install click")
        exit(1)
except ImportError:
    print("This example requires clickmd. Install with: pip install clickmd[click]")
    exit(1)


@click.group()
def cli() -> None:
    """Example CLI application with clickmd."""
    pass


@cli.command()
@click.option("--name", "-n", default="World", help="Name to greet")
@click.option("--formal", "-f", is_flag=True, help="Use formal greeting")
def hello(name: str, formal: bool) -> None:
    """Say hello with style."""
    if formal:
        click.md(f"""
## 🎩 Formal Greeting

Good day, **{name}**. It is a pleasure to make your acquaintance.
        """)
    else:
        click.md(f"""
## 👋 Hello, {name}!

Welcome to **clickmd** - making CLIs beautiful since 2024.

### Quick Tips

```yaml
features:
  - Syntax highlighting
  - Markdown rendering
  - Zero dependencies (core)
  - Click integration (optional)
```
        """)


@cli.command()
def status() -> None:
    """Show application status."""
    click.md("""
## 📊 Application Status

```log
✅ Server: Running
✅ Database: Connected
⚠️ Cache: Warming up
📦 Version: 1.0.0
```

### System Info

```json
{
  "python": "3.12",
  "clickmd": "1.0.0",
  "platform": "linux"
}
```
    """)


@cli.command()
@click.argument("language", type=click.Choice(["python", "javascript", "bash"]))
def example(language: str):
    """Show code example for a language."""
    examples = {
        "python": '''
## 🐍 Python Example

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    
    def greet(self) -> str:
        return f"Hello, {self.name}!"

user = User("Alice", "alice@example.com")
print(user.greet())
```
''',
        "javascript": '''
## 🟨 JavaScript Example

```javascript
const greet = async (name) => {
  const response = await fetch(`/api/users/${name}`);
  const user = await response.json();
  return `Hello, ${user.name}!`;
};

greet("Alice").then(console.log);
```
''',
        "bash": '''
## 🐚 Bash Example

```bash
#!/bin/bash

# Greet the user
greet() {
    local name=${1:-"World"}
    echo "Hello, $name!"
}

# Main
greet "$@"
```
'''
    }
    
    click.md(examples[language])


if __name__ == "__main__":
    cli()
