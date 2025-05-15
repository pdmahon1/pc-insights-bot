#! /bin/bash


# Ensure Python 3 is installed
if [[ $(python3 --version > /dev/null 2>&1; echo $?) -ne 0 ]] 
  then
    echo "You must install Python 3 before running the project setup."
    #exit(1)
fi


# Install the required modules
python3 -m pip install -r requirements.txt # Linux
# py -m pip install -r requirements.txt # Windows


# See the following for creating a Reddit app and adding OAuth:
# https://github.com/reddit-archive/reddit/wiki/OAuth2