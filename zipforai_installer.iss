; --- zipforai_installer.iss -----------------------------------

[Setup]
AppName=ZipForAI
AppVersion=1.0
DefaultDirName=C:\ZipForAI
DisableDirPage=yes
DisableProgramGroupPage=yes
OutputDir=installer\dist
OutputBaseFilename=zipforai_setup
Compression=lzma
SolidCompression=yes
SetupIconFile=media\zipforai.ico       

[Files]
; main executable
Source: "zipforai.exe";       DestDir: "{app}"; Flags: ignoreversion
; icon file (so Explorer can load it directly)
Source: "media\zipforai.ico"; DestDir: "{app}"; Flags: ignoreversion

[Registry]
; wipe any stale key first
Root: HKCR; Subkey: "Directory\\shell\\ZipForAI"; Flags: deletekey

; fresh context-menu entry
Root: HKCR; Subkey: "Directory\\shell\\ZipForAI";               ValueType: string; ValueName: "";      ValueData: "Zip for AI";             Flags: uninsdeletekey
Root: HKCR; Subkey: "Directory\\shell\\ZipForAI";               ValueType: string; ValueName: "Icon";  ValueData: "{app}\\zipforai.ico";     Flags: uninsdeletekey
Root: HKCR; Subkey: "Directory\\shell\\ZipForAI\\command";      ValueType: string; ValueName: "";      ValueData: """{app}\\zipforai.exe"" ""%1"""; Flags: uninsdeletekey

[Run]
Filename: "{app}\\zipforai.exe"; Description: "Run ZipForAI now"; Flags: nowait postinstall skipifsilent
