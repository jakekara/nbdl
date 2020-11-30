from .MargoBlock import MargoBlock
from ..utils.get_preamble_source import get_preamble_source


class MargoPythonCellPreambleBlock(MargoBlock):
    def __init__(self, source: str):

        """A helper to process just the Margo preamble (if any) of a Python
        cell
        :param source: The entire source of a Python cell
        """

        preamble_source = get_preamble_source(source)
        super().__init__(preamble_source)
