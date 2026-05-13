"""Tests for clickmd core functions (md, echo)"""

import io

from clickmd import CLICK_AVAILABLE, echo, md


class TestMd:
    def test_md_renders_text(self, capsys) -> None:
        md("# Hello")
        captured = capsys.readouterr()
        assert "Hello" in captured.out

    def test_md_handles_code_blocks(self, capsys) -> None:
        md("""
```python
print("test")
```
""")
        captured = capsys.readouterr()
        assert "print" in captured.out


class TestEcho:
    def test_echo_plain_text(self, capsys) -> None:
        echo("Hello, World!")
        captured = capsys.readouterr()
        assert "Hello, World!" in captured.out

    def test_echo_with_markdown_header(self, capsys) -> None:
        echo("## Header")
        captured = capsys.readouterr()
        assert "Header" in captured.out

    def test_echo_with_code_fence(self, capsys) -> None:
        echo("```python\ncode\n```")
        captured = capsys.readouterr()
        assert "code" in captured.out

    def test_echo_with_bold(self, capsys) -> None:
        echo("This is **bold** text")
        captured = capsys.readouterr()
        assert "bold" in captured.out

    def test_echo_none(self, capsys) -> None:
        echo(None)
        captured = capsys.readouterr()
        assert captured.out == "\n"

    def test_echo_no_newline(self, capsys) -> None:
        echo("test", nl=False)
        captured = capsys.readouterr()
        assert captured.out == "test"

    def test_echo_to_stderr(self, capsys) -> None:
        echo("error message", err=True)
        captured = capsys.readouterr()
        assert "error message" in captured.err

    def test_echo_to_custom_file(self) -> None:
        stream = io.StringIO()
        echo("custom output", file=stream)
        assert "custom output" in stream.getvalue()


class TestClickAvailable:
    def test_click_available_is_boolean(self) -> None:
        assert isinstance(CLICK_AVAILABLE, bool)
