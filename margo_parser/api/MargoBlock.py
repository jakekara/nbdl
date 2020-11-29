from ..parser import parse
from .MargoStatement import MargoStatement


class MargoBlock:
    def __init__(self, source: str):
        parsed = parse(source)
        self.statements = []
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
