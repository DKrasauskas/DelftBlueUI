run(){
  local dir="$1"
  local user="$2"
  ssh  "$user"@login.delftblue.tudelft.nl "cd $dir &&  sbatch request.sh"
}

if [[ "$1" == "run" ]]; then
    run "$2" "$3"
fi