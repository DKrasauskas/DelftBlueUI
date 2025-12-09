param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("check", "check2")]
    $Action,

    [Parameter(Mandatory=$true)]
    $User
)

function Check-Queue {
    param($User)

    ssh "$User@login.delftblue.tudelft.nl" "squeue --me"
}

function Check-Queue-Full {
    param($User)

    ssh "$User@login.delftblue.tudelft.nl" "squeue --me && echo @ && squeue --start"
}

switch ($Action) {
    "check"  { Check-Queue $User }
    "check2" { Check-Queue-Full $User }
}