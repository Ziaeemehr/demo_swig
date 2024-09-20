# test_module.py
from demo.pymodule import greet

try:
    from demo import module, module1
except:
    pass

# try:
#     from demo.another_module import compute_sum
# except:
#     pass

def test_greet():
    assert greet("World") == "Hello, World!"

def test_compute_average():
    assert (module.compute_average([1, 2, 3]) - 2.0) < 1e-6
    
def test_compute_sum():
    assert (module.compute_sum([1, 2, 3]) - 6.0) < 1e-6
    
def test_compute_average1():
    assert (module1.compute_average([1, 2, 3]) - 2.0) < 1e-6
    
def test_compute_sum1():
    assert (module1.compute_sum([1, 2, 3]) - 6.0) < 1e-6
