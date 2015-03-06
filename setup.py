from setuptools import setup

setup(
    name='backports.inspect',
    version='0.0.3',

    author='Tripp Lilley',
    author_email='tripplilley@gmail.com',
    url='https://github.com/agoraplex/backports.inspect',

    license='BSD',
    description='Backport (some) Python 3 `inspect` module features to 2.7 (extending aliles/funcsigs)',
    long_description=open('README.rst').read(),

    packages=[
        'backports',
        ],
    namespace_packages=[
        'backports',
        ],

    install_requires=[
        'funcsigs>=0.4',
        ],
    tests_require=[
        ],

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
)
