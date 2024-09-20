import os
import shutil
import subprocess
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


# Custom command to compile C++ and SWIG wrapper
class CustomBuildExtCommand(build_ext):
    def run(self):
        # Run SWIG to generate the wrapper
        subprocess.check_call(
            [
                "swig",
                "-python",
                "-c++",
                "-outdir",
                "src/demo",
                "-o",
                "src/demo/module_wrap.cxx",
                "src/demo/module.i",
            ]
        )

        # Call the parent class's run() method to continue the build process
        super().run()

# Define the C++ extension
module = Extension(
    "demo._module",  # Name of the Python module
    sources=[
        "src/demo/module.cpp",
        "src/demo/module_wrap.cxx",
    ],  # C++ and SWIG wrapper source files
    include_dirs=[],  # Add any include directories if necessary
    extra_compile_args=["-O2", "-fPIC"],  # Compilation flags
    extra_link_args=[],  # Any extra link flags
)

# Setup function
setup(
    name="demo",
    version="0.1.0",
    description="A Python package with C++ integration via SWIG",
    packages=["demo"],
    package_dir={"": "src"},
    ext_modules=[module],  # Include the C++ extension
    cmdclass={
        "build_ext": CustomBuildExtCommand,  # Override the default build_ext
    },
)
