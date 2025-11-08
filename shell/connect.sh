#!/bin/bash
connect(){
  ssh  dkrasauskas@login.delftblue.tudelft.nl
}

if [[ "$1" == "" ]]; then
    connect
fi