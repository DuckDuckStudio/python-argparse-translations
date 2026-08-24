"""
检查中文翻译中的错误。
"""

import re
from pathlib import Path


def test_punctuation():
    """
    检查中文翻译中的标点是否为全角标点。
    """

    with open(
        (
            Path()
            / "translations"
            / "1.1"
            / "locale"
            / "zh_CN"
            / "LC_MESSAGES"
            / "argparse.po"
        ),
        "r",
        encoding="utf-8",
    ) as f:
        content: str = f.read()
    assert re.search('msgstr\\s".*[\':.].*"', content) is None, "中文翻译应使用全角标点"
    assert re.search(r"^.*：\s+.*$", content, re.MULTILINE) is None, "全角标点后面不应该跟空格"
