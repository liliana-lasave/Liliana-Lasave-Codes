-- Punkt 1: Eine Zeile in der Tabelle qualifikationen hinzufügen (eine neue Qualifikation)
USE uebungsdatenbank;
INSERT INTO qualifikationen (bezeichnung, kuerzel, kategorie)
VALUES ('SQL', 'ITE', 'Informatik');

-- Punkt 2: Die Qualifikation Sys-Admin in die Tabelle qualifikationen einfügen
USE uebungsdatenbank;
INSERT INTO qualifikationen (bezeichnung, kuerzel, kategorie)
VALUES ('Sys-Admin', 'ADA', 'Support');

-- Punkt 3: 'Projektleitung' ohne Abkürzung und Kategorie einfügen
USE uebungsdatenbank;
INSERT INTO qualifikationen (bezeichnung, kuerzel, kategorie)
VALUES ('Projektleitung', NULL, NULL);

-- Punkt 4: Ändern der Werte in der Tabelle qualglobal
UPDATE qualglobal
SET bezeichnung = 'Second Level Helpdesk'
WHERE qid = 2 AND bezeichnung = 'Second Level Support';

UPDATE qualglobal
SET bezeichnung = 'First Level Helpdesk', kuerzel = 'FLH'
WHERE qid = 3 AND bezeichnung = 'First Level Support' AND kuerzel = 'FLS';

-- Prüfabfrage: Überprüfen, ob die Werte aktualisiert wurden
SELECT qid, bezeichnung, kuerzel
FROM qualglobal
WHERE qid IN (2, 3);

-- Punkt 5: Werte in der Spalte kuerzel aktualisieren
UPDATE qualglobal
SET kuerzel = 'DBE'
WHERE kuerzel = 'DAT';

-- Punkt 6: Löschen der Zeile mit qid = 2 aus der Tabelle qualglobalarchiv
DELETE FROM qualglobalarchiv
WHERE qid = 2;

-- Überprüfen, welche Zeilen noch in der Tabelle qualglobalarchiv vorhanden sind
SELECT * FROM qualglobalarchiv;

-- Punkt 7: Löschen der Zeilen mit qid 5, 6 und 7 aus der Tabelle qualglobalarchiv
DELETE FROM qualglobalarchiv
WHERE qid IN (5, 6, 7);

-- Überprüfen, welche Zeilen noch in der Tabelle qualglobalarchiv vorhanden sind
SELECT * FROM qualglobalarchiv;

-- Punkt 8: Löschen aller verbleibenden Zeilen aus der Tabelle qualglobalarchiv
DELETE FROM qualglobalarchiv;

-- Überprüfen, ob die Tabelle qualglobalarchiv jetzt leer ist
SELECT * FROM qualglobalarchiv;









