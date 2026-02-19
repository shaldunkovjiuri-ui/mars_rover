Bracket_sequence.py
--------------------
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
Dieses Modul enthält einen Algorithmus zur Validierung von Klammerausdrücken.
Das Programm prüft, ob eine Zeichenfolge korrekt ausgeglichen ist, indem es eine „Stack“-Datenstruktur verwendet, um öffnende und schließende Klammern der Typen (), [] und {} abzugleichen.

Implementierte Funktionen
is_correct_bracket_seq(seq: str) -> bool:

Akzeptiert einen String aus Klammern.

Verwendet eine Liste stek, um geöffnete Klammern zu speichern.

Nutzt das Dictionary word_def, um Paare zu vergleichen.

Gibt True zurück, wenn die Sequenz korrekt geschlossen und verschachtelt ist, andernfalls False.


Defining_an_index_for_insertion.py
----------------------------------
Description
This program implements a modified binary search algorithm for sorted integer arrays. 
This specific version finds the index of the first (leftmost) occurrence of a target value or determines the insertion point to maintain order.

Implemented Logic
Data Input: Reads a sequence of numbers and a target value from the console.

Algorithm:

Utilizes the two-pointer technique (left and right).

Midpoint calculation: mid = (left + right) // 2.

If a match is found (nums[mid] == target), the search continues in the left half (right = mid - 1) to locate the earliest occurrence.

Output: Prints the index of the found element or the left index as the appropriate insertion point if the element is missing.
______________________________________________________________________________________________________________________________
Beschreibung
Dieses Programm implementiert einen modifizierten binären Suchalgorithmus für sortierte Ganzzahl-Arrays. 
Diese Version findet den Index des ersten (ganz linken) Vorkommens eines Zielwerts oder bestimmt die Einfügeposition, um die Sortierung beizubehalten.

Implementierte Logik
Dateneingabe: Liest eine Zahlenfolge und einen Zielwert (Target) ein.

Algorithmus:

Verwendet die Zwei-Zeiger-Methode (left und right).

Berechnung des Mittelpunkts: mid = (left + right) // 2.

Wenn eine Übereinstimmung gefunden wird (nums[mid] == target), wird die Suche in der linken Hälfte fortgesetzt (right = mid - 1), um das am weitesten links stehende Element zu finden.

Ergebnis: Gibt den Index des Elements zurück oder den left-Index als Einfügepunkt, falls der Wert nicht existiert.


Delivery_service.py
-------------------
Description
This module solves a logistics optimization problem: calculating the minimum number of transport platforms required to move robots. Each platform has a weight limit and can carry a maximum of two robots at a time.

Implemented Methods
min_platforms(weights, limit):

Sorting: Pre-sorts robot weights to enable effective pairing.

Two-Pointer Technique: Attempts to pair the heaviest robot with the lightest one if their combined weight is within the limit.

Logic: If the combined weight exceeds the limit, the heaviest robot is assigned a platform alone.
____________________________________________________________________________________________________
Beschreibung
Dieses Modul löst ein Optimierungsproblem in der Logistik: die Berechnung der minimalen Anzahl an Transportplattformen, die für den Transport von Robotern erforderlich sind. Jede Plattform hat eine Tragfähigkeitsbeschränkung und kann maximal zwei Roboter gleichzeitig aufnehmen.

Implementierte Methoden
min_platforms(weights, limit):

Sortierung: Sortiert die Gewichte der Roboter vorab für eine effiziente Verarbeitung.

Zwei-Zeiger-Methode: Versucht, den schwersten Roboter mit dem leichtesten zu kombinieren, sofern das Gesamtgewicht das limit nicht überschreitet.

Logik: Wenn das Paar zu schwer ist, erhält der schwerste Roboter eine eigene Plattform.


Extra_task.py
-------------
Description
This module provides a solution for removing a node from a singly linked list at a specified index. The algorithm correctly handles removing the head node, middle nodes, and prevents errors when the index is out of bounds.

Implemented Components
Node Class: Represents a list element containing a value and a reference to the next_item.

solution(node, idx) function:

Head Removal (idx == 0): Returns the second node as the new head of the list.

