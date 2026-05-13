import sys
from typing import Literal, Optional


class MarkdownRenderer:
    def __init__(self, use_colors: bool = True, stream=None):
        self._stream = stream if stream is not None else sys.stdout
        is_tty = True
        try:
            is_tty = self._stream.isatty()
        except Exception:
            is_tty = True
        self._use_colors = bool(use_colors) and is_tty

    def _c(self, color: str, text: str, bold: bool = False, dim: bool = False) -> str:
        if not self._use_colors:
            return text
        prefix = ""
        if bold:
            prefix += _COLORS["bold"]
        if dim:
            prefix += _COLORS["dim"]
        return f"{prefix}{_COLORS[color]}{text}{_COLORS['reset']}"

    def _get_num_cols(self, headers: list[str], rows: list[list[str]]) -> int:
        return len(headers) if headers else (len(rows[0]) if rows else 0)

    def _render_markdown_wrapper(self, content_func, *args, **kwargs):
        self._writeln("```")
        content_func(*args, **kwargs)
        self._writeln("```")

    def _render_table_body(
        self,
        headers: list[str],
        rows: list[list[str]],
        style: str,
        align: list[str],
        markdown_safe: bool,
    ) -> None:
        num_cols = self._get_num_cols(headers, rows)
        widths = self._calculate_column_widths(headers, rows, num_cols)
        align = align or ["left"] * num_cols
        chars = self._get_table_chars(style)

        self._render_table_top_border(chars, widths)
        self._render_table_header(headers, widths, align, chars)
        self._render_table_rows(rows, widths, align, chars, num_cols)
        self._render_table_bottom_border(chars, widths)

    def table(
        self,
        headers: list[str],
        rows: list[list[str]],
        style: Literal["ascii", "unicode", "minimal", "none"] = "unicode",
        align: Optional[list[Literal["left", "center", "right"]]] = None,
        markdown_safe: bool = True,
    ) -> None:
        if not headers and not rows:
            return

        if markdown_safe:
            self._render_markdown_wrapper(
                self._render_table_body, headers, rows, style, align, False
            )
        else:
            self._render_table_body(headers, rows, style, align, False)
