# Sync demo/ -> public/ for Vercel static hosting at /
$root = Split-Path $PSScriptRoot -Parent
$demo = Join-Path $root "demo"
$public = Join-Path $root "public"
if (Test-Path $public) { Remove-Item -Recurse -Force $public }
New-Item -ItemType Directory -Path $public | Out-Null
Copy-Item -Recurse -Force (Join-Path $demo "*") $public
Write-Output "Synced demo -> public"
