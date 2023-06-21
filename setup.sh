#! /bin/bash


if [[ $(python3 --version > /dev/null 2>&1; echo $?) -ne 0 ]] 
  then
    echo "You must install Python 3 before running the project setup."
  else
    python3 -m pip install -r requirements.txt
fi

# for Windows users
# py -m pip install -r requirements.txt


# See the following for creating a Reddit app and adding OAuth:
# https://github.com/reddit-archive/reddit/wiki/OAuth2