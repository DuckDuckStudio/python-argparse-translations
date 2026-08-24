"""
通过环境中的 argparse 库来生成该版本的 argparse.pot 翻译模板。
"""

import argparse
import shutil
import subprocess
from pathlib import Path

from catfood.functions.print import 消息头 as MSHead


def main():
    """
    入口函数
    """

    if not shutil.which("xgettext"):
        raise FileNotFoundError("未找到 xgettext")

    ver: str = argparse.__version__  # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue, reportUnknownVariableType] pylint: disable=line-too-long / C0301
    if not isinstance(ver, str):
        raise TypeError("argparse.__version__ 不是 str 类型")

    pot_path = (Path() / "translations" / ver / "argparse.pot").resolve()
    if pot_path.exists():
        raise FileExistsError(f"argparse 版本 {ver} 的翻译模板已存在")

    location: str = argparse.__file__

    pot_path.parent.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [
            "xgettext",
            location,
            "--language", "Python",
            "--output", f"translations/{ver}/argparse.pot",
            "--default-domain", "argparse",
            "--from-code", "UTF-8",
            "--package-name", "argparse",
            "--package-version", ver,
            "--msgid-bugs-address",
            "https://github.com/DuckDuckStudio/python-argparse-translations/issues",
        ],
        check=True,
    )

    # TODO: 自动处理需要的修改
    print(f"{MSHead.成功} 已成功获取 argparse.pot，请依照贡献指北文档进行接下来的修改")
    return 0


if __name__ == "__main__":
    main()
