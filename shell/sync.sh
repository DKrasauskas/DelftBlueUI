#!/bin/bash

retrieve(){
  local user="$1"
  mkdir -p remote
  rsync -avz --delete  "$user"@login.delftblue.tudelft.nl:~/remote/ remote
}
send(){
  local user="$1"
  rsync -avz --delete  remote "$user"@login.delftblue.tudelft.nl:~/
}



export -f send
export -f retrieve

if [[ "$1" == "retrieve" ]]; then
    retrieve "$2"
fi

if [[ "$1" == "send" ]]; then
    send "$2"
fi