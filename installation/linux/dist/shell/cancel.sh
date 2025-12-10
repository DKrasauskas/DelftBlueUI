#!/bin/bash
terminate(){
  local id="$1"
  local user="$2"
  ssh  "$user"@login.delftblue.tudelft.nl  "scancel ${id}"
}

submit(){
  local id="$1"
  local user="$2"
  ssh  "$user"@login.delftblue.tudelft.nl  "scancel ${id}"
}

if [[ "$1" == "terminate" ]]; then
    id="$2"
    terminate "$id" "$3"
fi