#!/bin/bash
connect(){
  local user="$1"
  ssh  "$user"@login.delftblue.tudelft.nl
}

if [[ "$1" == "A" ]]; then
    connect "$2"
fi