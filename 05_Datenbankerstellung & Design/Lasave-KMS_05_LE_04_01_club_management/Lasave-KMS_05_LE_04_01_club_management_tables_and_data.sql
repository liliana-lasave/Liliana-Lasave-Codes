-- Create the database to manage all data related to the club.
-- Switch to this database to create and work with its tables.
CREATE DATABASE club_management;
USE club_management;

-- This table stores the basic information of each player (first and last name).
-- Each player has a unique ID (player_id) as a primary key.
CREATE TABLE players (
	player_id INT AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(100),
	last_name VARCHAR(100)
);

--

-- This table stores the list of all teams in the club.
-- Each team has a unique ID (team_id) as a primary key and a name.
CREATE TABLE teams (
	team_id INT AUTO_INCREMENT PRIMARY KEY,
	team_name VARCHAR (100)
);

-- Add a description column to the teams table to clarify
-- the type of each team.
ALTER TABLE teams
ADD COLUMN team_description VARCHAR(255);

--

-- This table links players to teams, allowing a many-to-many relationship.
-- Each record represents one player's participation in one team.
-- It also records the date when the player joined the team.
CREATE TABLE team_player (
	player_id INT,
    team_id INT,
    start_date DATE,
	PRIMARY KEY (player_id, team_id),
    
    CONSTRAINT fk_player_id_player_team_from_players
		FOREIGN KEY (player_id) REFERENCES players(player_id),

	CONSTRAINT fk_team_id_player_team_from_teams
		FOREIGN KEY (team_id) REFERENCES teams(team_id)
	
);

--
-- This table stores information about each trainer,
-- including name, description, worked hours (in decimals), and salary. 
CREATE TABLE trainers (
	trainer_id INT AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
    trainer_description VARCHAR(255),
    worked_hours DECIMAL(5, 2) DEFAULT 0.00,
    salary DECIMAL(10, 2)
);

--

-- This table links trainers to teams, allowing a many-to-many relationship.
-- Each record represents one trainer's participation in one team.
-- It also records the date when the trainer joined the team.
CREATE TABLE trainer_team (
	trainer_id INT,
    team_id INT,
    start_date DATE,
	PRIMARY KEY (trainer_id, team_id),
    
    CONSTRAINT fk_trainer_id_trainer_team_from_trainers
		FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id),

	CONSTRAINT fk_team_id_trainer_team_from_teams
		FOREIGN KEY (team_id) REFERENCES teams(team_id)
	
);

--

-- This table stores information about education or training programs that can be completed by trainers.
-- Each education has a unique ID (education_id) as a primary key, a name, a description, a certain duration in hours and a level.
CREATE TABLE education (
	education_id INT AUTO_INCREMENT PRIMARY KEY,
	education_name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    duration_hours DECIMAL(5, 2),
    education_level VARCHAR(50)
);

--

-- This table links trainers to training programs (education), allowing a many-to-many relationship.
-- Each record represents one trainer's participation in one training program.
-- It also records the date when the trainer completed the training program.
-- The table also includes a link to the digital certificate.
CREATE TABLE trainer_education (
	trainer_id INT,
    education_id INT,
    completion_date DATE,
    certificate_url VARCHAR(255),
	PRIMARY KEY (trainer_id, education_id),
    
    CONSTRAINT fk_trainer_id_trainer_education_from_trainers
		FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id),

	CONSTRAINT fk_education_id_trainer_education_from_education
		FOREIGN KEY (education_id) REFERENCES education(education_id)
	
);

-- This statement adds a column to store the duration in hours
-- of each training program completed by a trainer.
ALTER TABLE trainer_education
ADD COLUMN duration_hours DECIMAL(5, 2)
AFTER education_id;

-- This statement adds a column to store a description of the training completed by a trainer.
ALTER TABLE trainer_education
ADD COLUMN description VARCHAR(255)
AFTER duration_hours;

-- These columns were added by mistake and are not needed in the current design.
-- Therefore, we remove them from the table trainer_education.
ALTER TABLE trainer_education
DROP COLUMN duration_hours;

ALTER TABLE trainer_education
DROP COLUMN description;

--

