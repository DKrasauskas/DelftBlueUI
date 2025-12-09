param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("A")]
    $Action,

    [Parameter(Mandatory=$true)]
    $User
)

function Connect-Cluster {
    param($User)
    ssh  "$User@login.delftblue.tudelft.nl"
}

switch ($Action) {
    "A" { Connect-Cluster $User }
}