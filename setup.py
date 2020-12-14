from setuptools import setup
from os import path

this_dir = path.abspath(path.dirname(__file__))

with open(path.join(this_dir, 'README.md')) as f:
    long_description = f.read()

setup(
    name='twstatus.py',
    version='0.3.3',
    packages=["twstatus"],
    url='https://github.com/edg-l/twstatus.py',
    license='MIT',
    author='Edgar',
    author_email='git@edgarluque.com',
    description='Get information about teeworlds/ddnet servers.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    keywords=['teeworlds', 'servers', 'info', 'asyncio'],
    python_requires='>=3.6',
    classifiers=[
        # How mature is this project? Common values are
        #   1 - Planning
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ]
)
