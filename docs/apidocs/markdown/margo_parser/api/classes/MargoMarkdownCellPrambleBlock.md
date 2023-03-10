Module margo_parser.api.classes.MargoMarkdownCellPrambleBlock
=============================================================

Classes
-------

`MargoMarkdownCellPreambleBlock(source: str)`
:   A helper to process just the Margo preamble (if any) of a Markdown
    cell. Instead of using MargoBlock directly, which requires the source string to
    only be valid Margo, this will extract the preamble from the cell contents.
    
    :param source: The entire source of a Markdown cell

    ### Ancestors (in MRO)

    * margo_parser.api.classes.MargoBlock.MargoBlock