@ECHO OFF

echo Dieses Skript kann Miyamoto starten und/oder die
echo aktuelle Spritedaten und Kategoriedaten-XMLs aus dem Internet.
echo.
echo Anforderung:
echo - Python 3+, installiert im Pfad (stellen Sie sicher, dass der Befehl py funktioniert)
echo - PowerShell 3.0 (fuer den Download von Uebersetzungs Updates und anderen dateien), enthalten
echo   standardmaessig unter Windows 10, fuer andere Versionen von Windows,
echo   muessen Sie den Installer aus dem Internet herunterladen.
echo.
echo Geniessen Sie es!

echo Downloading latest spritedata...
powershell -Command "Invoke-WebRequest https://pastebin.com/raw/tvfQWENS -OutFile miyamotodata/entrancetypes.txt"
echo Done!

echo Downloading latest music...
powershell -Command "Invoke-WebRequest https://pastebin.com/raw/HQTWcxQP -OutFile miyamotodata/music.txt"
echo Done!

echo Downloading latest category...
powershell -Command "Invoke-WebRequest https://pastebin.com/raw/usYcVZ9L -OutFile miyamotodata/spritecategories.xml"
echo Done!

echo Downloading latest spritedata...
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/Gota7/Miyamoto/master/miyamotodata/spritedata.xml -OutFile miyamotodata/spritedata.xml"
echo Done!

echo Downloading latest ts1_descriptions...
powershell -Command "Invoke-WebRequest https://pastebin.com/raw/BR6rEga3 -OutFile miyamotodata/ts1_descriptions.txt"
echo Done!

echo Downloading latest strings...
powershell -Command "Invoke-WebRequest https://pastebin.com/raw/aALSGhRn -OutFile strings.py"
echo Done!

py miyamoto.py

echo Downloading the latest version...
powershell -Command "Invoke-WebRequest https://pastebin.com/raw/HT5pfYnY -OutFile run-python.bat"
echo Done!

EXIT