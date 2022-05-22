import setuptools

install_requires = [
        'numpy','astropy','python-casacore',
        ]

setuptools.setup(
    name="pymsoverview",
    version="0.0.1",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    )
