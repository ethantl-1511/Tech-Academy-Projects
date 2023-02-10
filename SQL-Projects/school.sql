--Create School database
create database db_school;
use db_school

--Create school tables
create table classes (
	class_id int not null primary key identity (1,1), --pk
	class_name varchar(50) not null
);

create table students (
	student_id int not null primary key identity (1,1), --pk
	student_name varchar(50) not null,
	class_id int,  --fk for classes tables
	instructor_id int, --fk for instructors table
);

create table instructors (
	instructor_id int not null primary key identity (1,1), --pk
	instructor_name varchar(50) not null
);

--Create foreign key assignment with constraints
alter table students
	add constraint fk_class_id foreign key (class_id) references classes(class_id)
;
alter table students
	add constraint fk_instructor_id foreign key (instructor_id) references instructors(instructor_id)
;

--Add values
---Add classes to classes table
insert into classes
	values
	('Software Developer Boot Camp'),
	('C# Boot Camp')
;
select * from classes; --check values

---Add students
insert into students (student_name)
	values
	('Hugh Jackman'),
	('Ryan Reynolds'),
	('Halle Berry'),
	('Anna Paquin'),
	('James Marsden'),
	('Alan Cumming')
;
select * from students; --check values, class_id / instructor_id are currently NULL

---Add instructors
insert into instructors
	values
	('Patrick Stewart'),
	('Ian McKellen')
;
select * from instructors; --check values

--Update student table, assign values to class_id
update students
set class_id = 1
where student_name = 'Hugh Jackman';
update students
set class_id = 1
where student_name = 'Ryan Reynolds';
update students
set class_id = 1
where student_name = 'Halle Berry';
update students
set class_id = 2
where student_name = 'Anna Paquin';
update students
set class_id = 2
where student_name = 'James Marsden';
update students
set class_id = 2
where student_name = 'Alan Cumming';

select * from students; --check values, instructor_id is currently NULL

--Update student table, assign values to instructor_id
update students
set instructor_id = 1
where class_id = 1;

update students
set instructor_id = 2
where class_id = 2;

select * from students; --check values

-- Query instructor names
select instructor_name
from instructors;

-- Query students in alphabetical order
select student_name
from students
order by student_name;

-- Query that displays all classes, with the students and Instructors assigned to each
select 
	class_name as 'Class:',
	student_name as 'Student:',
	instructor_name as 'Instructor'
from students
	inner join classes on classes.class_id = students.class_id
	inner join instructors on instructors.instructor_id = students.instructor_id