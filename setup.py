from setuptools import setup

setup(
    name='backports.inspect',
    version='0.0.0',

    author='Tripp Lilley',
    author_email='tripplilley@gmail.com',
    url='https://github.com/agoraplex/backports.inspect',

    license='BSD',
    description='Backport (some) Python 3 `inspect` module features to 2.7 (extending aliles/funcsigs)',
    long_description=open('README.rst').read(),
    packages=[
        'backports.inspect',
        ],
    namespace_packages=[
        'backports',
        ],

    install_requires=[
        'distribute',
        'funcsigs==0.2',
        ],
    tests_require=[
        'nose>=1.2.1',
        ],
)
