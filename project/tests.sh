#!/bin/bash
#To execute the '.sh' file on your local system, ensure you modify the file paths accordingly to match your local directory structure.
#pip install -r requirements.txt
#if python3 automated_testing.py ;
# echo ">>> installing required packages..."
# pip3  install -r ./project/requirements.txt
echo ">>> running the tests ..."
export PYTHONPATH=$(pwd)/project
echo "PYTHONPATH set to $PYTHONPATH"

echo "Installing required Python libraries..."
pip install --no-cache-dir -r ./project/requirements.txt


echo "Running the tests..."
pytest ./project/automated_test.py -v

