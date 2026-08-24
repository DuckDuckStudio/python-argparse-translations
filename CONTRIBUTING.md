# 贡献指北

感谢你为本项目做出贡献。

## 开始之前

你需要准备：

- Git；
- Python 3；
- GNU gettext 工具。

## 翻译文件结构

```text
translations/                        # 翻译文件目录
    1.1/                             # argparse 版本
        argparse.pot                 # 原文模板
        locale/                      # 翻译文件目录
            zh-CN/LC_MESSAGES/       # 各语言的翻译文件目录
                argparse.po          # 翻译
                argparse.mo
```

## 新语言翻译

新建该语言的翻译目录:

```bash
mkdir "translations/1.1/locale/<语言>/LC_MESSAGES/" --parents
```

从 POT 模板初始化:

```bash
msginit -i "translations/1.1/argparse.pot" -o "translations/1.1/locale/<语言>/LC_MESSAGES/argparse.po" -l "<语言>"
```

## 翻译流程

1. 创建新分支。
2. 打开 `translations/1.1/locale/<语言>/LC_MESSAGES/argparse.po`，翻译其中的 `msgstr` 字段。
3. 提交并推送你的翻译。
4. 创建拉取请求。

## 更新模板

当 argparse 更新时，需要重新提取字符串，生成 POT 模板。
请切换到包含新版本的 argparse 的 Python 环境，然后运行

```bash
python "tools/get_pot.py"
```

然后修改模板中的信息:
1. 移除 POT 模板中的版权信息。
2. 移除 `#, fuzzy` 标记。
3. 移除文件信息前缀，只保留 `/lib/python<版本号>/argparse.py:<行号>`。
4. 移除这些字段:
   - `POT-Creation-Date`
   - `PO-Revision-Date`
   - `Last-Translator`
   - `Language-Team`
5. 修改 
   ```diff
   - "Content-Type: text/plain; charset=CHARSET\n"
   + "Content-Type: text/plain; charset=UTF-8\n"
   ```
6. 修改
   ```diff
   - "Plural-Forms: nplurals=INTEGER; plural=EXPRESSION;\n"
   + "Plural-Forms: nplurals=2; plural=(n != 1);\n"
   ```

## 检查
### 使用 msgfmt 检查

```bash
msgfmt "translations/1.1/locale/<语言>/LC_MESSAGES/argparse.po" -o "translations/1.1/locale/<语言>/LC_MESSAGES/argparse.mo" -c --statistics
```

> [!TIP]
> 忽略如下警告:  
> ```log
> translations/1.1/locale/<语言>/LC_MESSAGES/argparse.po:2: 警告： 头部缺少文件头“PO-Revision-Date”
> translations/1.1/locale/<语言>/LC_MESSAGES/argparse.po:2: 警告： 头部缺少文件头“Last-Translator”
> translations/1.1/locale/<语言>/LC_MESSAGES/argparse.po:2: 警告： 头部缺少文件头“Language-Team”
> ```

### 使用 pytest 检查

> [!NOTE]
> 不要运行覆盖率测试。

运行：

```bash
pytest
```

## 生成 mo

```bash
msgfmt "translations/1.1/locale/<语言>/LC_MESSAGES/argparse.po" -o "translations/1.1/locale/<语言>/LC_MESSAGES/argparse.mo"
```

## 提交信息

对于翻译的提交信息，请使用 `i18n(<语言>): ` 开头。  
提交信息中应说明修改内容。  
如果是对现有翻译的修正，请指出原翻译为什么不合适，并给出相关依据。

对于其他提交，按照惯例使用 `chore:`、`ci:` 等这些开头。

## 翻译约定

对于中文语言，请使用全角标点。  
例如我们应该使用 `：` 而不是 `:`。

你不应该提交 argparse 库的代码。

## 建议

你可以使用 [PyCharm](https://www.jetbrains.com/zh-cn/pycharm/) 来编辑翻译文件，这个 IDE 内置翻译文件高亮。

如果你使用 Windows，可以通过 [WSL](https://learn.microsoft.com/zh-cn/windows/wsl/about) 来使用 GNU gettext 工具。

你可以使用 AI 进行初步翻译，然后再核对修正。

## 反馈问题

如果发现原文错误、翻译不一致或其他问题，请 [提交 Issue](https://github.com/DuckDuckStudio/python-argparse-translations/issues)。
如果你想直接修正，请参照本文内容提交 PR。
