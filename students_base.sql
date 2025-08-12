CREATE TABLE Groups_ (
  id INT AUTO_INCREMENT PRIMARY KEY,
  group_name VARCHAR(50) NOT NULL
);

CREATE TABLE Student (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  group_id INT NOT NULL,
  FOREIGN KEY (group_id) REFERENCES Groups_(id)
);

INSERT INTO Groups_ (group_name) VALUES ('gr1');
INSERT INTO Groups_ (group_name) VALUES ('gr2');
INSERT INTO Groups_ (group_name) VALUES ('gr3');

INSERT INTO Student (name, group_id) VALUES ("Grisha",'1');
INSERT INTO Student (name, group_id) VALUES ("Misha",'2');
INSERT INTO Student (name, group_id) VALUES ("Shishka",'3');
INSERT INTO Student (name, group_id) VALUES ("Arseny",'3');
INSERT INTO Student (name, group_id) VALUES ("Anton",'1');

SELECT 
  Student.id AS student_id,
  Student.name AS student_name,
  Groups_.group_name
FROM 
  Student
JOIN 
  Groups_ ON Student.group_id = Groups_.id;
  
SELECT 
  Groups_.group_name,
  COUNT(Student.id) AS student_count
FROM 
  Groups_
LEFT JOIN 
  Student ON Groups_.id = Student.group_id
GROUP BY 
  Groups_.id, Groups_.group_name;



SELECT * FROM Groups_;
SELECT * FROM Student
