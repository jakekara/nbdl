from margo_parser.api import MargoAssignment


def test_name():
    assignment = MargoAssignment("name", "value")
    assert assignment.name == "name"


def test_value():
    assignment = MargoAssignment("name", "value")
    assert assignment.value == "value"
