param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("terminate", "submit")]
    $Action,

    [Parameter(Mandatory=$true)]
    $Id,

    [Parameter(Mandatory=$true)]
    $User
)

function Terminate-Job {
    param($Id, $User)
    ssh "$User@login.delftblue.tudelft.nl" "scancel $Id"
}

function Submit-Job {
    param($Id, $User)
    ssh "$User@login.delftblue.tudelft.nl" "scancel $Id"
}

switch ($Action) {
    "terminate" { Terminate-Job $Id $User }
    "submit"    { Submit-Job $Id $User }
}