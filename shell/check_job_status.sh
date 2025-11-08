#!/bin/bash


check(){
  ssh  dkrasauskas@login.delftblue.tudelft.nl  "squeue --me"
}

if [[ "$1" == "check" ]]; then
    check
fi