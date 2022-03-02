import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "verilog")
src = "https://github.com/RapidSilicon/Uart16550_axi"

version_str = "1.1.0.post190"
version_tuple = (1, 1, 0, 190)
try:
    from packaging.version import Version as V
    pversion = V("1.1.0.post190")
except ImportError:
    pass

data_version_str = "1.1.0.post40"
data_version_tuple = (1, 1, 0, 40)
try:
    from packaging.version import Version as V
    pdata_version = V("1.1.0.post40")
except ImportError:
    pass
data_git_hash = "39789e40bc57f628507909e6ff493708980b25f0"
data_git_describe = "1.1.0-40-39789e4"
data_git_msg = """\
commit 39789e40bc57f628507909e6ff493708980b25f0
Author: asadaleem-rs <asad.aleem@rapidsilicon.com>
Date:   Fri Jan 7 02:39:27 2022 +0100

    Makefile to build python package added

"""

tool_version_str = "0.0.post144"
tool_version_tuple = (0, 0, 144)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post144")
except ImportError:
    pass

def data_file(f):
    """Get absolute path for file inside pythondata_ip_uart16550."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_ip_uart16550".format(f))
    return fn
