param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("retrieve", "send")]
    $Action,

    [Parameter(Mandatory=$true)]
    $User
)

function Retrieve {
    param($User)

    $remoteDir = "remote"

    if (-not (Test-Path $remoteDir)) {
        New-Item -ItemType Directory -Path $remoteDir | Out-Null
    }

    rsync -avz --delete "$User@login.delftblue.tudelft.nl:~/remote/" $remoteDir
}

function Send {
    param($User)

    rsync -avz --delete "remote" "$User@login.delftblue.tudelft.nl:~/"
}

switch ($Action) {
    "retrieve" { Retrieve $User }
    "send"     { Send $User }
}