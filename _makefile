
PYTHON_INCLUDE = $(shell python3-config --includes)
PYTHON_LIB = $(shell python3-config --libs)

CXX = g++
CXXFLAGS = -O2 -fPIC
SWIG = swig

# SRC = src/demo/module.cpp src/demo/module_wrap.cxx
# INC = src/demo/module.hpp

# all: src/demo/_module.so

# # Generate the SWIG wrapper file
# src/demo/module_wrap.cxx: src/demo/module.i
# 	$(SWIG) -python -c++ -outdir src/demo -o src/demo/module_wrap.cxx src/demo/module.i

# # Compile the shared object (Python extension)
# src/demo/_module.so: $(SRC) $(INC)
# 	$(CXX) $(CXXFLAGS) $(PYTHON_INCLUDE) -shared -o src/demo/_module.so $(SRC) $(PYTHON_LIB)

clean:
	rm -rf src/demo/*_wrap.cxx src/demo/*.so
	rm -rf src/demo/*.pyc
