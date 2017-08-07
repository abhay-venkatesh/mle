# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_eum')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_eum')
    _eum = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_eum', [dirname(__file__)])
        except ImportError:
            import _eum
            return _eum
        try:
            _mod = imp.load_module('_eum', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _eum = swig_import_helper()
    del swig_import_helper
else:
    import _eum
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _eum.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _eum.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _eum.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _eum.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _eum.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _eum.SwigPyIterator_equal(self, x)

    def copy(self):
        return _eum.SwigPyIterator_copy(self)

    def next(self):
        return _eum.SwigPyIterator_next(self)

    def __next__(self):
        return _eum.SwigPyIterator___next__(self)

    def previous(self):
        return _eum.SwigPyIterator_previous(self)

    def advance(self, n):
        return _eum.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _eum.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _eum.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _eum.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _eum.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _eum.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _eum.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _eum.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _eum.DoubleVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _eum.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _eum.DoubleVector___bool__(self)

    def __len__(self):
        return _eum.DoubleVector___len__(self)

    def __getslice__(self, i, j):
        return _eum.DoubleVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _eum.DoubleVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _eum.DoubleVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _eum.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _eum.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _eum.DoubleVector___setitem__(self, *args)

    def pop(self):
        return _eum.DoubleVector_pop(self)

    def append(self, x):
        return _eum.DoubleVector_append(self, x)

    def empty(self):
        return _eum.DoubleVector_empty(self)

    def size(self):
        return _eum.DoubleVector_size(self)

    def swap(self, v):
        return _eum.DoubleVector_swap(self, v)

    def begin(self):
        return _eum.DoubleVector_begin(self)

    def end(self):
        return _eum.DoubleVector_end(self)

    def rbegin(self):
        return _eum.DoubleVector_rbegin(self)

    def rend(self):
        return _eum.DoubleVector_rend(self)

    def clear(self):
        return _eum.DoubleVector_clear(self)

    def get_allocator(self):
        return _eum.DoubleVector_get_allocator(self)

    def pop_back(self):
        return _eum.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _eum.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        this = _eum.new_DoubleVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _eum.DoubleVector_push_back(self, x)

    def front(self):
        return _eum.DoubleVector_front(self)

    def back(self):
        return _eum.DoubleVector_back(self)

    def assign(self, n, x):
        return _eum.DoubleVector_assign(self, n, x)

    def resize(self, *args):
        return _eum.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _eum.DoubleVector_insert(self, *args)

    def reserve(self, n):
        return _eum.DoubleVector_reserve(self, n)

    def capacity(self):
        return _eum.DoubleVector_capacity(self)
    __swig_destroy__ = _eum.delete_DoubleVector
    __del__ = lambda self: None
DoubleVector_swigregister = _eum.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)


def optimal_basket(probs):
    return _eum.optimal_basket(probs)
optimal_basket = _eum.optimal_basket
# This file is compatible with both classic and new-style classes.


