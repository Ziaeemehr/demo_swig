import os
import shutil
import subprocess
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext


# Custom command to compile C++ and SWIG wrappers
class CustomBuildExtCommand(build_ext):
    def run(self):
        # Run SWIG to generate the wrapper for the first module
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
        subprocess.check_call(
            [
                "swig",
                "-python",
                "-c++",
                "-outdir",
                "src/demo",
                "-o",
                "src/demo/module1_wrap.cxx",
                "src/demo/module1.i",
            ]
        )

        # Call the parent class's run() method to continue the build process
        super().run()


module = Extension(
    "demo._module",  # Name of the first Python module
    sources=[
        "src/demo/module.cpp",
        "src/demo/module_wrap.cxx",
    ],
    include_dirs=[],  # Add any include directories if necessary
    extra_compile_args=["-O2", "-fPIC"],  # Compilation flags
    extra_link_args=[],  # Any extra link flags
)

module1 = Extension(
    "demo._module1",  # Name of the second Python module
    sources=[
        "src/demo/module1.cpp",
        "src/demo/module1_wrap.cxx",
    ],
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
    ext_modules=[module, module1],  # Include both C++ extensions
    cmdclass={
        "build_ext": CustomBuildExtCommand,  # Override the default build_ext
    },
)
