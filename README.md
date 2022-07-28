# passwordTx : sending Transaction Safe With Password

## Objective 

For using `Web3.py`, we should write `private key` to script or .env. it's dangerous to operating Live Service. Instead of using private key direct, `passwordTx` encrypt `private key` using `password`. At the moment when you need to send a transaction, A prompt window appears to confirm the password. 
It is designed for use in interactive environments such as Jupyter notebooks.


### Usages

#### 1. register private key 

````python
from passwordTx import PasswordTx
from web3 import Web3

web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
passwordTx = PasswordTx("developer", web3)
>> NEW PASSWORD : ******
>> PRIVATE KEY : ******
````

#### 2. send Tx with PasswordTx

````python
from passwordTx import PasswordTx
from web3 import Web3
web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

erc20 = web3.eth.contract(
    address="0x10cc453eA2d3d8C89Efb9EDf1Df7c237CC9b25Da",
    abi=[
          {
            "inputs": [
              {"internalType": "address","name": "to","type": "address"},
              {"internalType": "uint256","name": "amount","type": "uint256"}
            ],
            "name": "transfer",
            "outputs": [
              {"internalType": "bool", "name": "", "type": "bool"}
            ],
            "stateMutability": "nonpayable",
            "type": "function"
          }
    ]
)

with PasswordTx("developer", web3) as passwordTx:
    passwordTx.send(
        erc20.functions.transfer(web3.toChecksumAddress("0x70997970c51812dc3a010c7d01b50e0d17dc79c8"), 120 * 10 **18)
    )
````