-- This table stores information about training sessions.
-- Each session has a unique ID, a date, a start time, a duration, and a place.
-- Each session is associated with one trainer and one team.
-- No two sessions can occur at the same date and time for the same trainer and team.
CREATE TABLE training_sessions (
	session_id INT AUTO_INCREMENT PRIMARY KEY,
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    duration_minutes INT UNSIGNED CHECK (duration_minutes >= 30),
    place VARCHAR(100),
    
    trainer_id INT,
    team_id INT,
    
    CONSTRAINT fk_trainer_id_training_sessions_from_trainers
		FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id),
	
    CONSTRAINT fk_team_id_training_sessions_from_teams
		FOREIGN KEY (team_id) REFERENCES teams(team_id),
        
	CONSTRAINT unique_trainer_team_date
		UNIQUE (trainer_id, team_id, session_date, start_time)
);

-- Drop the old column 'place'
ALTER TABLE training_sessions
DROP COLUMN place;

-- Add the new column 'place_id'
ALTER TABLE training_sessions
ADD COLUMN place_id INT;

-- This statement ensures that every training session is assigned to a valid place.
-- It modifies the 'place_id' column to be NOT NULL, 
-- enforcing that no session can exist without a location.
ALTER TABLE training_sessions
MODIFY COLUMN place_id INT NOT NULL;

-- Add the foreign key constraint linking to 'places'
ALTER TABLE training_sessions
ADD CONSTRAINT fk_place_id_training_sessions_from_places
FOREIGN KEY (place_id) REFERENCES places(place_id);

--

-- This table stores information about the available training places.
-- Each place has a unique ID, a name, and an optional description.
-- Training sessions are assigned to one of these places.
CREATE TABLE places (
	place_id INT AUTO_INCREMENT PRIMARY KEY,
	place_name VARCHAR(100),
	place_description VARCHAR(255)
);

-- Add an address column to store the location of each training place.
ALTER TABLE places
ADD COLUMN address VARCHAR(255) AFTER place_name;

--
-- Insert sample players into the 'players' table
INSERT INTO players (first_name, last_name) VALUES
('Diego', 'Pérez'),
('Andrés', 'Jiménez'),
('Luis', 'Ortega'),
('Paula', 'Ruiz'),
('Valentina', 'Ramírez'),
('Lucía', 'Gómez'),
('Fernando', 'Castro'),
('Martina', 'García'),
('Pedro', 'Martínez'),
('Camila', 'Romero'),
('Laura', 'Delgado'),
('Jorge', 'Torres'),
('Miguel', 'Rodríguez'),
('Ricardo', 'Moreno');

--

-- Insert sample trainers into the 'trainers' table,
-- with discipline and experience level
INSERT INTO trainers (first_name, last_name, trainer_description, worked_hours, salary) VALUES
('Laura', 'Martínez', 'Experienced volleyball coach', 0.00, 2800.00),
('Luis', 'García', 'Experienced basketball coach', 0.00, 2750.00),
('Valentina', 'Flores', 'Novice volleyball assistant', 0.00, 1800.00),
('Ricardo', 'Jiménez', 'Experienced futsal coach', 0.00, 2900.00),
('Martina', 'López', 'Experienced curling coach', 0.00, 2700.00),
('Andrés', 'Ramírez', 'Novice basketball assistant', 0.00, 1900.00),
('Pedro', 'Castro', 'Novice curling coach', 0.00, 2000.00),
('Elena', 'Sánchez', 'Experienced futsal coach', 0.00, 2800.00);

--

-- This trigger automatically updates the total worked hours of a trainer
-- every time a new training session is inserted.
-- It converts the session's duration from minutes to hours and adds it
-- to the trainer's worked_hours field.
DELIMITER $$

CREATE TRIGGER trg_update_worked_hours
AFTER INSERT ON training_sessions
FOR EACH ROW
BEGIN
  UPDATE trainers
  SET worked_hours = worked_hours + (NEW.duration_minutes / 60.0)
  WHERE trainer_id = NEW.trainer_id;
END$$

DELIMITER ;


--

