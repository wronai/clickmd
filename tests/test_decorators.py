"""Tests for clickmd.decorators module"""

import pytest

from clickmd.decorators import (
    CLICK_AVAILABLE,
    Choice,
    Path,
    argument,
    command,
    group,
    option,
)


class TestClickAvailability:
    def test_click_available_is_boolean(self) -> None:
        assert isinstance(CLICK_AVAILABLE, bool)


@pytest.mark.skipif(not CLICK_AVAILABLE, reason="Click not installed")
class TestClickDecorators:
    def test_group_decorator(self) -> None:
        @group()
        def cli() -> None:
            pass

        assert hasattr(cli, "command")

    def test_command_decorator(self) -> None:
        @command()
        def my_cmd() -> None:
            pass

        assert callable(my_cmd)

    def test_option_decorator(self) -> None:
        @command()
        @option("--name", "-n", default="World")
        def greet(name) -> None:
            pass

        assert callable(greet)

    def test_argument_decorator(self) -> None:
        @command()
        @argument("name")
        def greet(name) -> None:
            pass

        assert callable(greet)

    def test_choice_type(self) -> None:
        choices = Choice(["a", "b", "c"])
        assert choices is not None

    def test_path_type(self) -> None:
        path = Path(exists=True)
        assert path is not None


@pytest.mark.skipif(CLICK_AVAILABLE, reason="Click is installed")
class TestClickNotAvailable:
    def test_decorators_raise_import_error(self) -> None:
        with pytest.raises(ImportError):

            @group()
            def cli() -> None:
                pass

    def test_choice_raises_import_error(self) -> None:
        with pytest.raises(ImportError):
            Choice(["a", "b"])

    def test_path_raises_import_error(self) -> None:
        with pytest.raises(ImportError):
            Path(exists=True)
