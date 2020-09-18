from .parser import parse
import pytest

NC = "NO_CODE"
SC = "SPLIT_CELL"
EB = "END_BLOCK"
IC = "IGNORE_CELL"


def NL(name, values):
    return (name, values)


def test_parses_empty_block():
    assert parse("   ") == []
    assert parse("") == []


def test_can_parse_endblock():
    assert parse("::") == [NC]


def test_can_parse_split_cell():
    assert parse("--- ::") == [SC, EB]
    assert parse(" --- ::") == [SC, EB]

    assert parse("---------- ::") == [SC, EB]


def test_rejects_unterminated_line():
    with pytest.raises(Exception):
        parse("---")


def test_accepts_many_endblocks():
    assert parse(":: :: :: :: ::") == [NC]
    assert parse(":: --- :: :: ::") == [EB, SC, EB]
    assert parse(":: :: --- :: --- :: ::") == [
        EB, SC, EB, SC, EB
    ]


def test_ignore_cell():
    assert parse("ignore-cell::") == [IC, EB]
    assert parse("ignore-cell::ignore-cell ::  ignore-cell::") == [
        IC, EB, IC, EB, IC, EB
    ]


def test_named_list_with_numbers():
    assert parse("meta.value: 100 :: meta.value: 200 ::") == [
        ("meta.value", [100]),
        EB,
        ("meta.value", [200]),
        EB
    ]


def test_named_list_with_strings():
    assert parse("meta_VALUE_1: \"string\" ::") == [
        ("meta_VALUE_1", ["string"]),
        EB
    ]


def test_named_list_with_multiple_values():
    assert parse(
        "meta: \"string\", 100, -1200.123, false, null, true::"
    ) == [
        ("meta",
         ["string",
          100,
          -1200.123,
          False,
          None,
          True]
         ),
        EB
    ]
