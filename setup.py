import setuptools

install_requires = [
        'numpy','astropy','python-casacore',
        ]

setuptools.setup(
    name="pymsoverview",
    version="0.0.2",
    author = 'Peijin',  
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    entry_points = {
        'console_scripts': [
            'pymsoverview = pymsoverview.__main__:main',
        ],
    },  
    classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',     # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license,
    'Programming Language :: Python :: 3.9',
    ],
)
