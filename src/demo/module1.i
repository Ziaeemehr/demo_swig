%module module1

%{
#include "module1.hpp"
%}


%include stl.i
%include "std_string.i"

namespace std {
    %template(IntVector)     vector<int>;
    %template(DoubleVector)  vector<double>;
    %template(DoubleVector2) vector<vector<double> >;
}

%include "module1.hpp"
