Module margo_parser.api.classes.MargoAssignment
===============================================

Classes
-------

`MargoAssignment(name: str, value)`
:   A Margo statement
    
    :param statement_type: MargoStatementTypes.DECLARATION or MargoStatementTypes.DIRECTIVE
    :param name: the name of the statement
    :param value: the value of the statement
    @raises MargoLangException if parameters are invalid

    ### Ancestors (in MRO)

    * margo_parser.api.classes.MargoStatement.MargoStatement
    * abc.ABC