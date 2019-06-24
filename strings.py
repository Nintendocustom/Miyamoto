#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Miyamoto! Level Editor - New Super Mario Bros. U Level Editor
# Copyright (C) 2009-2019 Treeki, Tempus, angelsl, JasonP27, Kinnay,
# MalStar1000, RoadrunnerWMC, MrRean, Grop, AboodXD, Gota7, John10v10

# This file is part of Miyamoto!.

# Miyamoto! is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Miyamoto! is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Miyamoto!.  If not, see <http://www.gnu.org/licenses/>.

# strings.py
# Strings for labels, tooltips, and more


################################################################
################################################################

############ Imports ############

import os.path
from xml.etree import ElementTree as etree

#################################


class MiyamotoTranslation:
    """
    A translation of all visible Miyamoto strings
    """
    def __init__(self, name):
        """
        Creates a Miyamoto translation
        """
        self.InitAsEnglish()

        # Try to load it from an XML
        try:
            self.InitFromXML(name)
        except Exception:
            self.InitAsEnglish()


    def InitAsEnglish(self):
        """
        Initializes the MiyamotoTranslation as the English translation
        """
        self.name = 'German'
        self.version = 1.0
        self.translator = 'Treeki, Tempus, AboodXD'

        self.files = {
            'bg': 'miyamotodata/bg.txt',
            'bgTrans': 'miyamotodata/bgTrans.txt',
            'entrancetypes': 'miyamotodata/entrancetypes.txt',
            'levelnames': 'miyamotodata/levelnames.xml',
            'music': 'miyamotodata/music.txt',
            'spritecategories': 'miyamotodata/spritecategories.xml',
            'spritedata': 'miyamotodata/spritedata.xml',
            'tilesets': 'miyamotodata/tilesets.xml',
            'ts1_descriptions': 'miyamotodata/ts1_descriptions.txt',
            }

        self.strings = {
            'AboutDlg': {
                0: 'Über Miyamoto!',
                },
            'AreaChoiceDlg': {
                0: 'Wähle einen Bereich',
                1: 'Bereich [num]',
                2: 'Du hast die maximale Anzahl von Bereichen in diesem Level erreicht.[br]Aufgrund der Einschränkungen des Spiels erlaubt Miyamoto! nur das Hinzufügen von bis zu 4 Bereichen in einem Level.',
                },
            'AreaCombobox': {
                0: 'Bereich [num]',
                },
            'AreaDlg': {
                0: 'Bereich Optionen',
                1: 'Tilesets',
                2: 'Einstellungen',
                3: 'Zeit:',
                4: '[b]Zeit:[/b][br]Die Standart Zeit. Setze das Limit, in "Mario Sekunden," für das Level.[br][b]Midway Timer Info:[/b] Der Midway-Timer wird berechnet, indem von diesem Wert 100 abgezogen werden.',
                5: 'Eingangs-ID:',
                6: '[b]Eingangs-ID:[/b][br]Legt die Eingangs-ID fest, in die geladen werden soll, wenn von der Weltkarte geladen wird.',
                7: 'Wickeln über Kanten',
                8: '[b]Wickel über Kanten:[/b][br]Lässt die Kanten der Bühne umhüllen[br]Warnung: Die Verpackung funktioniert nur dann richtig, wenn der Bereich richtig eingerichtet ist.',
                9: None, # REMOVED: 'Event [id]'
                10: None, # REMOVED: 'Default Events'
                11: 'Standart Suite',
                12: 'Stage Suite',
                13: 'Hintergrund Suite',
                14: 'Interaktiver Suite',
                15: 'Keine',
                16: '[CUSTOM]',
                17: '[CUSTOM] [name]',
                18: 'Custom Dateiname... [name]',
                19: '[name] ([file])',
                20: 'Gebe einen Dateinamen ein',
                21: 'Gib den Namen einer benutzerdefinierten Tileset-Datei ein, die verwendet werden soll. It must be placed in the game\'s Stage\\Texture or Unit folder in order for Miyamoto to recognize it. Do not add the \'.arc\' or \'.sarc\' extension at the end of the filename.',
                22: 'Unbekannter Wert 1:',
                23: 'Unbekannter Wert 2:',
                24: 'Unbekannter Wert 3:', # Currently unused
                25: '[b]Unbekannter Wert 1:[/b] Wir haben es nicht geschafft herauszufinden, was das bewirkt, oder ob es etwas bewirkt.',
                26: '[b]Unbekannter Wert 2:[/b] Wir haben es nicht geschafft herauszufinden, was das bewirkt, oder ob es etwas bewirkt.',
                27: '[b]Unbekannter Wert 3:[/b] Wir haben es nicht geschafft herauszufinden, was das bewirkt, oder ob es etwas bewirkt.', # Currently unused
                28: 'Name',
                29: 'Datei',
                30: '(Keine)',
                31: 'Tileset (Pa[slot]):',
                32: 'Unbekannter Wert 4:',
                33: 'Unbekannter Wert 5:',
                34: 'Eingangs-ID 2:',
                35: 'Unbekannter Wert 6:',
                36: 'Zeit 2:',
                37: 'Zeit 3:',
                38: '[b]Zeit 2 & 3:[/b]Dieses Zeitlimit wird vom nybble 12 auf sprite 25, Checkpoint Flag, gewählt. Siehe Sprite für Details.',                
                39: '[b]Eingangs-ID 2:[/b][br]Legt die Eingangs-ID fest, in die geladen werden soll, beim Laden aus dem Coin Battle oder Boost Rush Menü.',
				40: 'Unbekannte Option 1',
                41: '[b]Unbekannte Option 1:[/b] Wir haben es nicht geschafft herauszufinden, was das bewirkt, oder ob es etwas bewirkt. Diese Option ist in den meisten Levels deaktiviert.',
                42: 'Unbekannte Option 2',
                43: '[b]Unbekannte Option 2:[/b] Wir haben es nicht geschafft herauszufinden, was das bewirkt, oder ob es etwas bewirkt. Diese Option ist in den meisten Levels deaktiviert.',
                44: 'Unbekannte Option 3',
                45: '[b]Unbekannte Option 3:[/b] Wir haben es nicht geschafft herauszufinden, was das bewirkt, oder ob es etwas bewirkt. Diese Option ist in den meisten Levels deaktiviert.',
                46: 'Unbekannte Option 4',
                47: '[b]Unbekannte Option 4:[/b] Wir haben es nicht geschafft herauszufinden, was das bewirkt, oder ob es etwas bewirkt. Diese Option ist in den meisten Levels deaktiviert.',
                },
            'AutoSaveDlg': {
                0: 'Automatisch gespeichertes Backup gefunden',
                1: 'Miyamoto! hat einige Level-Daten gefunden, die nicht gespeichert wurden - möglicherweise aufgrund eines Absturzes im Editor oder von Ihrem Computer. Möchtest du diesen Level wiederherstellen?[br][br]Wenn du Nein wählst, werden die automatisch gespeicherten Level-Daten gelöscht und sind nicht mehr zugänglich.[br][br]Ursprünglicher Dateipfad: [path]',
                2: 'Wenn du ein gutes Level machst, gibst du auf.',
                3: 'Wenn du kein gutes Level machst, bleibst du.',
                },
            'BGDlg': {
                0: 'Hintergründe',
                1: (
                    'None',
                    '0.125x',
                    '0.25x',
                    '0.375x',
                    '0.5x',
                    '0.625x',
                    '0.75x',
                    '0.875x',
                    '1x',
                    'None',
                    '1.25x',
                    '1.5x',
                    '2x',
                    '4x',
                    ),
                2: 'Zone [num]',
                3: 'Scenery',
                4: 'Hintergrund',
                5: 'Position:',
                6: 'X:',
                7: '[b]Position (X):[/b][br]Legt den horizontalen Offset deines Hintergrunds fest',
                8: 'Y:',
                9: '[b]Position (Y):[/b][br]Legt den vertikalen Versatz des Hintergrunds fest',
                10: 'Scrollgeschwindigkeit:',
                11: '[b]Scrollgeschwindigkeit (X):[/b][br]Ändert die Geschwindigkeit, mit der sich der Hintergrund in[br]-Beziehung zu Mario bewegt, wenn er sich horizontal bewegt.[br]Werte größer als 1x können störend sein!',
                12: '[b]Scrollgeschwindigkeit (Y):[/b][br]Ändert die Geschwindigkeit, mit der sich der Hintergrund in[br]-Beziehung zu Mario bewegt, wenn er sich horizontal bewegt.[br]Werte größer als 1x können störend sein!',
                13: 'Zoom:',
                14: '[b]Zoom:[/b][br]Legt die Zoomstufe des Hintergrundbildes fest.',
                15: (
                    '100%',
                    '125%',
                    '150%',
                    '200%',
                    ),
                16: 'Vorschau',
                17: '[name] ([hex])',
                18: '(Custom)',
                19: 'Hintergrundtypen:',
                20: 'Ausrichtungsmodus: Diese Kombination von Hintergründen führt zu folgenden Ergebnissen "[mode]"',
                21: (
                    'Normal',
                    'Unbekannt 1',
                    'Unbekannt 2',
                    'Unbekannt 3',
                    'Unbekannt 4',
                    'Auf Bildschirm ausrichten',
                    'Unbekannt 5',
                    'Unbekannt 6',
                    ),
                22: 'Warnung',
                23: '"Lava 2" BG benötigt Sprites: 473, 477, 487, 497.[br]Natürlich musst du diese Sprites richtig einrichten, damit das Spiel nicht abstürzt.[br]Schau dir 8-43 Bereich 3 an.',
                },
            'ChangeGamePath': {
                0: 'Wähle den Stage-Ordner von [game]',
                1: 'Fehler',
                2: 'Dieser Ordner enthält nicht alle Dateien aus dem extrahierten NSMBU Ordner course_res_pack.',
                3: 'Dieser Ordner scheint nicht die erforderlichen Dateien zu haben. Um Miyamoto! nutzen zu können, du benötigst den Stage-Ordner des Spiels, einschließlich des Textur-Ordners und der darin enthaltenen Level-Dateien.',
                },
            'Comments': {
                0: '[x], [y]: [text]',
                1: '[b]Kommentar[/b][br]at [x], [y]',
                2: ' - ',
                3: '(empty)',
                4: '...',
                },
            'DeleteArea': {
                0: 'Bist du [b]sicher,[/b] dass du diesen Bereich löschen möchtest?[br][br]Der Level wird danach automatisch gespeichert - es gibt keine Möglichkeit.[br]Du kannst die Löschung rückgängig machen oder sie danach wieder zurückerhalten!',
                },
            'EntranceDataEditor': {
                0: 'ID:',
                1: '[b]ID:[/b][br]Muss sich von allen anderen IDs unterscheiden.',
                2: 'Type:',
                3: '[b]Type:[/b][br]Legt fest, wie sich der Eingang verhält.',
                4: 'Dest. ID:',
                5: '[b]Ziel-ID:[/b][br]Wenn dieser Eingang nirgendwo hinführt oder das Ziel in diesem Bereich liegt, setze ihn auf 0.',
                6: 'Dest. Area:',
                7: '[b]Zielbereich:[/b][br]Wenn dieser Eingang nirgendwo hinführt, setze ihn auf 0..',
                8: 'Enterable',
                9: '[b]Enterable:[/b][br]Wenn dieses Kästchen bei einer Röhre- oder Türeingang angekreuzt ist, kann Mario die Röhre/Tür betreten. Wenn es nicht angekreuzt wird, wird er nicht in der Lage sein, es zu betreten. Das Verhalten an anderen Arten von Eingängen ist Unbekannt/undefiniert.',
                10: 'Unbekannt Flag',
                11: '[b]Unbekannt Flag:[/b][br]Dieses Kästchen ist bei einigen Eingängen im Spiel angekreuzt, aber wir haben es nicht geschafft, herauszufinden, was es bewirkt (oder ob es etwas bewirkt).',
                12: 'Verbundene Röhre',
                13: '[b]Verbundene Röhre:[/b][br]Diese Box ermöglicht es dir, eine unbenutzte/kaputte Funktion im Spiel zu aktivieren. Es ermöglicht, dass das Rohr wie die Rohre in SMB3 funktioniert, wo Mario einfach durch das Rohr geht. Allerdings funktioniert es nicht richtig..',
                14: 'Verbundene Röhre Rückwärts',
                15: '[b]Verbundenes Rohr:[/b][br]Diese Box ermöglicht es dir, eine unbenutzte/kaputte Funktion im Spiel zu aktivieren. Es ermöglicht, dass das Rohr wie die Rohre in SMB3 funktioniert, wo Mario einfach durch das Rohr geht. Allerdings funktioniert es nicht richtig.',
                16: 'Pfad-ID:',
                17: '[b]Pfad-ID:[/b][br]Verwende diese Option, um die Pfadnummer einzustellen, der die angeschlossene Leitung folgen soll..',
                18: 'Links zur Vorwärtsröhre',
                19: '[b]Links zur Vorwärtsröhre:[/b][br]Wenn diese Option auf einer Röhre eingestellt ist, werden die Werte für den Zieleingang bzw. die Zielfläche ignoriert - Mario geht durch die Röhre und erscheint dann wieder, aus einer nach vorne gerichteten Röhre.',
                20: 'Ebene:',
                21: ('Ebene 1', 'Ebene 2', 'Ebene 0'),
                22: '[b]Ebene:[/b][br]Ermöglicht es Ihnen, die Kollisionsschicht zu ändern, in der dieser Eingang aktiv ist. Diese Option ist sehr glitchy und wird nicht in den Standard-Levels verwendet - für fast alle normalen Fälle wird Ebene 1 verwendet.',
                23: '[b]Eingang [id]:[/b]',
                24: 'Ändern der ausgewählten Eingangseigenschaften',
                25: 'CP Ausgangsrichtung:',
                26: '[b]CP Ausgangsrichtung:[/b][br]Stelle die Richtung ein, in die der Spieler aus einer angeschlossenen Röhre austreten soll.',
                27: (
                    'Hoch',
                    'Unten',
                    'Links',
                    'Rechts',
                    ),
                28: '([id]) [name]',
                29: '[b]Players to spawn:[/b][br]Spieler Spawn an diesem Eingang. Wird in Hinterhaltslevels verwendet.',
                30: '[b]Kamera X-Position:[/b][br]Wird verwendet, um den Punkt zu verschieben, auf dem die Kamera zentriert ist. Position in Bezug auf den\die Eingang\Eingänge.[br]16 = 1 Block.',
                31: '[b]Kamera Y-Position:[/b][br]Wird verwendet, um den Punkt zu verschieben, auf dem die Kamera zentriert ist. Position in Bezug auf den\die Eingang\Eingänge.[br]16 = 1 Block.',
                },
            'Entrances': {
                0: '[b]Eingang [ent]:[/b][br]Typ: [type][br][i][dest][/i]',
                1: 'Unbekannt',
                2: '(kann nicht betreten werden)',
                3: '(kommt am Eingang[id] in diesem Bereich an.)',
                4: '(kommt am Eingang[id] im Bereich[area] an.)',
                5: '[id]: [name] (kann nicht betreten werden) bei [x], [y]',
                6: '[id]: [name] (betretbar) bei [x], [y]'
                },
            'Err_BrokenSpriteData': {
                0: 'Warnung',
                1: 'Die Sprite-Datendatei wurde nicht korrekt geladen. Die folgenden Sprites haben falsche und/oder defekte Daten in sich und können möglicherweise nicht korrekt im Editor bearbeitet werden: [sprites]',
                2: 'Fehler',
                },
            'Err_CantFindLevel': {
                0: 'Datei konnte nicht gefunden werden:[br][name]',
                },
            'Err_CorruptedTileset': {
                0: 'Fehler',
                1: 'Beim Versuch, die Datei [file].szs zu laden, ist ein Fehler aufgetreten. Überprüfen den Ordner, um sicherzustellen, dass es vollständig und nicht beschädigt ist. Der Editor kann in einem defekten Zustand laufen oder abstürzen.',
                },
            'Err_CorruptedTilesetData': {
                0: 'Fehler',
                1: 'Die gewünschte Textur kann in der Tileset-Datei[file].szs nicht gefunden werden, so dass sie nicht geladen wird. Beachte, dass die Tileset-Datei nicht umbenannt werden kann, ohne die Namen der Textur-/Objektdateien im Archiv zu ändern!',
                },
            'Err_InvalidLevel': {
                0: 'Diese Datei scheint keine gültiges Level zu sein.',
                },
            'Err_MissingFiles': {
                0: 'Fehler',
                1: 'Sorry, du scheinst die erforderlichen Dateien für Miyamoto! nicht zu haben, damit es funktioniert. Bitte lade eine Kopie des Editors erneut herunter.',
                2: 'Sorry, es scheint dir fehlen einige der benötigten Dateien für Miyamoto! zu fehlen, damit es funktioniert. Bitte lade eine Kopie des Editors erneut herunter. Dies sind die Dateien, die du brauchst: [Dateien]',
                },
            'Err_MissingLevel': {
                0: 'Fehler',
                1: 'Die gewünschte Level-Datei[file].arc kann nicht gefunden werden. Überprüfe den Stage-Ordner und stelle sicher, dass er existiert.',
                },
            'Err_MissingTileset': {
                0: 'Fehler',
                1: 'Die gewünschte Tileset-Datei[file].arc kann nicht gefunden werden. Kontrolliere deinen Stage-Ordner und stelle sicher, dass er existiert.',
                },
            'Err_Save': {
                0: 'Fehler',
                1: 'Fehler beim Versuch von Miyamoto, den Level zu speichern:[br](#[err1])[err2][br][br][br](Ihre Arbeit wurde nicht gespeichert! Versuche, es unter einem anderen Dateinamen oder in einem anderen Ordner zu speichern.)',
                },
            'FileDlgs': {
                0: 'Wähle ein Level-Archiv aus',
                1: 'Level-Archive',
                2: 'Alle Dateien',
                3: 'Einen neuen Dateinamen wählen',
                4: 'Tragbare Netzwerkgrafiken',
                5: 'Komprimierte Level-Archive',
                6: 'Wähle ein Stempelarchiv aus',
                7: 'Stempeldatei',
                8: 'Komprimierte Level-Archive',
                9: 'Unkomprimierte Level-Archive',
                },
            'Gamedefs': {
                0: 'Dieses Spiel hat benutzerdefinierte Sprite-Bilder.',
                1: 'Patch wird geladen...',
                2: 'Neuer Spielpatch',
                3: 'Es scheint, dass dies dein erstes Mal ist, dass du den Spielpatch für [game] benutzt. Bitte wähle den Stage Ordner aus, damit benutzerdefinierte Tilesets und Levels geladen werden können.',
                4: 'Abbruch der Auswahl des Spielpfades',
                5: 'Da du den Stage-Ordner für [game] nicht ausgewählt hast, werden Level und Tilesets nicht korrekt geladen. Du kannst es erneut versuchen, indem du Spielpfad ändern wählst, während [game] geladen ist.',
                6: 'Neuer Spielpatch',
                7: 'Du kannst den Spielpfad für [game] jederzeit ändern, indem du Spielpfad ändern wählst, während [game] geladen ist.',
                8: 'Laden von Sprite-Daten...',
                9: 'Laden von Hintergrundnamen...',
                10: 'Neu laden von Tilesets...',
                11: 'Laden von Sprite-Bilddaten...',
                12: 'Sprite-Bilddaten anwenden...',
                13: 'New Super Mario Bros. U',
                14: 'Ein neues Abenteuer, und in HD! [br] Veröffentlicht von Nintendo im August 2012.',
                15: '[i]Keine Beschreibung[/i]',
                16: 'Laden von Eingangsnamen...',
                17: 'Fehler',
                18: 'Beim Versuch, diesen Patch zu laden, ist ein Fehler aufgetreten. Es wird nun entladen. Hier ist der spezifische Fehler:[br][error][error]',
                },
            'InfoDlg': {
                0: 'Level Informationen',
                1: 'Passwort hinzufügen/ändern',
                2: 'This level\'s information is locked.[br]Please enter the password below in order to modify it.',
                3: 'Passwort:',
                4: 'Titel:',
                5: 'Autor:',
                6: 'Gruppe:',
                7: 'Website:',
                8: 'Erstellt mit [name]',
                9: 'Passwort ändern',
                10: 'Neues Passwort:',
                11: 'Passwort bestätigen:',
                12: 'Level Informationen',
                13: 'Das Passwort kann aus einem beliebigen ASCII-Zeichen,[br]und bis zu 64 Zeichen bestehen.[br]',
                14: 'Sorry! [br] [br] Du kannst Level-Informationen nur in Bereich 1 ansehen oder bearbeiten.',
                },
            'LocationDataEditor': {
                0: 'ID:',
                1: '[b]ID:[/b][br]Muss sich von allen anderen IDs unterscheiden.',
                2: 'X Pos:',
                3: '[b]X-Pos:[/b][br]Gibt die X-Position des Ortes an.',
                4: 'Y Pos:',
                5: '[b]Y-Pos:[/b][br]Gibt die Y-Position des Ortes an',
                6: 'Breite:',
                7: '[b]Breite:[/b][br]Gibt die Breite der Position an',
                8: 'Höhe:',
                9: '[b]Höhe:[/b][br]Gibt die Höhe des Ortes an',
                10: 'Am Raster einrasten',
                11: '[b]Orte [id]:[/b]',
                12: 'Modifizieren der Eigenschaften des ausgewählten Ortes',
                },
            'Locations': {
                0: '[id]',
                1: '', # REMOVED: 'Paint New Location'
                2: '[id]: [width]x[height] bei [x], [y]',
                },
            'MainWindow': {
                0: '[nicht gespeichert]',
                1: 'Du versuchst, über 300 Elemente auf einmal einzufügen.[br]Das kann eine Weile dauern (abhängig von der Geschwindigkeit deines Computers), bist du sicher, dass du fortfahren möchtest?',
                },
            'Menubar': {
                0: '&Datei',
                1: '&Bearbeiten',
                2: '&Ansicht',
                3: '&Einstellungen',
                4: '&Tilesets',
                5: '&Hilfe',
                6: 'Editor-Symbolleiste',
                },
            'MenuItems': {
                0: 'Neues Level',
                1: 'Erstelle ein neues, leeres level',
                2: 'Level nach Name öffnen...',
                3: 'Öffne ein Level basierend auf der Anzahl der Welt/Nummer',
                4: 'Öffne Level von einer Datei...',
                5: 'Öffnet ein Level basierend auf ihrem Dateinamen.',
                6: 'Letzte Dateien',
                7: 'Öffnen ein Level aus einer Liste der zuletzt geöffneten Level',
                8: 'Speicher Level',
                9: 'Speicher das Level wieder in der Archivdatei.',
                10: 'Exportiere Level als...',
                11: 'Exportiere das level mit einem neuen Dateinamen',
                12: 'Level Informationen...',
                13: 'Füge Titel- und Autoreninformationen zu den Metadaten des Level hinzu',
                14: 'Level Screenshot...',
                15: 'Mach einen Screenshot deines Levels in voller Größe, damit du ihn mit anderen teilen kannst.',
                16: 'Spielpfad ändern...',
                17: 'Legen einen anderen Ordner fest, in dem du die Spieldateien laden kannst.',
                18: 'Miyamoto! Präferenzen...',
                19: 'Wichtige Miyamoto! Einstellungen ändern',
                20: 'Verlasse Miyamoto!',
                21: 'Verlasse den Editor',
                22: 'Alles auswählen',
                23: 'Alle Objekte in diesem Bereich auswählen',
                24: 'Abwählen',
                25: 'Alle aktuell ausgewählten Objekte abwählen.',
                26: 'Schnitt',
                27: 'Ausschneiden der aktuellen Auswahl in die Zwischenablage',
                28: 'Kopieren',
                29: 'Kopieren der aktuellen Auswahl in die Zwischenablage',
                30: 'Einfügen',
                31: 'Einfügen von Elementen aus der Zwischenablage',
                32: 'Objekte verschieben...',
                33: 'Alle ausgewählten Elemente um einen Offset verschieben',
                34: 'Standorte zusammenführen',
                35: 'Zusammenführen ausgewählter Standorte zu einem einzigen großen Standort',
                36: 'Level Diagnostik Werkzeug...',
                37: 'Finde Probleme mit dem Level und beheben sie',
                38: 'Einfrieren\\nObjekte',
                39: 'Objekte nicht selektierbar machen',
                40: 'Einfrieren\\nSprites',
                41: 'Sprites unauswählbar machen',
                42: 'Einfrieren Eingänge',
                43: 'Eingänge nicht wählbar machen',
                44: 'Einfrieren\\nStandorte',
                45: 'Orte nicht wählbar machen',
                46: 'Einfrieren Pfade',
                47: 'Pfade nicht auswählbar machen',
                48: 'Ebene 0',
                49: 'Umschalten der Anzeige der Ebene 0',
                50: 'Ebene 1',
                51: 'Umschalten der Anzeige der Ebene 1',
                52: 'Ebene 2',
                53: 'Umschalten der Anzeige der Ebene 2',
                54: 'Sprites anzeigen',
                55: 'Umschalten der Anzeige von Sprites',
                56: 'Sprites anzeigen',
                57: 'Umschalten der Anzeige von Sprite-Bildern',
                58: 'Standorte anzeigen',
                59: 'Umschalten der Anzeige von Positionen',
                60: 'Tausch\\nNetz',
                61: 'Welchsel durch die verfügbaren Gitteransichten',
                62: 'Auf Maximum zoomen',
                63: 'Zoome bis zum Anschlag hinein.',
                64: 'Vergrößern',
                65: 'Zoome in die Ansicht des Haupt Level.',
                66: 'Zoom 100%',
                67: 'Zeigt den Level mit dem Standard-Zoom an.',
                68: 'Verkleinern',
                69: 'Verkleinern der Ansicht des Haupt Level',
                70: 'Auf Minimum zoomen',
                71: 'Zoome bis zum Anschlag heraus.',
                72: 'Bereich\\nEinstellungen...',
                73: 'Steuer den Tileset-Austausch, die Levelzeit, den Eingang beim Laden und die Level verpackung.',
                74: 'Zone\\nEinstellungen...',
                75: 'Zonenerstellung, -löschung und Einstellungen',
                76: 'Hintergründe...',
                77: 'Hintergründe auf einzelne Zonen im aktuellen Bereich anwenden',
                78: 'Neuen Bereich hinzufügen',
                79: 'Einen neuen Bereich (Unterebene) zu diesem Level hinzufügen',
                80: 'Bereich aus Level importieren...',
                81: 'Importieren eines Bereichs (Unterebene) aus einer anderen Leveldatei',
                82: 'Aktuellen Bereich löschen...',
                83: 'Löschen Sie den aktuell geöffneten Bereich (Unterebene) aus dem Level',
                84: 'Tilesets neu laden',
                85: 'Laden Sie die Tileset-Datendateien neu, einschließlich aller Änderungen, die seit dem Laden des Levels vorgenommen wurden.',
                86: 'Über Miyamoto!',
                87: 'Informationen über das Programm und das Team dahinter',
                88: 'Hilfeinhalte...',
                89: 'Hilfedokumentation für den bedürftigen Neueinsteiger',
                90: 'Miyamoto! Tipps.Bereich aus Level importieren..',
                91: 'Tipps und Tricks für Einsteiger und Power-User',
                92: 'Über PyQt...',
                93: 'Miyamoto basiert auf der Qt-Bibliothek',
                94: 'Level-Übersicht',
                95: 'Ein- und Ausblenden des Levelübersichts Fensters',
                96: 'Palette',
                97: 'Ein- und Ausblenden des Palettenfensters',
                98: 'Spiel wechseln',
                99: 'Ändert den aktuell geladenen Miyamoto! Spielpatch',
                100: 'Inselgenerator',
                101: 'Ein- und Ausblenden des Inselgeneratoren Fensters',
                102: None, # REMOVED: 'Stamp Pad'
                103: None, # REMOVED: 'Show or hide the Stamp Pad window'
                104: 'Objekte tauschen\' Tileset',
                105: 'Tauscht den tileset von Objekten mit einem bestimmten tileset aus.',
                106: 'Objekte tauschen\' Typ',
                107: 'Tauscht den Typ von Objekten eines bestimmten Typs aus',
                108: 'Tileset Animationen',
                109: 'Wiedergabe von Tileset-Animationen, falls vorhanden (kann zu einer Verlangsamung führen)',
                110: 'Tileset-Kollisionen',
                111: 'Ansicht von Kollisionen von Tilesets für bestehende Objekte',
                112: 'Öffnen Level...',
                113: None, # This keeps the even-odd pattern going, since 112 uses description 3
                114: 'Kommentare einfrieren',
                115: 'Kommentare nicht auswählbar machen',
                116: 'Kommentare anzeigen',
                117: 'Umschalten der Anzeige von Kommentaren',
                118: 'Echte Ansicht',
                119: 'Zeigt Spezialeffekte, die im Level vorhanden sind',
                120: 'Nach Updates suchen...',
                121: 'Überprüfe, ob Updates für Miyamoto! zum Herunterladen verfügbar sind',
                122: 'Hervorheben von 3D-Effekten',
                123: 'Umschalten der Anzeige der 3D-Tiefeneffekt-Hervorhebung (NSMB2 only)',
                124: 'Freeze\\nProgress Paths',
                125: 'Fortschrittspfade nicht wählbar machen',
                126: 'Vollbild anzeigen',
                127: 'Anzeige des Hauptfensters mit allen verfügbaren Bildschirmflächen',
                128: 'Spritedaten neu laden',
                129: 'Lade die Spritedaten neu, ohne den Editor neu zu starten',
                130: 'Bearbeitung des HauptTileset',
                131: 'Bearbeitung des HauptTileset (Slot 1)',
                132: 'Objektpfad ändern...',
                133: 'Setze einen anderen Ordner, um die Objekte zu laden',
                134: 'Überschreibe keine Sprites im Level-Archiv',
                135: 'Überschreibe keine Sprites im Level-Archiv mit Sprites aus dem Datenordner',
                136: 'Quick Paint-Eigenschaften',
                137: 'Zeigt das Eigenschaftenfenster an, um Quick Paint zu konfigurieren',
                138: 'Pfade anzeigen',
                139: 'Umschalten der Anzeige von Pfaden',
                140: 'Die Tilesets immer neu speichern',
                141: 'Speichert die Tilesets beim Speichern des Levels immer neu, außer beim Löschen eines Bereichs',
                142: 'Bearbeitung von Slot [slot] Tileset',
                143: 'Bearbeitung von Slot [slot] Tileset',
                },
            'Objects': {
                0: '[b]Tileset [tileset], Objekt [obj]:[/b][br][width]x[height] on layer [layer]',
                1: 'Tileset [tileset], Objekt [id]',
                2: 'Tileset [tileset], Objekt [id][br][i]Dieses Objekt ist animiert[/i]',
                3: '[b]Tileset [tileset], Objekt [id]:[/b][br][desc]',
                4: '[b]Tileset [tileset], Objekt [id]:[/b][br][desc][br][i]Dieses Objekt ist animiert[/i]',
                5: 'Objekt [id]',
                },
            'OpenFromNameDlg': {
                0: 'Level auswählen',
                },
            'Palette': {
                0: 'Malen auf Ebene:',
                1: '[b]Ebene 0:[/b][br]Diese Schicht wird hauptsächlich für versteckte Höhlen verwendet, kann aber auch zum Überlagern von teilen verwendet werden, um Effekte zu erzeugen. Der Taschenlampen-Effekt tritt auf, wenn Mario hinter einer Wand auf Ebene 0 geht und die Zone diese aktiviert hat.[br][b]Hinweis:[/b] Um Objekte auf anderen Ebenen auf diese Ebene zu schalten, markiere sie und klicke dann auf diese Schaltfläche, während du die Taste [i]Alt[/i] gedrückt wird.',
                2: '[b]Ebene 1:[/b][br]Alle oder die meisten deiner Objekte auf Normalniveau sollten auf dieser Ebene platziert werden. Dies ist die einzige Ebene, in der Kachelwechselwirkungen (Solide, Schrägen, etc.) funktionieren.[br][b]Hinweis:[/b] Um Objekte auf anderen Ebenen auf diese Ebene zu schalten, markiere sie und klicke dann auf diese Schaltfläche, während die Taste [i]Alt[/i] gedrückt wird.',
                3: '[b]Ebene 2:[/b][br]Hintergrund-/Wandtiles (z.B. in den versteckten Höhlen) sollten auf dieser Ebene platziert werden. Tiles auf Layer 2 haben keinen Einfluss auf Kollisionen.[br][b]Hinweis:[/b] Um Objekte auf anderen Ebenen auf diese Ebene zu schalten, markiere sie und klicke dann auf diese Schaltfläche, während die Taste [i]Alt[/i] gedrückt wird.',
                4: 'Ansicht:',
                5: 'Suche:',
                6: 'Standardeigenschaften festlegen',
                7: 'Standardeigenschaften',
                8: 'Eingänge, die sich derzeit in diesem Bereich befinden:[br](Doppelklicke auf einen, um sofort zu ihm zu gelangen)',
                9: 'Die Pfadknoten, die sich derzeit in diesem Bereich befinden:[br](Doppelklicken auf einen, um sofort zu ihm zu springen)[br]Um einen Pfad zu löschen, entfernen alle seine Knoten einzeln.[br]Um neue Pfade hinzuzufügen, drücke die Schaltfläche unten und klicke mit der rechten Maustaste.',
                10: 'Abwählen (dann Rechtsklick für neuen Pfad)',
                11: 'Sprites, die sich derzeit in diesem Bereich befinden:[br](Doppelklicke auf eine, um sofort zu ihr zu springen)',
                12: 'Orte, die sich derzeit in diesem Bereich befinden:[br](Doppelklicke auf einen, um sofort zu ihm zu gelangen)',
                13: 'Objekte',
                14: 'Sprites',
                15: 'Eingänge',
                16: 'Standorte',
                17: 'Pfade',
                18: 'Events',
                19: 'Stempel',
                20: 'Ereigniszustände beim Start des Levels:[br](Klicke auf einen, um eine Notiz hinzuzufügen)',
                21: 'Hinweis:',
                22: 'Zustand',
                23: 'Notizen',
                24: 'Event [id]',
                25: 'Hinzufügen',
                26: 'Aktuell',
                27: 'Verfügbare Stempel:',
                28: 'Hinzufügen',
                29: 'Entfernen',
                30: 'Werkzeuge',
                31: 'Öffne Set...',
                32: 'Speichern unter...',
                33: 'Kommentare',
                34: 'Kommentare, die sich derzeit in diesem Bereich befinden:[br](Doppelklicken auf einen, um sofort zu ihm zu gelangen)',
                35: 'Name:',
                36: 'Mopsie Pfad',
                37: 'Mopsie Pfadknoten, die sich derzeit in diesem Bereich befinden:[br](Doppelklicke auf einen, um sofort zu ihm zu springen)',
                },
            'PathDataEditor': {
                0: 'Schleifen:',
                1: 'Schleifen:[/b][br]Alles, was diesem Pfad folgt, wartet auf irgendeine Verzögerung, die am letzten Knoten eingestellt wurde, und fährt dann geradlinig zum ersten Knoten zurück und fährt fort.',
                2: 'Geschwindigkeit:',
                3: '[b]Geschwindigkeit:[/b][br]Unbekannte Einheit. Vergnüge dich und berichte über deine Ergebnisse!',
                4: 'Beschleunigen:',
                5: 'Beschleunigung:[/b][br]Unbekannte Einheit. Vergnüge dich und melde deine Ergebnisse!',
                6: 'Delay:',
                7: '[b]Verzögerung:[/b][br]Zeitspanne, die bis zum Stoppen hier (an diesem Knoten) vergeht, bevor zum nächsten Knoten übergegangen wird. Die Einheit ist 1/60 einer Sekunde (60 für 1 Sekunde).',
                8: '[b]Pfad [id][/b]',
                9: '[b]Knoten [id][/b]',
                10: 'Modifizieren der Eigenschaften des ausgewählten Pfadknotens',
                11: 'Unbekannt 0x01:',
                12: '[b]Unbekannt 0x01:[/b][br]Keine Ahnung, was das ist',
                13: 'Modifizieren der Eigenschaften des ausgewählten Mopsie-Pfadknotens',
                14: '[b]Mopsie-Pfadknoten [id][/b]',
                15: 'Aktion:',
                16: '[b]Aktion:[/b][br]Die Aktion, die Mopsie durchgeführt wird, wenn er sich auf diesem Knoten befindet',
                },
            'Paths': {
                0: '[b]Pfad [path][/b][br]Knoten [node]',
                1: 'Pfad [path], Knoten [node]',
                2: '[b]Mopsie Pfad[/b][br]Knoten [node]',
                3: 'Mopsie Pfad, Knoten [node]',
                4: 'Entschuldigung![br]Du kannst nur Mopsie-Pfadknoten in Bereich 1 malen.',
                },
            'PrefsDlg': {
                0: 'Miyamoto! Präferenzen',
                1: 'Allgemeines',
                2: 'Symbolleiste',
                3: 'Designs',
                4: '[b]Miyamoto! Präferenzen[/b][br]Gestalte Miyamoto! durch Ändern dieser Einstellungen.[br]Verwenden die folgenden Registerkarten, um noch mehr Einstellungen anzuzeigen.[br]Miyamoto! muss neu gestartet werden, bevor bestimmte Änderungen wirksam werden können.',
                5: '[b]Toolbar Präferenzen[/b][br]Wähle Menüpunkte aus, die in der Symbolleiste erscheinen sollen.[br]Miyamoto! muss neu gestartet werden, bevor die Symbolleiste aktualisiert werden kann.[br]',
                6: '[b]Miyamoto! Themes[/b][br]Wähle ein Design unten aus, um die Farben und Symbole der Anwendung zu ändern.[br]Miyamoto! muss neu gestartet werden, bevor das Design geändert werden kann.',
                7: 'Zeigt den Startbildschirm an:',
                8: None,
                9: 'Immer',
                10: 'Niemals',
                11: 'Menüformat:',
                12: 'Benutze das Farbband',
                13: 'Verwende die Menüleiste',
                14: 'Sprache:',
                15: 'Daten der letzten Dateien:',
                16: 'Alle löschen',
                17: 'Alle Daten der letzten Dateien löschen',
                18: 'Bist du sicher, dass alle Daten der letzten Dateien löschen möchtest? Dies [b]kann nicht[/b] rückgängig gemacht werden!',
                19: 'Aktueller Bereich',
                20: 'Zurücksetzen',
                21: 'Verfügbare Designs',
                22: 'Vorschau',
                23: 'Nicht standardisierte Fensterstile verwenden',
                24: '[b]Nicht standardisierte Fensterstile verwenden[/b][br]Wenn dies überprüfbar ist, gibt das ausgewählte Design einen anderen[br]window Style als den Standard an. In den meisten Fällen solltest du[br]dies aktiviert lassen. Deaktiviere dies, wenn dir[br]der Stil, den dieses Design verwendet, nicht gefällt.',
                25: 'Optionen',
                26: '[b][name][/b][br]By [creator][br][description]',
                27: 'Tilesets:',
                28: 'Standard Tileset Picker verwenden (empfohlen)',
                29: 'Verwende den alten Tileset Picker.',
                30: 'Möglicherweise musst du Miyamoto! neu starten, damit Änderungen wirksam werden.',
                31: 'Displaylinien, die die äußerste linke x-Position anzeigen, an der Eingänge sicher in der Zone platziert werden können.s',
                32: 'SZS Kompressionsstufe:',
                33: '0: Am schnellsten',
                34: '1',
                35: '2',
                36: '3',
                37: '4',
                38: '5',
                39: '6',
                40: '7',
                41: '8',
                42: '9: Am besten',
                },
            'QuickPaint': {
                1: "WOAH! Aufgepasst!",
                2: "Uh oh, es sieht so aus, als gäbe es in dieser Voreinstellung Objekte, die nicht existieren. Bitte entfernen diese sofort.![br]Wenn du das Schnellmalwerkzeug Werkzeug mit nicht existierenden Objekten verwendest, wird das Spiel wahrscheinlich beim Laden des Levels ABSTÜRZEN!",
                3: "Schnellmalwerkzeug",
                4: "Malen",
                5: "Löschen",
                6: "Voreinstellungen:",
                7: "Speichern",
                8: "Hinzufügen",
                9: "Entfernen",
                10: "Dialog",
                11: "Bist du sicher, dass du diese Voreinstellung löschen möchtest? Du kannst diese Aktion nicht rückgängig machen.",
                12: "Diese Voreinstellung überschreiben?",
                13: "Name der Voreinstellung"
                },
            'Ribbon': {
                0: '&Startseite',
                1: '&Aktionen',
                2: '&Ansicht',
                3: '&Spiel',
                4: None, # REMOVED: 'H&elp'
                5: 'Zwischenablage',
                6: 'Einfrieren',
                7: 'Level Information',
                8: 'Bereich',
                9: 'Auswahl',
                10: 'Items',
                11: 'Level-Einstellungen',
                12: 'Bereiche',
                13: 'Tilesets',
                14: 'Layers',
                15: 'Sichtbarkeit',
                16: 'Zoom',
                17: 'Docks',
                18: 'Miyamoto!',
                19: 'Bibliotheken',
                20: '([shortcut]) [description]',
                21: ', ',
                22: '(None) [description]',
                23: '&Datei',
                },
            'ScrShtDlg': {
                0: 'Wähle eine Screenshot-Quelle aus',
                1: 'Aktueller Bildschirm',
                2: 'Alle Zonen',
                3: 'Zone [zone]',
                },
            'ShftItmDlg': {
                0: 'Positionen verschieben',
                1: 'Objekte verschieben um:',
                2: 'Gib einen Offset in Pixel ein - jeder Block entspricht 16 Pixel breit/hoch. Bedenke, dass normale Objekte nur auf 16x16 Grenzen platziert werden können. Wenn der von dir eingegebene Offset also kein Vielfaches von 16 ist, werden sie nicht korrekt verschoben.',
                3: 'X:',
                4: 'Y:',
                5: 'Warnung',
                6: 'Du versuchst, Objekte um einen Offset zu verschieben, der kein Vielfaches von 16 ist. Es wird funktionieren, aber die Objekte werden nicht in der Lage sein, genau die gleiche Menge wie die Sprites zu bewegen. Bist du sicher, dass du das tun willst?',
                },
            'Splash': {
                0: '[current] (Stage [stage])',
                1: 'Laden von Ebenen...',
                2: 'Laden von Level-Daten...',
                3: 'Laden von Tilesets...',
                4: 'Laden von Objekten...',
                5: 'Vorbereitung des Editors...',
                },
            'SpriteDataEditor': {
                0: 'Modifizieren der ausgewählten Sprite-Eigenschaften',
                1: '[b][name][/b]: [note]',
                2: '[b]Sprite Notizen:[/b] [notes]',
                3: 'Modifizieren der Rohdaten:',
                4: 'Notizen',
                5: '[b]Unbekannter Sprite ([id])[/b]',
                6: '[b]Sprite [id]:[br][name][/b]',
                7: 'Objektdateien',
                8: '[b]Dieses Sprite verwendet:[/b][br][list]',
                },
            'Sprites': {
                0: '[b]Sprite [type]:[/b][br][name]',
                1: '[name] (at [x], [y]',
                2: ', ausgelöst durch das Ereignis [event]',
                3: ', ausgelöst durch die Ereignisse [event1]+[event2]+[event3]+[event4]',
                4: ', ausgelöst durch das Ereignis [event1], [event2], [event3], oder [event4]',
                5: ', aktiviert das Ereignis [event]',
                6: ', aktiviert die Ereignisse [event1] - [event2]',
                7: ', aktiviert das Ereignis [event1], [event2], [event3], oder [event4]',
                8: ', Sternenmünze [num]',
                9: ', Sternenmünze 1',
                10: ', Coin/Set ID [id]',
                11: ', Bewegung/Münz-ID [id]',
                12: ', Bewegungs-ID [id]',
                13: ', Rotations-ID [id]',
                14: ', Orts-ID [id]',
                15: ')',
                16: 'Suchergebnisse',
                17: 'Keine Sprites gefunden',
                18: '[id]: [name]',
                19: 'Suche',
                },
            'Statusbar': {
                0: '- 1 Objekt ausgewählt',
                1: '- 1 Sprite ausgewählt',
                2: '- 1 Eingang ausgewählt',
                3: '- 1 Orte ausgewählt',
                4: '- 1 Pfadknoten ausgewählt',
                5: '- [x] Objekte ausgewählt',
                6: '- [x] Sprites ausgewählt',
                7: '- [x] Eingänge ausgewählt',
                8: '- [x] Orte ausgewählt',
                9: '- [x] Pfadknoten ausgewählt',
                10: '- [x] Items ausgewählt (',
                11: ', ',
                12: '1 Objekt',
                13: '[x] Objekte',
                14: '1 Sprite',
                15: '[x] Sprites',
                16: '1 Eingang',
                17: '[x] Eingänge',
                18: '1 Ort',
                19: '[x] Orte',
                20: '1 Pfadknoten',
                21: '[x] Pfadknoten',
                22: ')',
                23: '- Objekt unter der Maus: Größe [width]x[height] bei ([xpos], [ypos]) auf der Ebene [layer]; Typ [type] von Tileset [tileset]',
                24: '- Sprite unter der Maus: [name] bei [xpos], [ypos]',
                25: '- Eingang unter der Maus: [name] bei [xpos], [ypos] [dest]',
                26: '- Location unter der Maus: Location ID [id] bei [xpos], [ypos]; width [width], height [height]',
                27: '- Pfadknoten unter der Maus: Path [path], Node [node] bei [xpos], [ypos]',
                28: '([objx], [objy]) - ([sprx], [spry])',
                29: '- 1 Kommentar ausgewählt',
                30: '- [x] Kommentare ausgewählt',
                31: '1 Kommentar',
                32: '[x] Kommentare',
                33: '- Kommentar unter der Maus: [xpos], [ypos]; "[text]"',
                34: '- 1 Mopsie-Pfadknoten ausgewählt',
                35: '- [x] Mopsie-Pfadknoten ausgewählt',
                36: '1 Mopsie-Pfadknoten',
                37: '[x] Mopsie-Pfadknoten',
                38: '- Pfadknoten unter der Maus: Pfadknoten [node] bei [xpos], [ypos]',
                },
            'Themes': {
                0: 'Klassisch',
                1: 'Treeki, Tempus',
                2: 'Das Standard-Miyamoto!-Design.',
                3: '[i](Unbekannt)[/i]',
                4: '[i]Keine Beschreibung[/i]',
                },
            'Updates': {
                0: 'Nach Updates suchen',
                1: 'Fehler bei der Suche nach Updates.',
                2: 'Es sind keine Updates verfügbar.',
                3: 'Ein Update ist verfügbar: [name][br][info]',
                4: 'Jetzt herunterladen',
                5: 'Bitte warte, das Update wird gerade heruntergeladen...',
                6: 'Neustart zum Abschluss der Aktualisierung!',
                },
            'WindowTitle': {
                0: 'Ohne Titel',
                },
            'ZonesDlg': {
                0: 'Bereiche',
                1: (
                    'Überwelt',
                    'Untergrund',
                    'Unterwasser',
                    'Lava/Vulkan (rötlich)',
                    'Wüste',
                    'Strand*',
                    'Wald*',
                    'Schnee Überwelt*',
                    'Himmel/Bonus*',
                    'Berge*',
                    'Turm',
                    'Schloss',
                    'Geisterhaus',
                    'Flusshöhle',
                    'Geisterhaus Ausgang',
                    'Unterwasser-Höhle',
                    'Wüstenhöhle',
                    'Eishöhle*',
                    'Lava/Vulkan',
                    'Endkampf',
                    'Welt 8 Burg',
                    'Welt 8 Verdammnis*',
                    'Beleuchteter Turm',
                    ),
                2: (
                    'Normal/Überwelt',
                    'Untergrund',
                    'Unterwasser',
                    'Lava/Vulkan',
                    ),
                3: 'Bereich [num]',
                4: 'Neu',
                5: 'Löschen',
                6: 'Warnung',
                7: 'Du versuchst, mehr als 15 Zonen zu einem Level hinzuzufügen - denk daran, dass ohne die richtige Lösung für das Spiel, dies deinen Level zum [b]Absturz[/b] bringt oder andere seltsame Probleme hat![br][br][br]Bist du sicher, dass du das tun willst?',
                8: 'Abmessungen',
                9: 'X-Position:',
                10: '[b]X-Position:[/b][br]Setzt die X-Position der linken oberen Ecke.',
                11: 'Y-Position:',
                12: '[b]Y-Position:[/b][br]Setzt die Y-Position der linken oberen Ecke.',
                13: 'X-Größe:',
                14: '[b]X-Größe:[/b][br]Legt die Breite der Zone fest',
                15: 'Y-Größe:',
                16: '[b]Y-Größe:[/b][br]Legt die Höhe der Zone fest',
                17: 'Voreinstellung:',
                18: '[b]Voreinstellung:[/b][br]Die Zahl vor jedem Eintrag gibt an, welche Zoomstufe bei jeder Größe am besten funktioniert.',
                19: 'Rendern und Kamera',
                20: 'Zonenthema:',
                21: '[b]Zonenthema:[/b][br]Völlig nutzlos, da es automatisch vom Hintergrund bestimmt wird. Ändert die Art und Weise, wie Modelle und Teile des Hintergrunds wiedergegeben werden (für Unschärfe, Dunkelheit, Lavaeffekte usw.). Themen mit * daneben werden im Spiel verwendet, sehen aber genauso aus wie das Thema Überwelt.',
                22: 'Geländebeleuchtung:',
                23: '[b]Geländebeleuchtung:[/b][br]Ändert die Art und Weise, wie das Terrain dargestellt wird. Es beeinflusst auch die Teile des Hintergrunds, die das Zonenthema nicht verändert.',
                24: 'Normal',
                25: '[b]Sichtbarkeit - Normal:[/b][br]Setzt den Sichtbarkeitsmodus auf normal.',
                26: 'Ebene 0 Scheinwerferlicht',
                27: '[b]Sichtbarkeit - Ebene 0 Scheinwerferlicht:[/b][br]Sets the visibility mode to spotlight. In Spotlight mode,[br]moving behind layer 0 objects enables a spotlight that[br]follows Mario around.',
                28: 'Volle Dunkelheit',
                29: '[b]Sichtbarkeit - Volle Dunkelheit:[/b][br]Stellt den Sichtbarkeitsmodus auf volle Dunkelheit ein. Im Volldunkelmodus ist[br]der Bildschirm komplett schwarz und die Sichtbarkeit wird nur durch den verfügbaren Scheinwerfereffekt gewährleistet. Sterne und einige Sprites[br]können die Standard-Sichtbarkeit verbessern.',
                30: 'X Verfolgung:',
                31: '[b]X Verfolgung:[/b][br]Ermöglicht es der Kamera, Mario über die X-Achse zu verfolgen.[br]Wenn du diese Option ausschaltest, wird der Bildschirm horizontal in der Ansicht zentriert, wodurch ein stationärer Kameramodus entsteht.',
                32: 'Y Verfolgung:',
                33: '[b]Y Verfolgung:[/b][br]Ermöglicht es der Kamera, Mario über die Y-Achse zu verfolgen.[br]Wenn du diese Option ausschaltest, wird der Bildschirm vertikal in der Ansicht zentriert, wodurch sehr vertikal begrenzte Stufen entstehen.',
                34: 'Zoom-Stufe:',
                35: '[b]Zoom-Stufe:[/b][br]Ändert die Zoomfunktion der Kamera[br] - Negative Werte: Zoom In[br] - Positive Werte: Verkleinern[br][br][br]Zoom Level 4 ist ziemlich unruhig.',
                36: 'Bias:',
                37: '[b]Bias:[/b][br]Stellt die Bildschirmvorspannung auf den linken Rand beim Laden ein, wodurch ein anfängliches Zurückrollen verhindert wird.[br]Nützlich für gepatchte Ebenen.[br]Hinweis: Nicht alle Zoom/Modus-Kombinationen unterstützen Vorspannung.',
                38: (
                    'Left to Right',
                    'Right to Left',
                    'Top to Bottom',
                    'Bottom to Top',
                    ),
                39: 'Kamera-Tracking:',
                40: '[b]Kamera-Tracking:[/b][br]Diese Einstellung ändert die Kameraführung im Mehrspieler-Modus.[br]Wenn sich die Kamera nicht bewegt, wähle von links nach rechts.[br]Wenn du dir unsicher bist, wähle von links nach rechts.',
                41: (
                    'Versteckt',
                    'Oben',
                    ),
                42: '[b]Sichtbarkeit:[/b][br]Ausblendet - Mario ist ausgeblendet, wenn er sich hinter Objekten auf Ebene 0 ist[br]Oben - Mario wird immer über Ebene 0 angezeigt.[br][br][br]Hinweis: Andere Elemente hinter Ebene 0 als Mario sind nie sichtbar.',
                43: (
                    'Klein',
                    'Groß',
                    'Vollbild',
                    ),
                44: '[b]Sichtbarkeit:[/b][br]Klein - Ein kleiner, zentrierter Scheinwerfer ermöglicht die Sichtbarkeit durch die Ebene 0.[br]Groß - Ein großer, zentrierter Scheinwerfer ermöglicht die Sichtbarkeit durch die Ebene 0[br]Vollbild - der gesamte Bildschirm wird angezeigt, wenn Mario hinter die Ebene 0 tritt.',
                45: ('Großer Nebelscheinwerfert',
                     'Lichtstrahl',
                     'Großes Fokuslicht',
                     'Kleiner Nebelscheinwerfer',
                     'Licht mit kleinem Fokus',
                     'Absolut Schwarz',
                     ),
                46: '[b]Sichtbarkeit:[/b][br]Großes Nebelscheinwerfer - Eine große, organische Lichtquelle umgibt Mario[br]Lichtstrahl - Mario ist in der Lage, einen konischen Lichtstrahl durch den Einsatz der Wiimote[br]Großes Fokuslicht zu richten - Ein großer Scheinwerfer, der sich je nach Spielerbewegung ändert[br]Kleiner Nebelscheinwerfer - Eine kleine, organische Lichtquelle umgibt Mario[br]Kleines Fokuslicht - Ein kleiner Scheinwerfer, der sich je nach Spielerbewegung ändert[br]Absolutes Schwarz - Die Sicht wird nur von Feuerbällen, Sternen und bestimmten Sprites gewährleistet.',
                47: 'Grenzen',
                48: 'Obere Grenzen:',
                49: '[b]Obere Grenzen:[/b][br] - Positive Werte: Einfacheres Scrollen nach oben (110 ist zentriert)[br] - Negative Werte: Schwierigeres Scrollen nach oben (30 ist der obere Rand des Bildschirms)[br][br][br]Werte über 240 können beim Scrollen des Bildschirms zum sofortigen Tod führen.',
                50: 'Untergrenzen:',
                51: '[b]Untergrenzen:[/b][br] - Positive Werte: Schwierigeres Scrollen nach unten (65 ist der untere Rand des Bildschirms)[br] - Negative Werte: Leichteres Scrollen nach unten (95 ist zentriert)[br][br][br]Werte größer als 100 verhindern, dass die Szene scrollt, bis Mario den Bildschirm verlässt.',
                52: 'Audio',
                53: 'Hintergrundmusik:',
                54: '[b]Hintergrundmusik:[/b][br]Ändert die Hintergrundmusik',
                55: 'Klangmodulation:',
                56: '[b]Klangmodulation:[/b][br]Ändert die Soundeffekt-Modulation',
                57: (
                    'Normal',
                    'Wand-Echo',
                    'Raum-Echo',
                    'Doppeltes Echo',
                    'Höhlen-Echo',
                    'Unterwasser-Echo',
                    'Dreifaches Echo',
                    'Hochfrequentes Echo',
                    'Kleines Echo',
                    'Flach',
                    'Stumpf',
                    'Hohles Echo',
                    'Rich',
                    'Dreifach unter Wasser',
                    'Ring-Echo',
                    ),
                58: 'Boss-Flagge:',
                59: '[b]Boss-Flagge:[/b][br]Stellt die Bosse ein, um eine korrekte Musikumschaltung durch Sprites zu ermöglichen.',
                60: '(Keine)',
                61: 'Fehler',
                62: 'Die Zoomstufe -2 unterstützt keine Bias-Modi.',
                63: 'Die Zoomstufe -1 unterstützt keine Bias-Modi.',
                64: 'Die Zoomstufe -1 wird bei diesen Tracking-Modi nicht unterstützt. Auf Zoomstufe 0 einstellen.',
                65: 'Der Zoom-Modus 4 kann mit diesen Einstellungen gestört sein.',
                66: 'Kein Tracking-Modus ist durchgehend fehlerhaft und unterstützt keine Bias.',
                67: 'Kein Tracking-Modus ist durchgehend fehlerhaft.',
                68: 'Hintergrundmusik-ID:',
                69: '[b]Hintergrundmusik-ID:[/b][br]Diese erweiterte Option ermöglicht das Laden benutzerdefinierter Musiktitel, wenn die richtigen ASM-Hacks vorhanden sind.',
                70: 'Obergrenze 2:',
                71: '[b]Obergrenze 2:[/b][br]Unbekannte Unterschiede zu den Hauptobergrenzen.',
                72: 'Untergrenzen 2:',
                73: '[b]Untergrenzen 2:[/b][br]Unbekannte Unterschiede zu den wesentlichen Untergrenzen.',
                74: 'Vertikales Scrollen aktivieren?',
                75: '[b]Vertikales Scrollen aktivieren?:[/b][br]Die Ebene kann nicht vertikal scrollen, wenn dies nicht aktiviert ist Scheint immer aktiviert zu sein..',
                76: 'Typ:',
                77: '[b]Typ:[/b][br]Legt den Typ für diese Zone fest.',
                78: 'Einrasten auf 8x8 Raster',
                79: 'Einrasten auf 16x16 Raster',
                },
            'Zones': {
                0: 'Bereich [num]',
                },
            }


    def InitFromXML(self, name):
        """
        Parses the translation XML
        """
        if name in ('', None, 'None'): return
        name = str(name)
        MaxVer = 1.0

        # Parse the file (errors are handled by __init__())
        path = 'miyamotodata/translations/' + name + '/main.xml'
        tree = etree.parse(path)
        root = tree.getroot()

        # Add attributes
        # Name
        if 'name' not in root.attrib: raise Exception
        self.name = root.attrib['name']
        # Version
        if 'version' not in root.attrib: raise Exception
        self.version = float(root.attrib['version'])
        if self.version > MaxVer: raise Exception
        # Translator
        if 'translator' not in root.attrib: raise Exception
        self.translator = root.attrib['translator']

        # Parse the nodes
        files = {}
        strings = False
        addpath = 'miyamotodata/translations/' + name + '/'
        for node in root:
            if node.tag.lower() == 'file':
                # It's a file node
                name = node.attrib['name']
                path = addpath + node.attrib['path']
                files[name] = path
            elif node.tag.lower() == 'strings':
                # It's a strings node
                strings = addpath + node.attrib['path']

        # Get rid of the XML stuff
        del tree, root

        # Overwrite self.files with files
        for index in files: self.files[index] = files[index]



        # Check for a strings node
        if not strings: raise Exception

        # Parse the strings
        tree = etree.parse(strings)
        root = tree.getroot()

        # Parse the nodes
        strings = {}
        for section in root:
            # Get a section
            if section.tag.lower() != 'section': continue
            id = section.attrib['id']
            sectionStrings = {}

            # Get the strings/stringlists in this section
            for string in section:
                if not hasattr(string, 'attrib'): continue
                strValue = None
                if string.tag.lower() == 'string':
                    # String node; this is easy
                    strValue = string[0]
                elif string.tag.lower() == 'stringlist':
                    # Not as easy, but not hard
                    strValue = []
                    for entry in string:
                        if entry.tag.lower() == 'entry':
                            strValue.append(entry[0])
                    strValue = tuple(strValue)

                # Add this string to sectionStrings
                idB = int(string.attrib['id'])
                if strValue is not None: sectionStrings[idB] = strValue

            # Add it to strings
            strings[id] = sectionStrings

        # Overwrite self.strings with strings
        for index in strings:
            if index not in self.strings: self.strings[index] = {}
            for index2 in strings[index]:
                self.strings[index][index2] = strings[index][index2]


    def string(*args):
        """
        Usage: string(section, numcode, replacementDummy, replacement, replacementDummy2, replacement2, etc.)
        """
        self = args[0]

        # If there are errors when the string is found, return an error report instead
        try: return self.string_(args[1:])
        except Exception as e:
            text = '\nMiyamotoTranslation.string() ERROR: ' + str(args[1]) + '; ' + str(args[2]) + '; ' + repr(e) + '\n'
            # do 3 things with the text - print it, save it to MiyamotoErrors.txt, return it
            print(text)
            if not os.path.isfile('MiyamotoErrors.txt'):
                f = open('MiyamotoErrors.txt', 'w')
            else:
                f = open('MiyamotoErrors.txt', 'a')
            f.write(text)
            f.close(); del f
            return text

    def string_(*args):
        """
        Gets a string from the translation and returns it
        """
        # Get self and remove it from args
        self = args[0]
        args = args[1]

        # Get the string
        astring = self.strings[args[0]][args[1]]

        # Perform any replacements
        i = 2
        while i < len(args):

            # Get the old string
            old = str(args[i])

            # Get the new string
            new = str(args[i+1])

            # Replace
            astring = astring.replace(old, new)
            i += 2

        # Do some automatic replacements
        replace = {
            '[br]': '<br>',
            '[b]': '<b>',
            '[/b]': '</b>',
            '[i]': '<i>',
            '[/i]': '</i>',
            '[a': '<a',
            '"]': '">', # workaround
            '[/a]': '</a>',
            '\\n': '\n',
            '//n': '\n',
            }
        for old in replace:
            astring = astring.replace(old, replace[old])

        # Return it
        return astring

    def stringList(self, section, numcode):
        """
        Returns a list of strings
        """
        try: return self.strings[section][numcode]
        except Exception: return ('MiyamotoTranslation.stringList() ERROR:', section, numcode)

    def path(self, key):
        """
        Returns the path to the file indicated by key
        """
        try: return self.files[key]
        except Exception:
            # (print, save, return) an error message
            text = 'MiyamotoTranslation.path() ERROR: ' + key
            print(text)
            F = open('MiyamotoErrors.txt', 'w')
            F.write(text)
            F.close()
            raise SystemExit

    def generateXML(self):
        """
        Generates a strings.xml and places it in the folder of miyamoto.py
        """

        # Sort self.strings
        sortedstrings = sorted(
            (
                [
                    key,
                    sorted(
                        self.strings[key].items(),
                        key=lambda entry: entry[0]),
                    ]
                for key in self.strings
                ),
            key=lambda entry: entry[0])

        # Create an XML
        root = etree.Element('strings')
        for sectionname, section in sortedstrings:
            sectionElem = etree.Element('section', {'id': sectionname})
            root.append(sectionElem)
            for stringid, string in section:
                if isinstance(string, tuple) or isinstance(string, list):
                    stringlistElem = etree.Element('stringlist', {'id': str(stringid)})
                    sectionElem.append(stringlistElem)
                    for entryname in string:
                        entryElem = etree.Element('entry')
                        entryElem.text = entryname
                        stringlistElem.append(entryElem)
                else:
                    stringElem = etree.Element('string', {'id': str(stringid)})
                    stringElem.text = string
                    sectionElem.append(stringElem)

        tree = etree.ElementTree(root)
        tree.write('strings.xml', encoding='utf-8')