INSERT INTO teams (team_name, team_description) VALUES
('Southside Juniors', 'Junior volleyball team for ages 12-14'),
('Northside Panthers', 'Basketball team for senior players'),
('Eastfield Eagles', 'Youth futsal team for ages 10-12'),
('Westwood Curlers', 'Beginner curling team for adults'),
('Riverdale Rockets', 'Advanced volleyball team for adults'),
('Downtown Dribblers', 'Intermediate basketball team'),
('Uptown Strikers', 'Teen futsal team for ages 15-17'),
('Lakeside Sweepers', 'Curling team for seniors'),
('Greenhill Spikers', 'Mixed volleyball team for college students'),
('Metro Hoopers', 'Competitive adult basketball team'),
('Sunset Shooters', 'Recreational futsal team'),
('Hilltop Hammers', 'Professional curling team'),
('City Slam', 'Urban youth basketball team'),
('Forest Flyers', 'Young beginners volleyball team');

--

-- This statement inserts records into the trainer_team table, 
-- establishing the many-to-many relationship between trainers and teams.
-- Each entry indicates which trainer is coaching which team and since when.
-- Some trainers coach more than one team.
-- Insert trainers and the teams they coach into the trainer_team table
INSERT INTO trainer_team (trainer_id, team_id, start_date) VALUES
(1, 1, '2024-01-15'),
(2, 2, '2024-02-10'),
(3, 3, '2023-11-20'),
(4, 4, '2023-12-01'),
(5, 5, '2024-01-05'),
(6, 6, '2024-03-12'),
(7, 7, '2023-10-05'),
(8, 8, '2024-01-22'),
(7, 9, '2024-02-14'),
(8, 10, '2024-01-30'),
(1, 11, '2024-02-18'),
(2, 12, '2024-03-01'),
(3, 13, '2023-12-15'),
(4, 14, '2024-02-25'),
(5, 2, '2024-02-22'),
(6, 3, '2024-03-05');

--

-- Insert 4 training courses for coaches into the education table
INSERT INTO education (education_name, description, duration_hours, education_level) VALUES
('Volleyball Coaching Basics', 'Introductory course on volleyball techniques and team management.', 20.0, 'Beginner'),
('Basketball Advanced Tactics', 'Advanced strategies for coaching competitive basketball teams.', 35.0, 'Advanced'),
('Futsal Coaching Certification', 'Comprehensive course on futsal rules, drills, and team dynamics.', 30.0, 'Intermediate'),
('Curling Team Leadership', 'Training focused on curling strategy and team coordination.', 25.0, 'Intermediate');

--

-- Insert trainer-course relationships with completion date, 
-- and certificate link
-- This records which training programs each trainer has completed.alter
INSERT INTO trainer_education (trainer_id, education_id, completion_date, certificate_url) VALUES
(1, 1, '2023-11-10', 'https://certificates.example.com/trainer1_volleyball.pdf'),
(2, 2, '2024-01-05', 'https://certificates.example.com/trainer2_basketball.pdf'),
(3, 3, '2023-12-15', 'https://certificates.example.com/trainer3_futsal.pdf'),
(4, 4, '2024-02-01', 'https://certificates.example.com/trainer4_curling.pdf'),
(5, 1, '2023-10-20', 'https://certificates.example.com/trainer5_volleyball.pdf'),
(6, 2, '2023-12-28', 'https://certificates.example.com/trainer6_basketball.pdf'),
(7, 3, '2024-01-14', 'https://certificates.example.com/trainer7_futsal.pdf'),
(8, 4, '2024-02-20', 'https://certificates.example.com/trainer8_curling.pdf'),
(7, 1, '2024-01-18', 'https://certificates.example.com/trainer9_volleyball.pdf'),
(8, 2, '2024-03-03', 'https://certificates.example.com/trainer10_basketball.pdf');

--

-- Insert sample data into the 'places' table.
-- Each place is associated with a specific sport and has a descriptive name and location.
INSERT INTO places (place_name, address, place_description) VALUES
('Arena Norte', 'Calle Belgrano 1201', 'Indoor stadium for basketball games and training.'),
('Club Olímpico', 'Avenida Libertad 555', 'Multipurpose court used mainly for volleyball training.'),
('Polideportivo Sur', 'Calle San Martín 2300', 'Indoor futsal facility with locker rooms and stands.'),
('Centro de Curling Ártico', 'Ruta Provincial 9, Km 18', 'Ice rink facility for curling practice and events.');

