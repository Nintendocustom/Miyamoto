# Miyamoto!
## Der New Super Mario Bros. U / New Super Luigi U Editor
Ein Level-Editor f�r NSMBU und NSLU von AboodXD und Gota7, basierend auf Reggie! Next von RoadrunnerWMC, das auf Reggie von Treeki basiert, Tempus et al. verwendet Python 3, PyQt5, SarcLib und libyaz0.

----------------------------------------------------------------

Discord: https://discord.gg/AvFEHpp  
GitHub: https://github.com/aboood40091/Miyamoto  

----------------------------------------------------------------

### Credits
##### Reggie! & Reggie! Next
* Treeki -- Ersteller von Reggie!
* RoadrunnerWMC -- Ersteller von Reggie! Weiter
  
###### Miyamoto
* AboodXD -- Hauptprogrammierer, Spritedaten, Grafiken
* Gota7 -- Programmierung, Spritedaten, Grafiken, etc.
* Grop -- Programmierer, Spritedaten
* Gregory Haskins -- Gibberish
* John10v10 -- Quick Paint Tool
* libtxc_dxtn -- Original DXT5 (De)compressor in C
* Luzifer -- Grafiken
* Mayro -- Grafiken
* mrbengtsson -- Programmierung, Spritedaten, Grafiken
* Meorge -- Tests unter macOS
* NVIDIA -- NVCOMPRESS
* RicBent -- Grafiken
* reece stone -- Spritedata, Graphics
* Shawn Shea -- Grafiken
* Toms -- Spritedaten, Grafiken
* Wexos -- Originaler BC3 Kompressor in C#
* Wiimm -- WSZST
  
#### Reggie NSMBU
* Grop -- Programmierer, Spritedaten, Grafiken
* Hiccup -- Spritedaten
* Kinnay -- Spritedaten
* MrRean -- Programmierer, Spritedaten, Kategorien, Grafiken, etc.
* RoadrunnerWMC -- Programmierer, Spritedaten, Grafiken

----------------------------------------------------------------

#### TODO
- Unbekannte Gebietsfelder herausfinden
- Sprite-Bilder / HD-Screenshots (viele davon)
- Verbessern der Gr��en�nderung von Zonen und Objekten

----------------------------------------------------------------

### Miyamoto bauen
Bitte beachten Sie, dass du beim Bau von Miyamoto alle Instanzen der Nutzung von Cython sowohl in Miyamoto als auch in libyaz0 entfernen musst. (Pyximport)  
Alternativ kann man die .pyx-Dateien erstellen und dann alle Instanzen von Pyximport im Code entfernen.

----------------------------------------------------------------

### Wie man es benutzt
Zuerst l�dst du diesen Repo herunter (entweder durch die Verwendung von ```git clone``` oder ```git pull```, wenn du es bereits geklont hast), oder durch das Herunterladen einer Version, oder indem du einfach diesen Repo als Ganzes herunterl�dst.

Zweitens ben�tigst du das Dateisystem von New Super Mario Bros. U. Du kannst es bekommen, indem du das Spiel mit ddd dumpst: https://gbatemp.net/threads/ddd-wiiu-title-dumper.418492/

Drittens, Lade das Folgende herunter und installiere es:
 * Python 3.4 (oder neuer) - http://www.python.org
 * PyQt 5.3 (oder neuer) - http://www.riverbankcomputing.co.uk/software/pyqt/intro
 * SarcLib (pip3 install SarcLib)
 * libyaz0 (pip3 install libyaz0)
 * cx_Freeze 4.3 (oder neuer) (optional) - http://cx-freeze.sourceforge.net  

F�hre Folgendes in einer Eingabeaufforderung aus:  
`python3 miyamoto.py`  
Sie k�nnen `python3` durch den Pfad zu python.exe (mit "python.exe" am Ende) und `miyamoto.py` durch den Pfad zu miyamoto.py (mit "miyamoto.py" am Ende) ersetzen.  
  
Es wird dich bitten, einen Ordner zu w�hlen. W�hle den Ordner course_res_pack, oder wo du die Level gespeichert hast (mindestens 1-1.szs).

Viel Spa�.
