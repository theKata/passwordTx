# passwordTx : sending Transaction Safe With Password

## Objective 

For using `Web3.py`, we should write `private key` to script or .env. it's dangerous to operating Live Service. Instead of using private key direct, `passwordTx` encrypt `private key` using `password`. At the moment when you need to send a transaction, A prompt window appears to confirm the password. 
It is designed for use in interactive environments such as Jupyter notebooks.


