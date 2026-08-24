"""
检查翻译文件（*.po）。
"""

import re
import shutil
import subprocess
from itertools import islice
from pathlib import Path

import pytest


@pytest.mark.skipif(not shutil.which("msgfmt"), reason="需要安装 msgfmt 命令行工具")
def test_msgfmt_check():
    """
    检查翻译文件（*.po）是否合规。
    """

    po_files = sorted((Path() / "translations").rglob("*.po"))
    assert len(po_files) > 0

    for po_file in po_files:
        assert (
            subprocess.run(
                [
                    "msgfmt",
                    "--check",
                    "--statistics",
                    "--output-file=/dev/null",
                    po_file,
                ],
                check=False,
            ).returncode
            == 0
        )


def test_empty_msgstr():
    """
    检查翻译文件（*.po）中是否存在空的 msgstr / msgid，
    忽略文件开头 2 行的空 msgstr / msgid。
    """

    po_files = sorted((Path() / "translations").rglob("*.po"))
    assert len(po_files) > 0

    for po_file in po_files:
        with open(po_file, "r", encoding="utf-8") as f:
            lines = islice(f, 2, None)
            content = "".join(lines)
        assert 'msgstr ""\n\n' not in content
        assert 'msgid ""\nmsgstr' not in content


def test_fuzzy():
    """
    检查翻译文件（*.po）中是否存在 `#, fuzzy` 标记。
    """
    po_files = sorted((Path() / "translations").rglob("*.po"))
    assert len(po_files) > 0

    for po_file in po_files:
        with open(po_file, "r", encoding="utf-8") as f:
            assert "#, fuzzy" not in f.read()


def test_metadata():
    """
    检查元数据
    """

    po_files = sorted((Path() / "translations").rglob("*.po"))
    assert len(po_files) > 0

    for po_file in po_files:
        with open(po_file, "r", encoding="utf-8") as f:
            content = f.read()
            assert '"Content-Type: text/plain; charset=UTF-8\\n"' in content
            assert re.search(
                r'^"Plural-Forms:\snplurals=\d;\splural=[\(.*\)|\d];\\n"$', content, re.MULTILINE
            )
