# nbdlang, a Notebook Description Language

> A language for describing notebooks for interpreters and editing tools

## Comment language extension

nbdlang adds an annotation syntax for notebooks to support a variety of use
cases beyond the computational science use case notebooks are primarily used
for. It is meant to be implemented in comments within code cells, but could be
stored in metadata within a notebook format such as Jupyter's `nbformat`.

It is envisioned that users may directly write nbdlang annotations or editing
tools may automatically read and write these annotations and abstract their
features through the user interface.

## The ignore-cell use case

One key motivation is the desire to use Jupyter Notebooks as source code
modules. This is possible to achieve by converting a notebook to a script and
importing it, but that solution does not address the fact that notebook code is
written differently than module code, because notebooks often include
experimental code that does not make sense to export outside of the notebook
context. nbdlang's `ignore-cell` statement tells compatible interpreters to skip
this cell. Adding nbdlang support to Python's `import` system, or `nbconvert`
makes these tools significantly better equipped to reuse code in notebooks,
requiring the notebook's only author to add this line to code that should not be
exported.

```python
#: ignore-cell ::
```

## Language extension in comments

Note that this example is a Python comment that begins with `#:` and ends with
`::`. This syntax can be implemented in any language's comments. The `#:` is not
part of the language definition, and could just as easily be used with `;`,
`//`, `/**/` or any other comment characters specific to a particular language.

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

## Code and metadata together

In a very general sense, notebooks improve upon plain source text files and
editor interfaces by adding the concept that code can be coupled with metadata
in a single document. Notebooks have typically been used exclusively for
computation rather than for software engineering. nbdlang aims to make existing
notebook authoring tools more generally useful in a software engineering context
— such as with the `ignore-cell` statement — and support additional features. My
focus is features that allow code authors maximum flexibility in organizing and
representing software systems, particularly to reduce cognitive load and improve
comprehension of software they write.

## Additional syntax and use cases

The `ignore-cell` syntax illustrates how a very small bit of syntax can greatly
extend the utility of notebooks. This section looks at other ways nbdlang can
add functionality.

### Arbitrary metadata attributes

You can assign arbitrary values with:

```python
#: {meta_key}:{meta_value}[(, {meta_value)}*] ::
```

For example:

```python
#: favorite_cereal: "frosted flakes" ::
```

The `meta_key` may contain alphanumeric characteris, underscores and dots for
segmentation. They may not begin or end with dots.

The `meta_value` is a comma-separated list that may contain escaped strings,
signed numeric values, true, false, or null values. This is similar to JSON,
without dictionaries or arrays.

### Reserved metadata keywords

Some metadata keys will have reserved namespaces like `interface`, which can
define a task interface that describes the notebook to workflow tools like Make.

```python
#: interface.in_files: file1.txt, file1.txt ::
#: interface.out_files: out.csv ::
```

Since these `interface` fields apply to the entire notebook and not the cell,
perhaps they should be namespaced `notebook.interface`, and in that vein, all
metadata attribues should begin with either `notebook` or `cell`.

Another keyword that might be useful to reserve is `meta` or `metadata`. Editor
tools may want to add additional features and namespace certain attributes by
prefixing them with the name of the editor tool.

### Cell dependency and linking approaches

Another challenge in Jupyter and other notebook environments is that cell
dependencies and execution order may be unambiguously defined.

Jupyter has no in-built system for cell dependency, though there are models for
this.The [Gather](https://github.com/microsoft/gather) provides a way to build a
notebook from any cell using only cell dependencies.
[Observable](https://observablehq.com/) notebooks have a more native concept of
dependency, where each cell is recomputed each time a dependency changes.

In the next few sections, we'll examine ways cell-dependency could be represented.

#### require-cells

```python
#: meta.cell-id: define-hello-function
def hello(to="World"):
    return f"Hello, {to}!"
```

```python
#: meta.require-cells: define-hello-function
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
about the traversal order of the network, breadth first versus depth first for example.

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
generalized as relationships between one cell and another, (or perhaps even one-to-many, or many-to-many).

Code authoring tools that understand this notation could provide visual
interfaces that allow the programmer to view a code cell, documentation and
tests in a more integrated and fluid manner. A tested cell could show the author
with a small chart how many tests are passing and failing.

## Grammar

The grammar, writen in [Lark](https://github.com/lark-parser/lark) is very readable. The [entire grammar](https://github.com/jakekara/nbdl/blob/main/notebook_description_language/nbd.lark) can (so far)
be expressed in less than one printed page of code.

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
do not even allow writing arbtirary metadata, even though it would not result in invalid ipynb documents.

## Beyond notebooks

NBDlang is meant to appear in code comments, so it can appear in any source
code, but it assumes a cell-based structure of notebooks, and many of the
features described above would not make sense without cells. However, code cells
can be achieved without an ipynb document. Visual Studio Code's Python extension
allows cells to be defined in plain .py files, using a specially formatted
`# %%` comment to define the splits between cells. This lightweight implementation
would be sufficient for most of these concepts to translate to this context.
