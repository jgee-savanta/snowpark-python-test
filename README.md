# Getting Started

1. Install Python and Anaconda (or MiniConda)

1. Add Anaconda scripts to PATH and reopen terminal: Open 'Anaconda Promp' in Windows start menu, run `where conda` and copy&paste results to PATH

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
1. Run main.py and a browser should pop up, asking you to authenticate which you can login via Microsoft.