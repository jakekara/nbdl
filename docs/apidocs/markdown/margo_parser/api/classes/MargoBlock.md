Module margo_parser.api.classes.MargoBlock
==========================================

Classes
-------

`MargoBlock(source: str)`
:   A collection of Margo statements.
    
    Parses source immediately, raising an exception if parsing
    fails.
    :param source: The source code string
    :raises: MargoParseException if the source string cannot be parsed
    :raises: MargoLangException if there's some other error

    ### Descendants

    * margo_parser.api.classes.MargoMarkdownCellPrambleBlock.MargoMarkdownCellPreambleBlock
    * margo_parser.api.classes.MargoPythonCellPreambleBlock.MargoPythonCellPreambleBlock

    ### Instance variables

    `statements: List[margo_parser.api.classes.MargoStatement.MargoStatement]`
    :   List of Margo statements