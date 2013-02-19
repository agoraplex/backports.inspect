====================
`backports.inspect`_
====================

This is a backport of (some) `Python 3 inspect module`_ features to
2.7 (piggybacking on `aliles/funcsigs`_).

**NOTE:** While `aliles/funcsigs`_ targets Python 2.6 *and* 2.7,
  `backports.inspect` *only* targets 2.7.

**NOTE:** This module monkeypatches `formatannotation` in
`aliles/funcsigs`_ to fix a small bug. This will go away once `our
pull request`_ is integrated.

**BUGS:** There are currently no unit tests :-( ...which must mean
there are no bugs! :-) We welcome issues to expose this assertion as
incorrect, and pull requests to rectify that...

`backports.inspect`_ is licensed under the BSD "3-clause" license. See
`LICENSE`_ for details. The original `Python 3 inspect module`_, from
which most (all?) of this library is derived, is in the public domain.

.. _backports.inspect: https://github.com/agoraplex/backports.inspect
.. _Python 3 inspect module: http://docs.python.org/3/library/inspect.html
.. _aliles/funcsigs: https://github.com/aliles/funcsigs
.. _our pull request: https://github.com/aliles/funcsigs/pull/1
.. _LICENSE: https://github.com/agoraplex/backports.inspect/blob/master/LICENSE.rst
