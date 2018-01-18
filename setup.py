from setuptools import setup, find_packages

setup(
    name='KrakenX Auto',
    version='0.0.1',
    description='daemon to control pump and fan of kraken x series(x62, x52, x42) automatically',
    author='whybe',
    author_email='ahsky2@gmail.com',
    packages=find_packages(),
    install_requires=[
        'krakenx==0.0.1',
    ],
    setup_requires=[],
    dependency_links=[],
    scripts=[],
)
