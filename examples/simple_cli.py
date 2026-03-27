#!/usr/bin/env python3
"""
Simple CLI - Minimalne CLI z markdown help

Pokazuje jak w kilku liniach stworzyć profesjonalne CLI
z kolorowym helpem i markdown w docstrings.

Run: python examples/simple_cli.py --help
     python examples/simple_cli.py greet Alice
     python examples/simple_cli.py info
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import clickmd

if not clickmd.CLICK_AVAILABLE:
    print("Ten przykład wymaga click: pip install clickmd[click]")
    sys.exit(1)


# ============================================================================
# NAJPROSTSZE CLI - jedna komenda
# ============================================================================

@clickmd.command(cls=clickmd.MarkdownCommand)
@clickmd.argument("name")
@clickmd.option("--loud", "-l", is_flag=True, help="Użyj **WIELKICH** liter")
def greet(name, loud) -> None:
    """
    # 👋 Powitanie
    
    Wyświetla powitanie dla podanej osoby.
    
    ## Przykłady
    
    ```bash
    python simple_cli.py greet Alice
    python simple_cli.py greet Bob --loud
    ```
    """
    message = f"Hello, {name}!"
    if loud:
        message = message.upper()
    
    clickmd.success(message)


# ============================================================================
# CLI Z GRUPĄ KOMEND
# ============================================================================

@clickmd.group(cls=clickmd.MarkdownGroup)
def cli() -> None:
    """
    # 🛠️ Simple CLI Tool
    
    Przykładowe narzędzie CLI z **clickmd**.
    
    ## Szybki start
    
    ```bash
    simple_cli.py greet Alice
    simple_cli.py info
    ```
    """
    pass


@cli.command(cls=clickmd.MarkdownCommand)
@clickmd.argument("name")
def hello(name) -> None:
    """Przywitaj użytkownika."""
    clickmd.success(f"Hello, {name}!")


@cli.command(cls=clickmd.MarkdownCommand)
def info() -> None:
    """
    # Informacje o systemie
    
    Wyświetla informacje o środowisku.
    """
    import platform
    
    clickmd.table(
        headers=["Właściwość", "Wartość"],
        rows=[
            ["Python", platform.python_version()],
            ["System", platform.system()],
            ["clickmd", "1.5.0"],
        ]
    )


@cli.command(cls=clickmd.MarkdownCommand)
@clickmd.option("--format", "-f", type=clickmd.Choice(["json", "yaml", "table"]), default="table")
def status(format):
    """
    Pokaż status aplikacji.
    
    Formaty: `json`, `yaml`, `table`
    """
    data = {
        "status": "running",
        "uptime": "2h 30m",
        "memory": "128 MB",
    }
    
    if format == "json":
        import json
        clickmd.md(f"```json\n{json.dumps(data, indent=2)}\n```")
    elif format == "yaml":
        yaml_str = "\n".join(f"{k}: {v}" for k, v in data.items())
        clickmd.md(f"```yaml\n{yaml_str}\n```")
    else:
        clickmd.table(
            headers=["Key", "Value"],
            rows=[[k, v] for k, v in data.items()]
        )


if __name__ == "__main__":
    cli()
