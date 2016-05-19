import os
from setuptools import setup, find_packages

current_dir = os.path.dirname(os.path.abspath(__file__))


def read(filename):
    fullpath = os.path.join(current_dir, filename)
    try:
        with open(fullpath) as f:
            return f.read()
    except Exception:
        return ""


setup(
    name='soloftpd',
    version='0.4',
    description="FTP server application.",
    long_description=read('README.rst'),
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={'console_scripts': [
        'soloftpd = soloftpd.command:main',
    ]},
    author='Shinya Okano',
    author_email='tokibito@gmail.com',
    url='https://github.com/tokibito/soloftpd',
    install_requires=['pyftpdlib'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ])
