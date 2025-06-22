-- Query 1: List all players with their teams, 
-- ordered by the player's last name.
SELECT
	p.first_name,
    p.last_name,
    t.team_name,
    pt.start_date
FROM
	players p
JOIN 
	player_team pt ON p.player_id = pt.player_id
JOIN
	teams t ON pt.team_id = t.team_id
ORDER BY
	p.last_name, pt.start_date;
    
--

-- Query 2: List all trainers, grouped and sorted 
-- by the training course they completed.
SELECT
	t.first_name,
    t.last_name,
    e.education_name,
    te.completion_date
FROM
	trainers t
JOIN 
	trainer_education te ON t.trainer_id = te.trainer_id
JOIN
	education e ON te.education_id = e.education_id
ORDER BY
	e.education_name, t.last_name;
    
--

-- Query 3: List all players with their trainers.
SELECT
	p.first_name AS player_first_name,
    p.last_name AS player_last_name,
 	tr.first_name AS trainer_first_name,
    tr.last_name AS trainer_last_name,
    t.team_name AS team_team_name
FROM
	players p
JOIN 
	player_team pt ON pt.player_id = p.player_id
JOIN
	teams t ON t.team_id = pt.team_id
JOIN
	trainer_team trt ON trt.team_id = t.team_id
JOIN
	trainers tr ON tr.trainer_id = trt.trainer_id
ORDER BY
	p.last_name, tr.last_name;
    
--
-- Query 4: Increase all trainers' salaries by 25%
UPDATE trainers
SET salary = salary + (salary * 0.25)
WHERE trainer_id > 0;

