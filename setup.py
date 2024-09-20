import os
import shutil
import subprocess
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext

# Custom command to compile C++ and SWIG wrappers
class CustomBuildExtCommand(build_ext):
    def run(self):
        # Get the list of all SWIG interface files (.i) and corresponding .cpp files
        swig_files = []
        cpp_files = []

        for filename in os.listdir('src/demo'):
            if filename.endswith('.i'):
                swig_files.append(filename)
                # Derive the corresponding .cpp filename
                cpp_filename = filename[:-2] + 'cpp'
                if cpp_filename in os.listdir('src/demo'):
                    cpp_files.append(cpp_filename)

        # Generate the SWIG wrappers for each module
        for swig_file in swig_files:
            module_name = swig_file[:-2]  # Remove the .i extension
            subprocess.check_call(
                [
                    "swig",
                    "-python",
                    "-c++",
                    "-outdir",
                    "src/demo",
                    "-o",
                    f"src/demo/{module_name}_wrap.cxx",
                    f"src/demo/{swig_file}",
                ]
            )

        # Call the parent class's run() method to continue the build process
        super().run()

# Define the C++ extensions dynamically based on found files
ext_modules = []
for filename in os.listdir('src/demo'):
    if filename.endswith('.i'):
        module_name = filename[:-2]  # Remove the .i extension
        cpp_filename = f"{module_name}.cpp"
        if cpp_filename in os.listdir('src/demo'):
            ext_modules.append(
                Extension(
                    f"demo._{module_name}",
                    sources=[
                        f"src/demo/{cpp_filename}",
                        f"src/demo/{module_name}_wrap.cxx",
                    ],
                    include_dirs=[],  # Add any include directories if necessary
                    extra_compile_args=["-O2", "-fPIC"],  # Compilation flags
                    extra_link_args=[],  # Any extra link flags
                )
            )

# Setup function
setup(
    name="demo",
    version="0.1.0",
    description="A Python package with C++ integration via SWIG",
    packages=["demo"],
    package_dir={"": "src"},
    ext_modules=ext_modules,  # Include dynamically found C++ extensions
    cmdclass={
        "build_ext": CustomBuildExtCommand,  # Override the default build_ext
    },
)
