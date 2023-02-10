--Create Payroll Database
CREATE DATABASE db_payroll;
USE db_payroll;

--Create tables
CREATE TABLE employee (
	employee_id INT NOT NULL PRIMARY KEY IDENTITY (1,1), --primary key
	job_id INT NOT NULL, --foreign key for job table
	first_name VARCHAR(50) NOT NULL,
	last_name varchar(50) not null,
	date_of_hire date
);

create table job (
	job_id INT NOT NULL PRIMARY KEY identity (1,1), --PK
	job_title varchar(50) not null,
	job_dept varchar(50) not null,
	salary_id int not null --FK for salary table
);

create table salary (
	salary_id int not null primary key identity (1,1), --PK
	hourly_rate money not null
);

create table payroll (
	payroll_date date not null,
	employee_id int not null, --FK for employee table
	hours_worked int not null
);

--Create foreign key relationships
alter table employee
	add foreign key (job_id) references job(job_id); --Connects employee table/job_id to job table/job_id

alter table job
	add foreign key (salary_id) references salary(salary_id); --Connects job table/salary_id to salary table/salary_id

alter table payroll
	add foreign key (employee_id) references employee(employee_id); --Connects payroll table/employee_id to employee table/employee_id

--Add values
---Salary/Hourly rates
insert into salary
	values
	(19.50),
	(20.00),
	(20.50),
	(21.00),
	(21.50)
;
select * from salary; --Check to see if values were input correctly

---Job titles and their corresponding salary_id number
insert into job
	values
	('AR Director', 'Accounting', 2),
	('HR Director', 'Human Resources', 4),
	('Developer', 'IT', 5),
	('Customer Service Manager', 'Operations', 3),
	('Sales Manager', 'Sales and Marketing', 1)
;
select * from job; --Check to see if values were input correctly

---Employee values
insert into employee
	values
	(1, 'Sam', 'Smith', '2018-11-28'),
	(2, 'Amanda', 'James', '2020-04-01'),
	(3, 'David', 'McGarth', '2021-12-11'),
	(4, 'Valerie', 'Ringer', '2014-07-31'),
	(5, 'Andrea', 'Antivilo', '2019-02-04')
;
select * from employee; --Check values

---Payroll values
insert into payroll
	values
	('2023-06-07', 1, 40),
	('2023-06-07', 2, 25),
	('2023-06-07', 3, 38),
	('2023-06-07', 4, 22),
	('2023-06-07', 5, 34)
;
select * from payroll --Check values

-- Query all data
select * from employee
	INNER JOIN payroll on employee.employee_id = payroll.employee_id
	INNER JOIN job on employee.job_id = job.job_id
	INNER JOIN salary on job.salary_id = salary.salary_id;

-- Query total pay for each employee in pay period
select 
	employee.first_name as 'First Name:',
	employee.last_name as 'Last Name:',
	payroll.hours_worked as 'Hours:',
	salary.hourly_rate as 'Rate:',
	payroll.hours_worked * salary.hourly_rate as 'Total Pay:'
from employee
	INNER JOIN payroll on employee.employee_id = payroll.employee_id
	INNER JOIN job on employee.job_id = job.job_id
	INNER JOIN salary on job.salary_id = salary.salary_id;