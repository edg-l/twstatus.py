from setuptools import setup

setup(
    name='twstatus.py',
    version='0.2.4',
    packages=["twstatus"],
    url='https://github.com/Ryozuki/twstatus.py',
    license='MIT',
    author='Edgar',
    author_email='',
    description='Get information about teeworlds/ddnet servers.',
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
