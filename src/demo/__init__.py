# __init__.py
from .pymodule import greet
try:
    from ._module import *
except:
    pass

try:
    from ._another_module import *
except:
    pass
