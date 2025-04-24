
-- Create the database
CREATE DATABASE IF NOT EXISTS NanoBioConference;
USE NanoBioConference;

-- Table: Speakers
CREATE TABLE Speakers (
     speaker_id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(100) NOT NULL,
     email VARCHAR(100) UNIQUE NOT NULL,
     organization VARCHAR(100) NOT NULL
);

-- Table: Participants
CREATE TABLE Participants (
     participant_id INT AUTO_INCREMENT PRIMARY KEY,
     name VARCHAR(100) NOT NULL,
     email VARCHAR(100) UNIQUE NOT NULL,
     organization VARCHAR(100) NOT NULL
);

-- Table: Topics 
CREATE TABLE Topics (
     topic_id INT AUTO_INCREMENT PRIMARY KEY,
     title VARCHAR(200) NOT NULL,
     description TEXT NOT NULL,
     duration_min INT,
     max_num_participants INT,
     speaker_id INT,
     FOREIGN KEY (speaker_id) REFERENCES Speakers(speaker_id)
);

-- Junction Table: Participants_Topics
CREATE TABLE Participants_Topics (
     participant_id INT,
     topic_id INT,
     PRIMARY KEY (participant_id, topic_id),
     FOREIGN KEY (participant_id) REFERENCES Participants(participant_id),
     FOREIGN KEY (topic_id) REFERENCES Topics(topic_id)
);

-- Insert sample speakers
INSERT INTO Speakers (name, email, organization) VALUES
('Dr. Jane Smith', 'jane.smith@nanomed.com', 'Nanomed Institute'),
('Prof. John Doe', 'john.doe@biomaterials.com', 'BioMaterials Corp'),
('Dr. Alice Johnson', 'alice.johnson@ethics.org', 'Ethics in Tech Org');

-- Insert conference topics
INSERT INTO Topics (title, description, speaker_id, duration_min, max_num_participants) VALUES
('Nanomedicine: Applications in Drug Delivery',
  'Exploring the use of nanoparticles for targeted drug delivery systems
and personalized medicine.', 1, 30, 60),
('Bio-inspired Nanomaterials',
  'Development of advanced nanomaterials mimicking biological structures
for sustainable technology.', 2, 40, 120),
('Ethical Implications in Medical Nanotech',
  'Addressing ethical challenges in nanotechnology applications for
healthcare and human enhancement.', 3, 20, 300);

-- Insert participants
INSERT INTO Participants (name, email, organization) VALUES
('María López', 'maria.lopez@utec.edu', 'Universidad Tec'),
('Ahmed Khan', 'ahmed.khan@biotech.com', 'BioTech Solutions'),
('Emily Chen', 'emily.chen@nanohealth.com', 'NanoHealth Inc.');

-- Map participants to topics
INSERT INTO Participants_Topics (participant_id, topic_id) VALUES
(1, 1),  -- María registered for Nanomedicine
(1, 2),  -- María also registered for Bio-materials
(2, 3),  -- Ahmed registered for Ethics
(3, 1),  -- Emily registered for Nanomedicine
(3, 3);  -- Emily also registered for Ethics
