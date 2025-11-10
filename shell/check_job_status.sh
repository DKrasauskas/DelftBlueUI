#!/bin/bash


check(){
  local user="$1"
  ssh  "$user"@login.delftblue.tudelft.nl  "squeue --me"
}

if [[ "$1" == "check" ]]; then
    check "$2"
fi