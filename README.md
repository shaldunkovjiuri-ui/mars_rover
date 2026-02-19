Bracket_sequence.py

Description
This module provides an algorithm to validate bracket sequences. It determines if a string is a balanced bracket sequence using a "stack" data structure to match opening and closing symbols of various types: (), [], and {}.

Implemented Functions
is_correct_bracket_seq(seq: str) -> bool:

Accepts a string of brackets as input.

Utilizes a list stek to keep track of open brackets.

Uses the word_def dictionary to validate matching pairs.

Returns True if the sequence is balanced and correctly nested; otherwise, returns False.
_________________________________________________________________________________________
Beschreibung
Dieses Modul enthält einen Algorithmus zur Validierung von Klammerausdrücken. Das Programm prüft, ob eine Zeichenfolge korrekt ausgeglichen ist, indem es eine „Stack“-Datenstruktur verwendet, um öffnende und schließende Klammern der Typen (), [] und {} abzugleichen.

Implementierte Funktionen
is_correct_bracket_seq(seq: str) -> bool:

Akzeptiert einen String aus Klammern.

Verwendet eine Liste stek, um geöffnete Klammern zu speichern.

Nutzt das Dictionary word_def, um Paare zu vergleichen.

Gibt True zurück, wenn die Sequenz korrekt geschlossen und verschachtelt ist, andernfalls False.
