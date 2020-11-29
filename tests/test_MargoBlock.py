from margo_parser.exceptions import MargoParseException
import json
from margo_parser.api.MargoBlock import MargoBlock
from margo_parser.api.MargoStatement import MargoStatement, MargoStatementTypes
import pytest
import yaml 


def test_parses_empty_margo_block():
    block = MargoBlock("")
    assert block.statements == []


def test_parses_ignore_cell():
    block = MargoBlock("ignore-cell ::")
    assert len(block.statements) == 1
    assert type(block.statements[0]) == MargoStatement
    assert block.statements[0].value == None
    assert block.statements[0].name == "ignore-cell"
    assert block.statements[0].type == MargoStatementTypes.DIRECTIVE

def test_parses_arbitrary_directives():
    block = MargoBlock("example-code ::")
    statement = block.statements[0]
    assert statement.type == MargoStatementTypes.DIRECTIVE
    assert statement.name == "example-code"

def test_parses_plain_text():
    inner_string = "hello world!! 1 true 3 false null"
    test_string = f"""
    hello [raw]: '{inner_string}' ::
    """
    block = MargoBlock(test_string)
    statement = block.statements[0]
    assert statement.value == inner_string

def test_parses_json():
    obj = {"inputs": ["1", 2, True, False, None]}
    json_str = json.dumps(obj)
    margo_source = f"json-values [json]: '{json_str}' ::"
    declaration = MargoBlock(margo_source).statements[0]
    assert declaration.name == "json-values"
    assert declaration.value == obj

def test_parses_yaml():
    obj = {"inputs": ["1", 2, True, False, None]}
    yaml_str = yaml.dump(obj)
    # TODO - This fails when using single quotes around yaml
    # because yaml.dump uses single quotes. Is this part of
    # yaml spec? Or do I need to accomodate both types of quotes?
    margo_source = f"yaml-values [yaml]: \"{yaml_str}\" ::"
    declaration = MargoBlock(margo_source).statements[0]
    assert declaration.name == "yaml-values"
    assert declaration.value == obj

def test_invalid_margo_raises():
    with pytest.raises(MargoParseException):
        MargoBlock("# :: Invalid Margo Code ::")