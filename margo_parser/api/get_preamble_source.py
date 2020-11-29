from .MargoBlock import MargoBlock

class MargoCommentPrefixes:
    PYTHON = "# ::"

def get_preamble_source(cell_source: str, prefix=MargoCommentPrefixes.PYTHON) -> str:
    """
    Get the Margo preamble source using the default Python Margo note prefix "# :: "
    """

    ret = []

    lines = cell_source.split("\n")

    for line in lines:
        trim_line = line.lstrip()
        if trim_line.startswith(prefix):
            ret.append(trim_line.lstrip()[len(prefix):])
        elif trim_line.startswith("#"):
            # Ignore comments
            continue
        elif len(trim_line.strip()) < 1:
            # Ignore empty lines
            continue
        else:
            # Stop at the first non-comment, non-empty line
            break 

    return "\n".join(ret)