Middle/Tail Removal: Traverses to the node preceding the target index and updates its next_item reference to bypass the deleted node.

Robustness: If the index is out of range, the list remains unchanged.
________________________________________________________________________________________________________________________________
Beschreibung
Dieses Modul enthält eine Lösung zum Entfernen eines Knotens aus einer einfach verketteten Liste an einem bestimmten Index. Der Algorithmus verarbeitet das Löschen des Kopfknotens sowie von Knoten in der Mitte und verhindert Fehler bei Indizes außerhalb des gültigen Bereichs.

Implementierte Komponenten
Klasse Node: Beschreibt ein Listenelement mit einem Wert (value) und einem Verweis auf das nächste Element (next_item).

Funktion solution(node, idx):

Entfernen des Kopfes (idx == 0): Gibt den zweiten Knoten als neuen Kopf der Liste zurück.

Entfernen in der Mitte/am Ende: Navigiert zum Knoten vor dem Zielindex und aktualisiert dessen Verweis next_item, um den Zielknoten zu überspringen.

Sicherheit: Wenn der Index außerhalb der Listenlänge liegt, bleibt die Liste unverändert.


Removing_duplicates.py
--------------------------
Description
This module implements an efficient in-place algorithm to remove duplicates from a sorted array. The algorithm shifts unique elements to the beginning of the array while maintaining their relative order and pads the remaining space with underscores.

Implemented Logic
Two-Pointer Technique:

read_index: Iterates through the array to identify new unique values.

write_index: Tracks the position where the next unique value should be stored.

Processing: If the current element differs from the previous one, it is written to the write_index position, and the write pointer is incremented.

Output: The final list displays unique elements followed by '_' characters to match the original array length.
______________________________________________________________________________________________________________________
Beschreibung
Dieses Modul implementiert einen effizienten In-place-Algorithmus zum Entfernen von Duplikaten aus einem sortierten Array. Der Algorithmus verschiebt eindeutige Elemente an den Anfang des Arrays, behält deren relative Reihenfolge bei und füllt den verbleibenden Platz mit Unterstrichen auf.

Implementierte Logik
Zwei-Zeiger-Methode:

read_index: Durchläuft das Array, um neue eindeutige Werte zu identifizieren.

write_index: Markiert die Position, an der der nächste eindeutige Wert gespeichert wird.

Verarbeitung: Wenn sich das aktuelle Element vom vorherigen unterscheidet, wird es an der Position write_index geschrieben und der Schreibzeiger wird erhöht.

Ausgabe: Die Ergebnisliste enthält die eindeutigen Elemente, ergänzt durch '_' Zeichen, um die ursprüngliche Länge beizubehalten.


The_number_of_numbers_less_than_a_given_number.py
-------------------------------------------------
Description
This module analyzes numerical data (e.g., radiation levels).
The algorithm calculates the number of elements in the list that are strictly smaller than each current element.
This helps determine the relative rank of each measurement within the dataset.
Implemented Methods
nukle(data: list[int]) -> list[int]:
Input: A list of integers.
Logic: Uses a nested loop to compare each number against every other element in the list.
Complexity: The algorithm has a time complexity of O(n^2), where n is the number of elements.
Output: A list of integers representing the count of elements smaller than the current one.
____________________________________________________________________________________________
Beschreibung
Dieses Modul dient der Analyse numerischer Daten (z. B. Strahlungswerte). Der Algorithmus berechnet für jedes Element einer Liste die Anzahl der anderen Elemente, die strikt kleiner sind. Dies ermöglicht die Bestimmung des relativen Ranges jeder Messung im Datensatz.
Implementierte Methodennukle(data: list[int]) -> list[int]:
Eingabe: Eine Liste von Ganzzahlen.
Logik: Verwendet eine verschachtelte Schleife, um jede Zahl mit allen anderen Elementen der Liste zu vergleichen.
Komplexität: Der Algorithmus hat eine Zeitkomplexität von O(n^2), wobei n die Anzahl der Elemente ist.
Ausgabe: Eine Liste von Ganzzahlen, die die Anzahl der jeweils kleineren Elemente darstellen.


