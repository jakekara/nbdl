from .get_preamble_source import get_preamble_source
from .MargoBlock import MargoBlock

def get_preamble_block(cell_source: str) -> MargoBlock:
    return MargoBlock(get_preamble_source(cell_source))