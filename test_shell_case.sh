#!/bin/bash
option=$1
case $option in
    -f) 
        echo "File name is FILE"
        ;;
    -d) 
        echo "Dir name is DIR"
        ;;
    "abc")
        echo "abc"
        ;;
    *) 
        echo "`basename ${0}`:usage: [-f file] | [-d directory]"
        exit 1 # Command to come out of the program with status 1
        ;;
esac
