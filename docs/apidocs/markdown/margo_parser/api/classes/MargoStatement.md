Module margo_parser.api.classes.MargoStatement
==============================================

Classes
-------

`MargoStatement(statement_type: str, name: str, value=None)`
:   A Margo statement
    
    :param statement_type: MargoStatementTypes.DECLARATION or MargoStatementTypes.DIRECTIVE
    :param name: the name of the statement
    :param value: the value of the statement
    @raises MargoLangException if parameters are invalid

    ### Ancestors (in MRO)

    * abc.ABC

    ### Descendants

    * margo_parser.api.classes.MargoAssignment.MargoAssignment
    * margo_parser.api.classes.MargoDirective.MargoDirective

    ### Instance variables

    `name: str`
    :   The name of the statement

    `type: str`
    :   'DIRECTIVE' or 'DECLARATION'

    `value: <built-in function any>`
    :   Any value. Should be None for directives

`MargoStatementTypes()`
:   Supported types of Margo statements

    ### Class variables

    `DECLARATION`
    :

    `DIRECTIVE`
    :

    `VALID_TYPES`
    :

    ### Static methods

    `is_valid_type(statement_type: str) ‑> bool`
    :   Determine if a string is a valid margo statement type