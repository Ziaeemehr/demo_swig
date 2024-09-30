# demo

This is a simple Python package example including C++ code wrapped with SWIG.
The C++ code is compiled automatically during the installation using pip.

## Key Features

- **C++ Integration**: The package includes C++ code wrapped with SWIG, facilitating efficient function calls from Python.
- **Easy Installation**: I've prepared both `pyproject.toml` and `setup.py` files, enabling straightforward compilation of the C++ code during installation via pip. This ensures a smooth setup process for users.
- **Cross-Platform Compatibility**: Designed for compatibility across different platforms, this package can be installed and run without compatibility issues.


### Installation 

```bash
pip install -e .
```

### Quick check

```bash
# in directory including pyproject.toml just type in terminal:
pytest
```

The expected output is:


```bash
pytest          
================================================================= test session starts =================================================================
platform linux -- Python 3.11.10, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/ziaee/git/workshops/demo_package_swig
configfile: pyproject.toml
collected 5 items                                                                                                                                     

tests/test_module.py .....                                                                                                                      [100%]

================================================================== 5 passed in 0.02s ==================================================================
```

