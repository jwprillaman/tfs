#!/bin/sh
DIR=$( cd "( dirname "${BASH_SOURCE[0]}" )" && pwd )
echo $3
python /home/jim/Dev/tfs/tfs.py -done "$3"
