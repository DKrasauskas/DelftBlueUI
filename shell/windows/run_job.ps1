param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("run")]
    $Action,

    [Parameter(Mandatory=$true)]
    $Dir,

    [Parameter(Mandatory=$true)]
    $User
)

function Run-Job {
    param($Dir, $User)

    ssh "$User@login.delftblue.tudelft.nl" "cd $Dir && sbatch request.sh"
}

switch ($Action) {
    "run" { Run-Job $Dir $User }
}