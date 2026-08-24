"""
检查生成的翻译文件（*.mo）。
"""

import filecmp
import shutil
import subprocess
from pathlib import Path

import pytest


@pytest.mark.skipif(not shutil.which("msgfmt"), reason="需要安装 msgfmt 命令行工具")
def test_have_updated_mo_file(tmp_path: Path):
    """
    检查 *.po 是否有对应的 *.mo，
    并检查该 *.mo 是否最
    """

    po_files = sorted((Path() / "translations").rglob("*.po"))
    assert len(po_files) > 0

    for po_file in po_files:
        assert po_file.with_suffix(".mo").exists(), (
            f"请使用 msgfmt 生成 {po_file} 对应的 .mo 文件。"
        )

        assert (
            subprocess.run(
                ["msgfmt", po_file, "-o", (tmp_path / po_file.with_suffix(".mo").name)],
                check=False,
            ).returncode
            == 0
        )

        assert filecmp.cmp(
            po_file.with_suffix(".mo"),
            (tmp_path / po_file.with_suffix(".mo").name),
            shallow=False,
        ), f"{po_file} 对应的 .mo 文件已过时，请重新生成。"
