"""
检查中文翻译中的错误。
"""

import re
from pathlib import Path

import pytest


@pytest.mark.parametrize("lang", ["zh_CN", "zh_TW"])
def test_punctuation(lang: str):
    """
    检查中文翻译中的标点是否为全角标点。
    """

    with open(
        (
            Path()
            / "translations"
            / "1.1"
            / "locale"
            / lang
            / "LC_MESSAGES"
            / "argparse.po"
        ),
        "r",
        encoding="utf-8",
    ) as f:
        content: str = f.read()
    assert re.search('msgstr\\s".*[:.\'"].*"', content) is None, (
        "中文翻译应使用全角标点"
    )
    cpm = "[，。、；：？！“”‘’（）《》〈〉【】〔〕「」『』—…·～]"  # cpm = Chinese Punctuation Marks
    assert re.search(rf"\s+{cpm}|{cpm}\s+", content) is None, "全角标点周围不应该有空格"
    assert (
        re.search(
            f"^.*[{'“”‘’' if (lang == 'zh_TW') else '「」『』'}].*$",
            content,
            re.MULTILINE,
        )
        is None
    ), "不应该混用简繁引号"
