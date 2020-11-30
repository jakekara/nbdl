from ..exceptions import MargoLoaderException
class MargoStatementTypes:

    DECLARATION = "DECLARATION"
    DIRECTIVE = "DIRECTIVE"

    VALID_TYPES = [DECLARATION, DIRECTIVE]

    @staticmethod
    def is_valid_type(statement_type: str) -> bool:
        """Determine if a string is a valid margo statement type"""
        return statement_type in MargoStatementTypes.VALID_TYPES


class MargoStatement:

    TYPES = [MargoStatementTypes.DECLARATION, MargoStatementTypes.DECLARATION]

    def __init__(self, statement_type: str, name: str, value=None):
        if not MargoStatementTypes.is_valid_type(statement_type):
            raise MargoLoaderException("Invalid Margo statement type: " + statement_type)
        self.type = statement_type
        if type(name) != str:
            raise MargoLoaderException("Margo statement type must be str")
        self.name = name
        # Value can be anything
        self.value = value
