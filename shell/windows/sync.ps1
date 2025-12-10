param(
    [Parameter(Mandatory=$true)]
    [ValidateSet("retrieve", "send")]
    $Action,

    [Parameter(Mandatory=$true)]
    $User,
    [Parameter(Mandatory=$true)]
    $location
)

function Retrieve {
    param($User, $location)
    $remoteDir = "$location"

    if (-not (Test-Path $remoteDir)) {
        New-Item -ItemType Directory -Path $remoteDir | Out-Null
    }
    Write-Host "Current directory: $PWD"
    & .\shell\windows\rsync\bin\rsync.exe -avz --delete -e ".\shell\windows\rsync\bin\ssh.exe" "$User@login.delftblue.tudelft.nl:~/remote/" $remoteDir
}

function Send {
    param($User, $location)
    Write-Host "Current directory: $PWD"
    & .\shell\windows\rsync\bin\rsync.exe -avz --delete -e ".\shell\windows\rsync\bin\ssh.exe" "$location" "$User@login.delftblue.tudelft.nl:~/"
}

switch ($Action) {
    "retrieve" { Retrieve $User $location }
    "send"     { Send $User $location }
}