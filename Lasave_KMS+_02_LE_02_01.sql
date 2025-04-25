-- SQL-Abfragen – KMS+/02/LE_02-01

-- 1. Eintritts- und Austrittsdatum der Mitarbeiter:innen
SELECT mitarbeiterid, name, vorname, eintrittsdatum, austrittsdatum
FROM mitarbeiter;


-- 2. Austrittsgrund hinzufügen
SELECT mitarbeiterid, name, vorname, eintrittsdatum, austrittsdatum, austrittsgrund
FROM mitarbeiter
WHERE austrittsdatum is not null;


-- 3. Alle Daten der Mitarbeiter:innen anzeigen
SELECT * FROM mitarbeiter;


-- 4. Mitarbeiter:innen der Abteilung Vertrieb
SELECT * FROM mitarbeiter
WHERE abteilung = 'Vertrieb';


-- 5. Mitarbeiter:innen mit 30 genommenen Urlaubstagen
SELECT * FROM mitarbeiter
WHERE urlaubgenommen >= 30;


-- 6. Mitarbeiter:innen mit mindestens einem Kind
SELECT * FROM mitarbeiter
WHERE anzahlkinder >= 1;


-- 7. Zwischen dem 01.01.1990 und dem 01.01.2000 eingestellte Mitarbeiter:innen
SELECT * FROM mitarbeiter
WHERE eintrittsdatum BETWEEN '1990-01-01' AND '2000-01-01';


-- 8. Weibliche Mitarbeiter:innen in der Abteilung Vertrieb
SELECT * FROM mitarbeiter
WHERE geschlecht = 'w' AND abteilung = 'Vertrieb';


-- 9. Mitarbeiter:innen mit bestimmten Krankenkassen
SELECT * FROM mitarbeiter
WHERE krankenversicherung = 'MH Plus Bonn'
   OR krankenversicherung = 'IKK gesund plus';
   
   
-- 10. Alleinerziehende Mütter mit Kindern
SELECT * FROM mitarbeiter
WHERE geschlecht = 'w' AND verheiratet != 'ja' AND anzahlkinder >= 1;


-- 11. Erste 10 Zeilen der Tabelle krankenkasse
SELECT * FROM krankenkasse
LIMIT 10;


-- 12. Mitarbeiter:innen sortiert nach Abteilung, Name, Vorname
SELECT name, vorname, abteilung
FROM mitarbeiter
ORDER BY abteilung ASC, name ASC, vorname ASC;


-- 13. Mitarbeiter:innen mit Bonus, sortiert nach Abteilung und Bonus
SELECT name, vorname, abteilung, bonus
FROM mitarbeiter
ORDER BY abteilung, bonus;    -- oder ORDER BY abteilung DEsc, bonus ASC;

-- 14. Adressdaten mit Aliasnamen
SELECT 
  name AS Name,
  vorname AS Vorname,
  strasse AS Strasse,
  hausnummer AS Hausnummer,
  plz AS Postleitzahl,
  ort AS Ort
FROM mitarbeiter;


-- 15. Anzahl der Mitarbeiter:innen pro Ort
SELECT ort, COUNT(*) AS anzahl_mitarbeiter
FROM mitarbeiter
GROUP BY ort;
