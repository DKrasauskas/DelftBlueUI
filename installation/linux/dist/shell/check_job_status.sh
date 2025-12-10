#!/bin/bash


check(){
  local user="$1"
  ssh  "$user"@login.delftblue.tudelft.nl  "squeue --me"
}

check_full(){
  local user="$1"
  ssh  "$user"@login.delftblue.tudelft.nl  "squeue --me && echo @ &&  squeue --start"
}

if [[ "$1" == "check" ]]; then
    check "$2"
fi

if [[ "$1" == "check2" ]]; then
    check_full "$2"
fi