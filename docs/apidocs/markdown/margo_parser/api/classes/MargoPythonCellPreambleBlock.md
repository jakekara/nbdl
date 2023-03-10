Module margo_parser.api.classes.MargoPythonCellPreambleBlock
============================================================

Classes
-------

`MargoPythonCellPreambleBlock(source: str)`
:   A helper to process just the Margo preamble (if any) of a Python cell.
    Instead of using MargoBlock directly, which requires the source string to
    only be valid Margo, this will extract the preamble from the cell contents.
    
    :param source: The entire source of a Python cell

    ### Ancestors (in MRO)

    * margo_parser.api.classes.MargoBlock.MargoBlock