
-- Create the main database for the club management system.
CREATE DATABASE club_management_final;
USE club_management;

-- Create the 'players' table to store basic personal information about each player.
CREATE TABLE players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
);

-- Create the 'teams' table to store information about all teams in the club.
CREATE TABLE teams (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(100)
);

-- Add a description column to the 'teams' table to describe the type of each team.
ALTER TABLE teams
ADD COLUMN team_description VARCHAR(255);

-- Create the 'trainers' table to store personal and professional information of trainers.
CREATE TABLE trainers (
    trainer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    trainer_description VARCHAR(255),
    worked_hours DECIMAL(5, 2) DEFAULT 0.00,
    salary DECIMAL(10, 2)
);

-- Create the 'education' table to store information about training programs that trainers can complete.
CREATE TABLE education (
    education_id INT AUTO_INCREMENT PRIMARY KEY,
    education_name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    duration_hours DECIMAL(5, 2),
    education_level VARCHAR(50)
);

-- Create the 'places' table to store all available training locations.
CREATE TABLE places (
    place_id INT AUTO_INCREMENT PRIMARY KEY,
    place_name VARCHAR(100),
    place_description VARCHAR(255)
);

-- Add an address column to the 'places' table to indicate the location of each training place.
ALTER TABLE places
ADD COLUMN address VARCHAR(255) AFTER place_name;

-- Create the 'player_team' table to link players to teams (many-to-many relationship).
-- It uses a primary key ID to allow multiple participations in the same team.
CREATE TABLE player_team (
    player_team_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    team_id INT NOT NULL,
    start_date DATE,
    FOREIGN KEY (player_id) REFERENCES players(player_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

-- Create the 'trainer_team' table to link trainers to teams (many-to-many relationship).
-- Uses an ID instead of composite PK to allow multiple assignments.
CREATE TABLE trainer_team (
    trainer_team_id INT AUTO_INCREMENT PRIMARY KEY,
    trainer_id INT NOT NULL,
    team_id INT NOT NULL,
    start_date DATE,
    FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

-- Create the 'trainer_education' table to track which trainers completed which training programs.
-- Uses a surrogate primary key instead of a composite key for flexibility.
CREATE TABLE trainer_education (
    trainer_education_id INT AUTO_INCREMENT PRIMARY KEY,
    trainer_id INT NOT NULL,
    education_id INT NOT NULL,
    completion_date DATE,
    certificate_url VARCHAR(255),
    FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id),
    FOREIGN KEY (education_id) REFERENCES education(education_id)
);

-- Create the 'training_sessions' table to store each scheduled training session.
-- Includes date, time, duration, and location, with constraints to avoid overlaps.
CREATE TABLE training_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    session_date DATE NOT NULL,
    start_time TIME NOT NULL,
    duration_minutes INT UNSIGNED CHECK (duration_minutes >= 30),
    trainer_id INT,
    team_id INT,
    place_id INT NOT NULL,
    FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (place_id) REFERENCES places(place_id),
    UNIQUE (trainer_id, team_id, session_date, start_time)
);

-- Create a trigger to automatically update the worked hours of a trainer
-- after a new training session is inserted.
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

-- Insert example data into 'players'.
INSERT INTO players (first_name, last_name) VALUES
('Diego', 'Pérez'), ('Andrés', 'Jiménez'), ('Luis', 'Ortega'), ('Paula', 'Ruiz'),
('Valentina', 'Ramírez'), ('Lucía', 'Gómez'), ('Fernando', 'Castro'), ('Martina', 'García'),
('Pedro', 'Martínez'), ('Camila', 'Romero'), ('Laura', 'Delgado'), ('Jorge', 'Torres'),
('Miguel', 'Rodríguez'), ('Ricardo', 'Moreno');

-- Insert example data into 'trainers'.
INSERT INTO trainers (first_name, last_name, trainer_description, worked_hours, salary) VALUES
('Laura', 'Martínez', 'Experienced volleyball coach', 0.00, 2800.00),
('Luis', 'García', 'Experienced basketball coach', 0.00, 2750.00),
('Valentina', 'Flores', 'Novice volleyball assistant', 0.00, 1800.00),
('Ricardo', 'Jiménez', 'Experienced futsal coach', 0.00, 2900.00),
('Martina', 'López', 'Experienced curling coach', 0.00, 2700.00),
('Andrés', 'Ramírez', 'Novice basketball assistant', 0.00, 1900.00),
('Pedro', 'Castro', 'Novice curling coach', 0.00, 2000.00),
('Elena', 'Sánchez', 'Experienced futsal coach', 0.00, 2800.00);

-- Insert example data into 'education'.
INSERT INTO education (education_name, description, duration_hours, education_level) VALUES
('Volleyball Coaching Basics', 'Introductory course on volleyball techniques and team management.', 20.0, 'Beginner'),
('Basketball Advanced Tactics', 'Advanced strategies for coaching competitive basketball teams.', 35.0, 'Advanced'),
('Futsal Coaching Certification', 'Comprehensive course on futsal rules, drills, and team dynamics.', 30.0, 'Intermediate'),
('Curling Team Leadership', 'Training focused on curling strategy and team coordination.', 25.0, 'Intermediate');

-- Insert example data into 'places'.
INSERT INTO places (place_name, address, place_description) VALUES
('Arena Norte', 'Calle Belgrano 1201', 'Indoor stadium for basketball games and training.'),
('Club Olímpico', 'Avenida Libertad 555', 'Multipurpose court used mainly for volleyball training.'),
('Polideportivo Sur', 'Calle San Martín 2300', 'Indoor futsal facility with locker rooms and stands.'),
('Centro de Curling Ártico', 'Ruta Provincial 9, Km 18', 'Ice rink facility for curling practice and events.');

-- Insert example data into 'teams' before referencing them in foreign keys.
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

-- Insert player-team associations with start dates.
INSERT INTO player_team (player_id, team_id, start_date) VALUES
(1, 1, '2023-09-10'), (2, 1, '2023-10-12'), (3, 2, '2023-11-01'), (4, 2, '2023-11-15'),
(5, 3, '2024-01-05'), (6, 3, '2024-01-06'), (7, 4, '2024-02-01'), (8, 4, '2024-02-02'),
(9, 5, '2023-12-10'), (10, 6, '2024-01-20'), (11, 7, '2023-10-30'), (12, 8, '2023-09-25'),
(13, 9, '2023-08-14'), (14, 10, '2024-03-03'), (1, 12, '2024-03-01'), (2, 11, '2024-03-12'),
(3, 13, '2024-03-15'), (4, 12, '2024-03-18'), (5, 13, '2024-04-01'), (6, 14, '2024-04-10'),
(7, 14, '2024-04-05'), (9, 11, '2024-02-05');

-- Insert trainer-team relationships with start dates.
INSERT INTO trainer_team (trainer_id, team_id, start_date) VALUES
(1, 1, '2024-01-15'), (2, 2, '2024-02-10'), (3, 3, '2023-11-20'), (4, 4, '2023-12-01'),
(5, 5, '2024-01-05'), (6, 6, '2024-03-12'), (7, 7, '2023-10-05'), (8, 8, '2024-01-22'),
(7, 9, '2024-02-14'), (8, 10, '2024-01-30'), (1, 11, '2024-02-18'), (2, 12, '2024-03-01'),
(3, 13, '2023-12-15'), (4, 14, '2024-02-25'), (5, 2, '2024-02-22'), (6, 3, '2024-03-05');

-- Insert trainer-education completion records with certificates.
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

-- Insert training session data.
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
