#!/bin/bash
connect(){
  ssh  dkrasauskas@login.delftblue.tudelft.nl
}

if [[ "$1" == "A" ]]; then
    connect
fi