#!/bin/bash

retrieve(){
  local user="$1"
  local remote_path="$2"
  mkdir -p $remote_path
  rsync -avz --delete  "$user"@login.delftblue.tudelft.nl:~/remote/ $remote_path
}
send(){
  local user="$1"
  local remote_path="$2"
  rsync -avz --delete  $remote_path "$user"@login.delftblue.tudelft.nl:~/
}


export -f send
export -f retrieve

if [[ "$1" == "retrieve" ]]; then
    retrieve "$2" "$3"
fi

if [[ "$1" == "send" ]]; then
    send "$2" "$3"
fi