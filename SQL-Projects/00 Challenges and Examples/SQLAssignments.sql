-- Assignment 1 --
SELECT *
FROM tbl_species

-- Assignment 2 --
SELECT species_name
FROM tbl_species
WHERE species_order = 3;

-- Assignment 3 --
SELECT nutrition_type
FROM tbl_nutrition
WHERE nutrition_cost <= 600;

-- Assignment 4 --
SELECT species_name
FROM tbl_nutrition INNER JOIN tbl_species ON tbl_nutrition.nutrition_id = tbl_species.species_nutrition
WHERE nutrition_id BETWEEN 2202 AND 2206;

-- Assignment 5 --
SELECT 
	species_name as 'Species Name: ',
	nutrition_type as 'Nutrition Type: '
FROM tbl_nutrition INNER JOIN tbl_species ON tbl_nutrition.nutrition_id = tbl_species.species_nutrition

-- Assignment 6 --
SELECT
	specialist_fname as 'First Name',
	specialist_lname as 'Last Name',
	specialist_contact as 'Number'
FROM tbl_care
	INNER JOIN tbl_specialist ON care_specialist = specialist_id
	INNER JOIN tbl_species ON species_care = care_id
WHERE species_name = 'penguin'