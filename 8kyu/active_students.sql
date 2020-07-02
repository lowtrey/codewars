-- Instructions
-- Create a simple SELECT query to display student information of all ACTIVE students.

-- TABLE STRUCTURE:

-- students
-- Id	FirstName	LastName	IsActive

-- Note: IsActive (true or false)


-- My Solution
SELECT * FROM students 
  WHERE IsActive = 1


-- Top Answer
SELECT * FROM students WHERE IsActive;