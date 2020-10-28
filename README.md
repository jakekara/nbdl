# Margo

> A notebook margin syntax to extend the re-use of notebooks across contexts

## What is Margo

Notebook interfaces are an expressive way to write and share code, but code in
notebooks is not easy to reuse. Margo is a flexible syntax for packaging more
information about how your code should be run in different contexts. Instead of
using notebook metadata, margo can be written right in comments.

## The ignore-cell use case

One key motivation is the desire to use Jupyter Notebooks as source code
modules. This is possible to achieve by converting a notebook to a script and
importing it, but that has one key drawback: notebook code is written
differently than module code, because notebooks often include experimental code
that does not make sense to export outside of the notebook context.

Margo's `ignore-cell` statement tells compatible tools to skip this cell when
importing a notebook. The Python package margo-loader adds support for the
`ignore-cell` statement to Python's `import` system.

Users who want to import a notebook and ignore certain cells can install
margo-loader and add the following line to the top of a cell.

```python
# :: ignore-cell ::
```

Then, in a notebook or Python source file, they can do the following

```python
import margo_loader # once per source file
import Notebook # loads Notebook.ipynb, excluding ignored cells
```

For more details, check out the margo-loader project.

## Language extension in comments

Margo can be added to comments in any programming language by adding a special
comment to mark the beginning of margo syntax. margo-loader uses `# ::`, so each
line must begin with `# ::`. However, this library is only designed to parse
blocks of margo code. It's possible to embed margo in comments, notebook
metadata, docstrings, or even non-python source code.

## Quickstart

This repo only includes code for parsing nbdlang at the moment. The following
will install dependencies and run unit tests, which demonstrate how to use the
code in this repo.

```bash
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ pytest
```

## Additional syntax and use cases

The `ignore-cell` syntax illustrates how a very small bit of syntax can greatly
extend the utility of notebooks. This section looks at other ways margo can add
functionality.

### Declaration

`ignore-cell` is considered a builtin that has a precisely defined meaning. A
more open-ended feature of margo is declaring values with a name.

```python
# :: {meta_key} : VALUES  ::
```

For example:

```python
# ::favorite_cereal: "frosted flakes" ::
```

`VALUES` is assumed to be the contents of a JSON array, except you don't need to
enclose it with brackets.

Because it's an array, you can use any valid JSON values, including `true`,
`false`, `null`, numbers, and strings.

### Language-specified declarations

You can pass a string in a specified format as a declaration. JSON, YAML and
"raw" plain text are currently supported.

The previous example can also be achieved by specifying a JSON field:

```python
# ::favorite_cereal [json]: '["frosted flakes"]' ::
```

In YAML:

```python
# :: favorite_cereal [yaml]: "
# :: -frosted flakes
# " ::
```

Note from the above example, multiline strings are permitted without any special
syntax. You could define a notebook's requirements like so:

```python
# :: requirements.txt [raw]: "
margo-loader
opencv-python
requests
# " ::
```

Another use case would be defining an interface for the notebook when it is run
as a task with a tool like GNU Make. Here's an example:

```python
# :: notebook.interface.in_files: "file_1.txt", "file_2.txt" ::
# :: notebook.interface.out_files: "out.csv" ::
```

### Reserved keywords

Margo is a _mostly_ syntax, so it does not specify the meaning of how it should
be interpreted and used by tools. However, by convention some of these keywords
should eventually become reserved. The examples like `notebook.interface` and
`requirements.txt` might be worth reserving. Here we will start a running list
of reserved keywords.

#### Reserved keyword: 'view'

Defined by margo-loader. This signals that a cell is part of the listed virtual
modules, which will be created during import. So for example, if you have the
following two cells in Greeter.ipynb:

```python
# :: view : "grumpy" ::

def say_hello(to="World"):
    return f"Oh, hi ... {to}."
```

```python
# :: view : "pleasant" ::

def say_hello(to="World"):
    return f"Why, hello, {to}! So wonderful to see you again."
```

You can then import these cells as if they were inside modules named `grumpy` and `pleasant`:

```python
>>> from Greeter.grumpy import hello
>>> print(say_hello())
"Oh, hi ... World."
```

