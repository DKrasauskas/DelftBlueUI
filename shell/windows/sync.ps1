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
    Write-Host "Current directory: $PWD"
    & .\shell\windows\rsync\bin\rsync.exe -avz --delete -e ".\shell\windows\rsync\bin\ssh.exe" "$User@login.delftblue.tudelft.nl:~/remote/" $remoteDir
}

function Send {
    param($User)
    Write-Host "Current directory: $PWD"
    & .\shell\windows\rsync\bin\rsync.exe -avz --delete -e ".\shell\windows\rsync\bin\ssh.exe" "remote" "$User@login.delftblue.tudelft.nl:~/"
}

switch ($Action) {
    "retrieve" { Retrieve $User }
    "send"     { Send $User }
}