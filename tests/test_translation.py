"""
检查加载翻译后的 argparse 输出。
"""

import argparse
import gettext
import re
from pathlib import Path

import pytest


def test_argparse_output_is_translated(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """
    检查 argparse 加载翻译后，帮助文本是否已翻译。
    """

    localedir = (
        Path()
        / "translations"
        / "1.1"
        / "locale"
    )

    for lang in localedir.iterdir():
        assert lang.is_dir()

        translation = gettext.translation("argparse", localedir, [lang.name])
        argparse._ = translation.gettext # pyright: ignore[reportAttributeAccessIssue]
        argparse.ngettext = translation.ngettext # pyright: ignore[reportAttributeAccessIssue]

        parser = argparse.ArgumentParser(prog="demo")
        parser.add_argument("--version", action="version", version="demo 1.0")

        try:
            parser.parse_args(["--help"])
        except SystemExit:
            pass

        output = capsys.readouterr().out
        help_output = re.search(r"^\s+-h,\s--help\s+(.*)$", output, re.MULTILINE)
        assert help_output is not None

        with open(lang / "LC_MESSAGES" / "argparse.po", 'r', encoding="utf-8") as po:
            assert f'msgstr "{help_output.group(1)}"' in po.read()
