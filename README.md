# Notebook Description Language

> A language for describing notebooks to interpreters

## Overview

This is a basic language for describing notebooks so they may be used more
effectively by _interpreters_ and _editors_.

**Use with interpreters**: One key motivation is the desire to use Python
notebooks as Python modules, but without running cells that are irrelevant
outside of the notebook context. This allows you to use syntax like this to tell
the python `ignore-cell` statement to ignore this cell.

```python
#: ignore-cell ::
```

Note that this is a Python comment that begins with `#:` and ends with `::`.

This syntax can be implemented in any language that supports comments. The `#:` is not part of the language definition, but the end block `::` is.

**Use with editors**: Another important use for nbd is support richer UI
features in editors such as Visual Studio Code and JupyterLab.

## Quickstart

The tests demonstrate the core functionality right now.

```bash
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ pytest
```

## More about the syntax

The syntax is still being defined. Here are some additional features besides
ignoring cells.

### Arbitrary metadata

You can assign arbitrary values with:

```python
#: {meta_key}:{meta_value}[(, {meta_value)}*] ::
```

For example:

```python
#: favorite_cereal: "frosted flakes" ::
```

### Interface definition

Some metadata keys will have reserved namespaces like `interface`, which can
define a task interface that describes the notebook to workflow tools like Make.

```python
#: interface.in_files: file1.txt, file1.txt ::
#: interface.out_files: out.csv ::
```

## Grammar

The grammar, writen in [Lark](https://github.com/lark-parser/lark) is very readable. The [entire grammar](https://github.com/jakekara/nbdl/blob/main/notebook_description_language/nbd.lark) can (so far)
be expressed in less than one printed page of code.
