# Python argparse 库翻译

Python 标准库 `argparse` 的非官方翻译项目。

想要贡献？请阅读 [贡献指北](CONTRIBUTING.md)。

## 使用

> [!TIP]
> 推荐阅读：
> 1. [如何翻译 argparse 的输出](https://docs.python.org/zh-cn/3.14/howto/argparse.html#how-to-translate-the-argparse-output)
> 2. [国际化 (I18N) 你的程序和模块](https://docs.python.org/zh-cn/3.14/library/gettext.html#i18n-howto)

将仓库中的[翻译目录](translations/1.1/locale/)放到你的程序下，然后在你的程序中添加下面这些代码：

```python
import argparse
import gettext
import locale

_lang = locale.getdefaultlocale()[0] or "zh-CN"  # https://github.com/python/cpython/issues/130796 pylint: disable=deprecated-method / W4902
# 这里设置 zh-CN 为默认语言

t = gettext.translation(
    "argparse", "locale", [_lang]
)  # 修改 "locale" 为你存放翻译文件的位置
argparse._ = t.gettext  # pyright: ignore[reportAttributeAccessIssue]
argparse.ngettext = t.ngettext  # pyright: ignore[reportAttributeAccessIssue]
```

## 许可

本项目采用 <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0 Universal</a><img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg" alt="CC 标志" style="max-width: 1em;max-height:1em;margin-left: .2em;"><img src="https://mirrors.creativecommons.org/presskit/icons/zero.svg" alt="CC 0 标志" style="max-width: 1em;max-height:1em;margin-left: .2em;"> 许可协议。