--

-- Insert data into 'player_team'.
-- Each record links a player to a team and includes the date the player joined the team.
INSERT INTO player_team (player_id, team_id, start_date) VALUES
(1, 1, '2023-09-10'),
(2, 1, '2023-10-12'),
(3, 2, '2023-11-01'),
(4, 2, '2023-11-15'),
(5, 3, '2024-01-05'),
(6, 3, '2024-01-06'),
(7, 4, '2024-02-01'),
(8, 4, '2024-02-02'),
(9, 5, '2023-12-10'),
(10, 6, '2024-01-20'),
(11, 7, '2023-10-30'),
(12, 8, '2023-09-25'),
(13, 9, '2023-08-14'),
(14, 10, '2024-03-03'),

-- Some players also belong to a second team.
-- Insert extra players into the player_team table.
INSERT INTO player_team (player_id, team_id, start_date) VALUES
(1, 12, '2024-03-01'),
(3, 13, '2024-03-15'),
(6, 12, '2024-04-10'),
(9, 12, '2024-02-05');
INSERT INTO player_team (player_id, team_id, start_date) VALUES
(2, 11, '2024-03-12'),
(4, 12, '2024-03-18'),
(5, 13, '2024-04-01'),
(7, 14, '2024-04-05');

DELETE FROM player_team;

DELETE FROM player_team
WHERE player_id IS NOT NULL;

DELETE FROM player_team
WHERE player_id IS NOT NULL AND team_id IS NOT NULL;

DROP TABLE player_team;

--

-- This table links players to teams, allowing a many-to-many relationship.
-- Each record represents one player's participation in one team.
-- It also records the date when the player joined the team.
CREATE TABLE player_team (
	player_id INT,
    team_id INT,
    start_date DATE,
	PRIMARY KEY (player_id, team_id),
    
    CONSTRAINT fk_player_id_player_team_from_players
		FOREIGN KEY (player_id) REFERENCES players(player_id),

	CONSTRAINT fk_team_id_player_team_from_teams
		FOREIGN KEY (team_id) REFERENCES teams(team_id)
	
);

--

-- Insert initial player-team associations with realistic start dates.
INSERT INTO player_team (player_id, team_id, start_date) VALUES
(1, 1, '2023-09-10'),
(2, 1, '2023-10-12'),
(3, 2, '2023-11-01'),
(4, 2, '2023-11-15'),
(5, 3, '2024-01-05'),
(6, 3, '2024-01-06'),
(7, 4, '2024-02-01'),
(8, 4, '2024-02-02'),
(9, 5, '2023-12-10'),
(10, 6, '2024-01-20'),
(11, 7, '2023-10-30'),
(12, 8, '2023-09-25'),
(13, 9, '2023-08-14'),
(14, 10, '2024-03-03'),
(1, 12, '2024-03-01'),
(2, 11, '2024-03-12'),
(3, 13, '2024-03-15'),
(4, 12, '2024-03-18'),
(5, 13, '2024-04-01'),
(6, 14, '2024-04-10'),
(7, 14, '2024-04-05'),
(9, 11, '2024-02-05');

--

-- Insert training session records.
-- Each session has a date, time, duration, place, trainer, and team.
INSERT INTO training_sessions (
    session_date, start_time, duration_minutes, place_id, trainer_id, team_id
) VALUES
('2024-03-01', '17:00:00', 60, 1, 1, 1),
('2024-03-02', '10:00:00', 90, 2, 2, 2),
('2024-03-03', '09:00:00', 60, 3, 3, 3),
('2024-03-04', '14:00:00', 75, 4, 4, 4),
('2024-03-05', '16:30:00', 45, 1, 1, 11),
('2024-03-06', '18:00:00', 60, 2, 2, 12),
('2024-03-07', '19:00:00', 90, 3, 3, 13),
('2024-03-08', '15:30:00', 60, 4, 4, 14),
('2024-03-09', '17:15:00', 75, 1, 5, 2),
('2024-03-10', '10:00:00', 90, 2, 6, 3);

