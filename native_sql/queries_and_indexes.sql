--query 1:
EXPLAIN ANALYZE
SELECT
    target_city,
    air_force,
    COUNT(mission_id) AS mission_count
FROM mission
WHERE EXTRACT(YEAR FROM mission_date) = 1945 AND air_force IS NOT NULL
GROUP BY target_city, air_force
ORDER BY mission_count DESC LIMIT 1;

-- Index on Mission Date (Year) and Target City for the WHERE and GROUP BY operations
CREATE INDEX idx_mission_date_target_city ON mission (EXTRACT(YEAR FROM mission_date), target_city);

-- Index on Air Force for faster COUNT operations
CREATE INDEX idx_air_force ON mission (air_force);

--query 2:
EXPLAIN ANALYZE
SELECT
    target_country,
	bomb_damage_assessment,
	COUNT(bomb_damage_assessment)
FROM mission
WHERE airborne_aircraft > 5 AND target_country IS NOT NULL
GROUP BY target_country, bomb_damage_assessment
order by count(bomb_damage_assessment) DESC LIMIT 1;

-- Index on Airborne Aircraft for filtering
CREATE INDEX idx_airborne_aircraft ON mission (airborne_aircraft);

-- Index on Target Country for grouping
CREATE INDEX idx_target_country ON mission (target_country);

