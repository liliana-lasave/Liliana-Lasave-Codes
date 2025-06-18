
-- This query selects all songs (track_name) from the table 'track'
-- that have a validation score of 3 or higher.
-- The results are sorted first by validation in descending order
-- (from highest to lowest), and then alphabetically by track name.
SELECT track_name, validation
from track
WHERE validation >= 3
ORDER BY validation DESC, track_name;

--

-- In this query, the value 9 is used instead of 3
-- because there are no songs in the database with a rating lower than 3.
-- Therefore, the filter was adjusted to return at least one actual result.
SELECT album.album_name, track.track_name, track.validation
FROM track
JOIN album ON track.album_id = album.album_id
WHERE album.album_name = '1989'
	AND track.validation < 9;
    
--
    
-- This query creates a complete list showing:
-- the album name, track title, interpreter (artist), and genre.
-- It joins the tables 'track', 'album', 'interpreter', and 'genre'
-- and orders the result alphabetically by the album name.
SELECT
	album.album_name,
    track.track_name,
    interpreter.interpreter_name,
    genre.genre_name
FROM track
JOIN album ON track.album_id = album.album_id
JOIN interpreter ON track.interpreter_id = interpreter.interpreter_id
JOIN genre ON album.genre_id = genre.genre_id
ORDER BY album.album_name ASC;

--

-- This query calculates how many songs belong to each music genre.
-- It joins the tables 'track', 'album', and 'genre',
-- groups the results by genre name,
-- and orders the output by the number of tracks in descending order.
SELECT genre.genre_name, COUNT(track.track_id) AS total_tracks
FROM track
JOIN album ON track.album_id = album.album_id
JOIN genre ON album.genre_id = genre.genre_id
GROUP BY genre.genre_name
ORDER BY total_tracks DESC;

--

-- Update genre name from 'Rock' to 'International Rock'
UPDATE genre
SET genre_name = 'International Rock'
WHERE genre_name = 'Rock';

-- Update genre name from 'Ballad' to 'Romantic Ballad'
UPDATE genre
SET genre_name = 'Romantic Ballad'
WHERE genre_name = 'Ballad';

-- First, retrieve all genres to find the correct genre_id values.
SELECT * FROM genre;

-- Then update the genre name 'Rock' to 'International Rock'
-- using its unique ID to satisfy safe update mode.
UPDATE genre
SET genre_name = 'International Rock'
WHERE genre_id = 2;

-- Update the genre name 'Ballad' to 'Romantic Ballad'
-- also using the genre_id to ensure the update is precise and safe.
UPDATE genre
SET genre_name = 'Romantic Ballad'
WHERE genre_id = 4;

-- This query displays all music genres currently stored in the 'genre' table.
-- It is used to verify that the previous updates to genre names were applied correctly.
SELECT * FROM genre;

--

-- This query shows all albums that do not have a genre assigned
SELECT * 
FROM album
WHERE genre_id IS NULL;

-- This DELETE query would remove all albums that have no genre assigned.
-- However, there are no albums in the database with genre_id IS NULL,
-- so this query does not delete any rows.
DELETE FROM album
WHERE genre_id IS NULL;

--





