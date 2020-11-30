from ...parser import parse
from .MargoStatement import MargoStatement


class MargoBlock:
    def __init__(self, source: str):

        """A class representing a block of multiple Margo statements.
        Constructor parses source immediately, raising an exception if parsing
        fails.
        :param source: The source code string
        :raises: MargoParseException if the source string cannot be parsed
        :raises: MargoLoaderException if there's some other error"""

        # This is what raises the MargoParseException if it fails
        parsed = parse(source)
        self.statements = []
        # TODO - Test statement for valid structure
        for statement in parsed["BODY"]:
            statement_type = statement["TYPE"]
            statement_name = statement["NAME"]
            if "VALUE" in statement:
                statement_value = statement["VALUE"]
                statement = MargoStatement(
                    statement_type, statement_name, value=statement_value
                )
            else:
                statement = MargoStatement(statement_type, statement_name)

            self.statements.append(statement)
