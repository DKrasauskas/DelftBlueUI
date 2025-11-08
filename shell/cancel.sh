#!/bin/bash
terminate(){
  local id="$1"
  ssh  dkrasauskas@login.delftblue.tudelft.nl  "scancel ${id}"
}

if [[ "$1" == "terminate" ]]; then
    id="$2"
    terminate "$id"
fi