# Run the shipped engine with real Windows rendering and isolated test saves.
param([string]$TestCase = 'cs_vertical_slice')
$ErrorActionPreference = 'Stop'
$csGameRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..\..')).Path
$csModRoot = Split-Path $PSScriptRoot -Parent
$csSaveRoot = Join-Path $csModRoot 'qa\saves'
New-Item -ItemType Directory -Force -Path $csSaveRoot | Out-Null
$env:SDL_VIDEODRIVER = 'windows'
$env:SDL_AUDIODRIVER = 'directsound'
$env:RENPY_RENDERER = 'gl2'
$env:RENPY_SKIP_SPLASHSCREEN = '1'
$csLogName = if ($TestCase -eq 'cs_vertical_slice') { 'runtime_final.txt' } else { $TestCase + '.txt' }
& (Join-Path $csGameRoot 'lib\windows-x86_64\python.exe') (Join-Path $csGameRoot 'Everlasting Summer.py') $csGameRoot test $TestCase --savedir $csSaveRoot > (Join-Path $csModRoot ('qa\' + $csLogName)) 2>&1
$csTestExitCode = $LASTEXITCODE
exit $csTestExitCode
