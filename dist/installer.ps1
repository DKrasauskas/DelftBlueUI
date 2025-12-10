$desktop = [Environment]::GetFolderPath("Desktop")
$shortcutPath = Join-Path $desktop "DelftBlue.lnk"
$currentDir = Get-Location
$exeName = "main.exe"
$iconPath = Join-Path $currentDir "backends\icon.ico"
$targetPath = Join-Path $currentDir $exeName


$WshShell = New-Object -ComObject WScript.Shell



# shortcut
$shortcut = $WshShell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $targetPath
$shortcut.WorkingDirectory = Split-Path $targetPath
$shortcut.IconLocation = $iconPath
$shortcut.Save()

Write-Host "Finished"