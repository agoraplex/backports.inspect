from setuptools import setup

setup(
    name='backports',
    version='0.0.0',
    author='Tripp Lilley',
    author_email='tripplilley@gmail.com',
    packages=['backports.inspect'],
    namespace_packages=['backports'],
    url='',
    license='See LICENSE',
    description='',
    long_description=open('README.rst').read(),
    install_requires=['distribute', 'funcsigs==0.2'],
    tests_require=['nose>=1.2.1'],
)