```python
>>> from Greeter.pleasant import hello
>>> print(say_hello())
"Why, hello, World! So wonderful to see you again."
```

### Cell dependency and linking approaches

Another challenge in Jupyter and other notebook environments is that cell
dependencies and execution order may be unambiguously defined.

Jupyter has no in-built system for cell dependency, though there are models for
this.The [Gather](https://github.com/microsoft/gather) provides a way to build a
notebook from any cell using only cell dependencies.
[Observable](https://observablehq.com/) notebooks have a more native concept of
dependency, where each cell is recomputed each time a dependency changes.

In the next few sections, we'll examine ways cell-dependency could be
represented.

#### require-cells

```python
# ::meta.cell-id: define-hello-function
def hello(to="World"):
    return f"Hello, {to}!"
```

```python
# ::meta.require-cells: define-hello-function
print(hello("world"))
```

This pair of statements allow assignment of fixed cell ids, and referencing
these cell ids in a `meta.require-cells` list. An editor tool may use this
feature to ensure that whenever the second cell is executed, the required cells
are run first.

#### next-cell linked list approach

Another approach would be "linking" cells together in a linked list structure
such that each cell can have `meta.next-cell` attribute, which tells compatible
software that whenever this cell is run, the `meta.next-cell` should also be
run. Running one cell would trigger a "domino" effect until a cell without a
`next-cell` attribute set.

#### bock.start and block.end

A similar effect can be achieved by creating cell groups signified by syntax
like `block.start:[name]` and `block.end:[name]`.

Just as code in cells can be run as a single unit, this linear linking of cells
allows the author to make larger groups of code instead of creating overly large
cells.

#### Heirarchical graph approach

Another approach would be a heirarchical structure where cells are graph nodes
with at most one parent and one or more children. Unlike a linear approach of
linking cells or grouping sequences of cells, this requires more decision making
about the traversal order of the network, breadth first versus depth first for
example.

This model could support collapsing cells in a way that is supported by
Mathematica.

Collapsing code is a useful way to represent entire chunks of code in a single
cell. Code collapsing is common in modern IDEs, where nested blocks of code,
such as function body can be collapsed to just the function signature. In a
notebook context, collapsing decisions could be made explicitly by the
programmer and therefore could be provide beneficial expressive features.

### Tests, documentation and cell "relationships"

It might also be useful to use cell annotations to indicate that they are unit
tests or documentation for other cells, with code such as `cell.documents: {cell-id}` or `cell.tests:{cell-id}`. These types of metadata attributes can be
generalized as relationships between one cell and another, (or perhaps even
one-to-many, or many-to-many).

Code authoring tools that understand this notation could provide visual
interfaces that allow the programmer to view a code cell, documentation and
tests in a more integrated and fluid manner. A tested cell could show the author
with a small chart how many tests are passing and failing.

## Grammar

The grammar, writen in [Lark](https://github.com/lark-parser/lark) is very
readable. The [entire
grammar](https://github.com/jakekara/nbdl/blob/main/notebook_description_language/nbd.lark)
can (so far) be expressed in less than one printed page of code.

## Where should NBDLang live

It is not my vision that this syntax would be manually written by programmers.
Tools that support nbdlang would ideally create user interfaces that read and
write these annotations "under the hood" and do not expose the nbdlang area to
programmers by default. Certain tools will have use for certain annotations and
not others. In tools that have no understanding of nbdlang, such as JupyterLab
without any plugins, nbdlang will be exposed as comments. In this case, it's my
goal that the language is decipherable and limited enough that it is not
daunting to programmers.

I have considered using the .ipynb format's built-in metadata fields, however
this appears to be strongly out of favor. Certain notebook document library APIs
do not even allow writing arbtirary metadata, even though it would not result in
invalid ipynb documents.

## Beyond notebooks

NBDlang is meant to appear in code comments, so it can appear in any source
code, but it assumes a cell-based structure of notebooks, and many of the
features described above would not make sense without cells. However, code cells
can be achieved without an ipynb document. Visual Studio Code's Python extension
allows cells to be defined in plain .py files, using a specially formatted `# %%` comment to define the splits between cells. This lightweight implementation
would be sufficient for most of these concepts to translate to this context.
