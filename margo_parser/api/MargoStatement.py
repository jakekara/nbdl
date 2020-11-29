class MargoStatementTypes:

    DECLARATION = "DECLARATION"
    DIRECTIVE = "DIRECTIVE"

    VALID_TYPES = [DECLARATION, DIRECTIVE]

    @staticmethod
    def is_valid_type(statement_type: str) -> bool:
        return statement_type in MargoStatementTypes.VALID_TYPES


class MargoStatement:

    TYPES = [MargoStatementTypes.DECLARATION, MargoStatementTypes.DECLARATION]

    def __init__(self, statement_type: str, name: str, value=None):
        if not MargoStatementTypes.is_valid_type(statement_type):
            raise Exception("INVALID MARGO STATEMENT TYPE: " + statement_type)
        self.type = statement_type
        if type(name) != str:
            raise EXCEPTION("MARGO STATEMENT TYPE MUST BE STRING")
        self.name = name
        # Value can be anything
        self.value = value
