from __future__ import absolute_import

# backports.inspect : backports of Python 3's inspect module
from copy import copy
from collections import namedtuple

# re-export the public API from ``inspect`` (which is noisy!)
from inspect import *

# re-export :mod:`funcsigs` for :class:`Signature` objects
from funcsigs import *

# borrowed from Python 3.3's inspect.py
FullArgSpec = namedtuple('FullArgSpec',
    'args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations')

# borrowed and tweaked from Python 3.3's inspect.py
def getfullargspec(func):
    """Get the names and default values of a function's arguments.

    A tuple of seven things is returned:
    (args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults annotations).
    'args' is a list of the argument names.
    'varargs' and 'varkw' are the names of the * and ** arguments or None.
    'defaults' is an n-tuple of the default values of the last n arguments.
    'kwonlyargs' is an empty list
    'kwonlydefaults' is None
    'annotations' is a dictionary mapping argument names to annotations.

    The first four items in the tuple correspond to getargspec().

    Python 2.x doesn't have keyword-only arguments, and we don't have
    a backported alternative. We therefore fill ``kwonlyargs`` and
    ``kwonlydefaults`` as though the function were defined without any
    keyword-only arguments. (i.e., an empty list and ``None``,
    respectively).

    We synthesize a new ``__annotations__`` member if one isn't
    already present because callers expect it to exist, and be
    mutable, and have those side effects persist.
    """

    if ismethod(func):
        func = func.__func__
    if not isfunction(func):
        raise TypeError('{!r} is not a Python function'.format(func))
    args, varargs, kwonlyargs, varkw = _getfullargs(func.__code__)
    func.__annotations__ = getattr( func, '__annotations__', {})
    return FullArgSpec(args, varargs, varkw, func.__defaults__,
            kwonlyargs, None, func.__annotations__)

# borrowed and tweaked from Python 3.3's inspect.py
def _getfullargs(co):
    """Get information about the arguments accepted by a code object.

    Four things are returned: (args, varargs, kwonlyargs, varkw), where
    'args' and 'kwonlyargs' are lists of argument names, and 'varargs'
    and 'varkw' are the names of the * and ** arguments or None.

    Python 2.x doesn't have keyword-only arguments, and we don't have
    a backported alternative. We therefore fill ``kwonlyargs`` and
    ``kwonlydefaults`` as though the function were defined without any
    keyword-only arguments. (i.e., an empty list and ``None``,
    respectively)."""

    if not iscode(co):
        raise TypeError('{!r} is not a code object'.format(co))

    nargs = co.co_argcount
    names = co.co_varnames
    #nkwargs = co.co_kwonlyargcount
    args = list(names[:nargs])
    #kwonlyargs = list(names[nargs:nargs+nkwargs])
    kwonlyargs = []
    step = 0

    #nargs += nkwargs
    varargs = None
    if co.co_flags & CO_VARARGS:
        varargs = co.co_varnames[nargs]
        nargs = nargs + 1
    varkw = None
    if co.co_flags & CO_VARKEYWORDS:
        varkw = co.co_varnames[nargs]
    return args, varargs, kwonlyargs, varkw
