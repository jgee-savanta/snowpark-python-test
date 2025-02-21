# Getting Started

1. Install Python and Anaconda (or MiniConda)
1. Add Anaconda scripts to PATH and reopen terminal: Open 'Anaconda Promp' in Windows start menu, run `where conda` and copy&paste results to PATH
1. Reopen terminal
1. Setup python env (Snowflake only compatible with Python 3.9>3.11):
    ```
    conda create -n <env_name> python==3.10
    conda activate <env_name>
    ```
1. Reopen terminal
1. Check Python version is 3.10.0:
    ```
    python --version
    ```
1. Install snowflake python package:
    ```
    pip install -r requirements.txt
    ```
1. Key-Pair auth setup (in C:\Users\<Your User>\.ssh)
    1. Generate your private key (Best to use a password generator like https://1password.com/password-generator for encryption password and make a note of it):
        ```
        openssl genrsa 2048 | openssl pkcs8 -topk8 -v2 des3 -inform PEM -out rsa_key.p8
        ```
    1. Create a public key:
        ```
        openssl rsa -in rsa_key.p8 -pubout -out rsa_key.pub
        ```
    1. Assign public key to your user. Go to snowflake homepage -> Query data then run:
        ```
        ALTER USER "<Your Savanta Email>" SET RSA_PUBLIC_KEY='MIIBIj...'
        ```
1. Create a file in C:/Users/<Your User>/.snowflake called connections.toml and add the following:
    ```
    ["LK43159.uk-south.azure"]
    account = "LK43159.uk-south.azure"
    user = "<Your Savanta Email>"
    authenticator = "SNOWFLAKE_JWT"
    private_key_file = "C:\\Users\\<Your User>\\.ssh\\rsa_key.p8"
    private_key_file_pwd = "<Your generated encryption password>"
    ```
1. Your python script should now be able to connect to Snowflake