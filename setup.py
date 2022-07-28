## setup.py
from setuptools import setup

setup(
    name='passwordTx',
    version='0.1',
    packages=['passwordTx'],
    url="https://github.com/theKata/passwordTx",
    python_requires='>=3.6',
    install_requires=[
        "cryptography>=37.0.0",
        "web3>=5.29.0"
    ]
)