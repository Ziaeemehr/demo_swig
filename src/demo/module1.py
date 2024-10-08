# This file was automatically generated by SWIG (https://www.swig.org).
# Version 4.2.1
#
# Do not make changes to this file unless you know what you are doing - modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _module1
else:
    import _module1

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "this":
            set(self, name, value)
        elif name == "thisown":
            self.this.own(value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _module1.delete_SwigPyIterator

    def value(self):
        return _module1.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _module1.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _module1.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _module1.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _module1.SwigPyIterator_equal(self, x)

    def copy(self):
        return _module1.SwigPyIterator_copy(self)

    def next(self):
        return _module1.SwigPyIterator_next(self)

    def __next__(self):
        return _module1.SwigPyIterator___next__(self)

    def previous(self):
        return _module1.SwigPyIterator_previous(self)

    def advance(self, n):
        return _module1.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _module1.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _module1.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _module1.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _module1.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _module1.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _module1.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _module1:
_module1.SwigPyIterator_swigregister(SwigPyIterator)
class IntVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _module1.IntVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _module1.IntVector___nonzero__(self)

    def __bool__(self):
        return _module1.IntVector___bool__(self)

    def __len__(self):
        return _module1.IntVector___len__(self)

    def __getslice__(self, i, j):
        return _module1.IntVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _module1.IntVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _module1.IntVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _module1.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _module1.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _module1.IntVector___setitem__(self, *args)

    def pop(self):
        return _module1.IntVector_pop(self)

    def append(self, x):
        return _module1.IntVector_append(self, x)

    def empty(self):
        return _module1.IntVector_empty(self)

    def size(self):
        return _module1.IntVector_size(self)

    def swap(self, v):
        return _module1.IntVector_swap(self, v)

    def begin(self):
        return _module1.IntVector_begin(self)

    def end(self):
        return _module1.IntVector_end(self)

    def rbegin(self):
        return _module1.IntVector_rbegin(self)

    def rend(self):
        return _module1.IntVector_rend(self)

    def clear(self):
        return _module1.IntVector_clear(self)

    def get_allocator(self):
        return _module1.IntVector_get_allocator(self)

    def pop_back(self):
        return _module1.IntVector_pop_back(self)

    def erase(self, *args):
        return _module1.IntVector_erase(self, *args)

    def __init__(self, *args):
        _module1.IntVector_swiginit(self, _module1.new_IntVector(*args))

    def push_back(self, x):
        return _module1.IntVector_push_back(self, x)

    def front(self):
        return _module1.IntVector_front(self)

    def back(self):
        return _module1.IntVector_back(self)

    def assign(self, n, x):
        return _module1.IntVector_assign(self, n, x)

    def resize(self, *args):
        return _module1.IntVector_resize(self, *args)

    def insert(self, *args):
        return _module1.IntVector_insert(self, *args)

    def reserve(self, n):
        return _module1.IntVector_reserve(self, n)

    def capacity(self):
        return _module1.IntVector_capacity(self)
    __swig_destroy__ = _module1.delete_IntVector

# Register IntVector in _module1:
_module1.IntVector_swigregister(IntVector)
class DoubleVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _module1.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _module1.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _module1.DoubleVector___bool__(self)

    def __len__(self):
        return _module1.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _module1.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _module1.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _module1.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _module1.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _module1.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _module1.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _module1.DoubleVector_pop(self)

    def append(self, x):
        return _module1.DoubleVector_append(self, x)

    def empty(self):
        return _module1.DoubleVector_empty(self)

    def size(self):
        return _module1.DoubleVector_size(self)

    def swap(self, v):
        return _module1.DoubleVector_swap(self, v)

    def begin(self):
        return _module1.DoubleVector_begin(self)

    def end(self):
        return _module1.DoubleVector_end(self)

    def rbegin(self):
        return _module1.DoubleVector_rbegin(self)

    def rend(self):
        return _module1.DoubleVector_rend(self)

    def clear(self):
        return _module1.DoubleVector_clear(self)

    def get_allocator(self):
        return _module1.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _module1.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _module1.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        _module1.DoubleVector_swiginit(self, _module1.new_DoubleVector(*args))

    def push_back(self, x):
        return _module1.DoubleVector_push_back(self, x)

    def front(self):
        return _module1.DoubleVector_front(self)

    def back(self):
        return _module1.DoubleVector_back(self)

    def assign(self, n, x):
        return _module1.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _module1.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _module1.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _module1.DoubleVector_reserve(self, n)

    def capacity(self):
        return _module1.DoubleVector_capacity(self)
    __swig_destroy__ = _module1.delete_DoubleVector

# Register DoubleVector in _module1:
_module1.DoubleVector_swigregister(DoubleVector)
class DoubleVector2(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _module1.DoubleVector2_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _module1.DoubleVector2___nonzero__(self)

    def __bool__(self):
        return _module1.DoubleVector2___bool__(self)

    def __len__(self):
        return _module1.DoubleVector2___len__(self)

    def __getslice__(self, i, j):
        return _module1.DoubleVector2___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _module1.DoubleVector2___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _module1.DoubleVector2___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _module1.DoubleVector2___delitem__(self, *args)

    def __getitem__(self, *args):
        return _module1.DoubleVector2___getitem__(self, *args)

    def __setitem__(self, *args):
        return _module1.DoubleVector2___setitem__(self, *args)

    def pop(self):
        return _module1.DoubleVector2_pop(self)

    def append(self, x):
        return _module1.DoubleVector2_append(self, x)

    def empty(self):
        return _module1.DoubleVector2_empty(self)

    def size(self):
        return _module1.DoubleVector2_size(self)

    def swap(self, v):
        return _module1.DoubleVector2_swap(self, v)

    def begin(self):
        return _module1.DoubleVector2_begin(self)

    def end(self):
        return _module1.DoubleVector2_end(self)

    def rbegin(self):
        return _module1.DoubleVector2_rbegin(self)

    def rend(self):
        return _module1.DoubleVector2_rend(self)

    def clear(self):
        return _module1.DoubleVector2_clear(self)

    def get_allocator(self):
        return _module1.DoubleVector2_get_allocator(self)

    def pop_back(self):
        return _module1.DoubleVector2_pop_back(self)

    def erase(self, *args):
        return _module1.DoubleVector2_erase(self, *args)

    def __init__(self, *args):
        _module1.DoubleVector2_swiginit(self, _module1.new_DoubleVector2(*args))

    def push_back(self, x):
        return _module1.DoubleVector2_push_back(self, x)

    def front(self):
        return _module1.DoubleVector2_front(self)

    def back(self):
        return _module1.DoubleVector2_back(self)

    def assign(self, n, x):
        return _module1.DoubleVector2_assign(self, n, x)

    def resize(self, *args):
        return _module1.DoubleVector2_resize(self, *args)

    def insert(self, *args):
        return _module1.DoubleVector2_insert(self, *args)

    def reserve(self, n):
        return _module1.DoubleVector2_reserve(self, n)

    def capacity(self):
        return _module1.DoubleVector2_capacity(self)
    __swig_destroy__ = _module1.delete_DoubleVector2

# Register DoubleVector2 in _module1:
_module1.DoubleVector2_swigregister(DoubleVector2)

def compute_average(values):
    return _module1.compute_average(values)

def compute_sum(values):
    return _module1.compute_sum(values)

