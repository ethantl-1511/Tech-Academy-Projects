--Create Library database
create database db_library;
use db_library;

--Create Library tables
create table library_branch (
	branchID int not null primary key identity (1,1), --pk
	branchName varchar(50) not null,
	branchAddress varchar(50) not null
);

create table book_copies (
	bookID int, --fk to books
	branchID int, --fk to library_branch
	number_of_copies int not null
);

create table books  (
	bookID int not null primary key identity (1,1), --pk
	title varchar(50) not null,
	publisherName varchar(50) --fk to publisher
);

create table book_authors (
	bookID int, --fk to books
	authorName varchar(50) not null
);

create table publisher (
	publisherName varchar(50) not null primary key, --pk
	publisherAddress varchar(50) not null,
	publisherPhone varchar(50) not null
);

create table book_loans (
	bookID int, --fk to books
	branchID int, --fk to library_branch
	cardNo int, --fk to borrower
	dateOut date not null,
	dateDue date not null
);

create table borrower (
	cardNo int not null primary key, --pk
	borrowerName varchar(50) not null,
	borrowerAddress varchar(50) not null,
	borrowerPhone varchar(50) not null
);

--In case of reset needed:
--drop table library_branch
--drop table book_copies
--drop table books
--drop table book_authors
--drop table publisher
--drop table book_loans
--drop table borrower

--Create foreign keys
alter table book_copies add constraint fk_bookID foreign key (bookID) references books(bookID);
alter table book_copies add constraint fk_branchID foreign key (branchID) references library_branch(branchID);

alter table books add constraint fk_publisherName foreign key (publisherName) references publisher(publisherName);

alter table book_authors add constraint fk_bookID_2 foreign key (bookID) references books(bookID);

alter table book_loans add constraint fk_bookID_3 foreign key (bookID) references books(bookID);
alter table book_loans add constraint fk_branchID_2 foreign key (branchID) references library_branch(branchID);
alter table book_loans add constraint fk_cardNo foreign key (cardNo) references borrower(cardNo);

--Add values
---Library branch names and addresses
insert into library_branch 
	(branchName, branchAddress)
	values
	('Sharpstown','70391 Lazaro Shores'),
	('Fritschchester','336 Margarete Light'),
	('Bartolettichester','47682 Satterfield Underpass'),
	('Wehnerstad','851 Mayert Ports'),
	('Shaneview','99297 Skye Plaza'),
	('South Jaleel','7480 Predovic Keys')
;

---Borrower information
insert into borrower 
	(cardNo, borrowerName, borrowerAddress, borrowerPhone)
	values
	('486458','Kairi Neff','8784 Shannon Course','202-918-2132'),
	('415487','Rashid Strachan','76789 Rogahn Stravenue','240-677-0503'),
	('466753','Zackary Voss','82455 Feeney Plaza','202-960-9613'),
	('430842','Vanna Priddy','946 Buckridge Oval','305-641-5941'),
	('460098','Tatianna An','64282 Mario River','505-776-0622'),
	('429875','Chase Nowlin','07823 Toy Crescent','505-676-0743'),
	('499721','Dallin Bankston','45123 Kiehn Run','228-224-2735'),
	('461643','Lilianne Cauley','049 Titus Trace','332-227-7022')
;
---Publisher information
insert into publisher 
	(publisherName, publisherAddress, publisherPhone)
	values
	('Miking Ciccone','25728 Nitzsche Haven','206-414-7482'),
	('Sabina Loy','161 Beahan Way','209-639-0120'),
	('Easten Prevost','765 Edmund Unions','240-774-6091'),
	('Yael Chavis','06740 Pfannerstill Plaza','505-644-4646'),
	('Rylen Squires','1526 Dach Neck','505-644-7836'),
	('Thais Lasley','362 Heidenreich Villages','339-215-6105'),
	('Rileigh Tavares','41231 Koch Lakes','341-332-0139'),
	('Asiel Tarrant','60943 Parker Passage','225-951-8197'),
	('Johnathan Bruce','03019 Willms Lake','228-626-8403'),
	('Dhilan Walcott','9696 Pattie Villages','415-345-5348')
;
---Book titles and publishers
insert into books
	(title, publisherName)
	values
	('The Lost Tribe','Miking Ciccone'),
	('A Random Bond','Miking Ciccone'),
	('These Random Eyes','Sabina Loy'),
	('Under the Random Lights','Easten Prevost'),
	('A Random Inheritance','Easten Prevost'),
	('The Random Author','Easten Prevost'),
	('The Random Message','Thais Lasley'),
	('A Random Marriage','Yael Chavis'),
	('The Claws of Mario','Rylen Squires'),
	('My Life and Mario','Rileigh Tavares'),
	('Dinner and Mario','Rileigh Tavares'),
	('Works of Art','Asiel Tarrant'),
	('Art for Survival','Johnathan Bruce'),
	('The Changing of Art','Johnathan Bruce'),
	('Art We Choose','Dhilan Walcott'),
	('More to Democracy','Dhilan Walcott'),
	('Ghost of the Democracy','Dhilan Walcott'),
	('The Dragon of Humanity','Sabina Loy'),
	('The Millennial Dragon','Yael Chavis'),
	('When the Dragon Fell','Yael Chavis')
;
---Book authors
insert into book_authors 
	(bookID, authorName)
	values
	(1, 'Loralei Lum'),
	(2, 'Sawyer Rivas'),
	(3, 'Michelangelo Resendiz'),
	(4, 'Emersen Kiel'),
	(5, 'Aaric Wagers'),
	(6, 'Michelangelo Resendiz'),
	(7, 'Zyion Huskey'),
	(8, 'Indiana Stidham'),
	(9, 'Devion Graybill'),
	(10, 'Zyion Huskey')
;
---Book copies
insert into book_copies
	(bookID, branchID, number_of_copies)
	values
	(1,1,2),
	(2,1,2),
	(3,1,3),
	(4,1,5),
	(5,1,2),
	(6,2,3),
	(7,2,6),
	(8,2,7),
	(9,2,3),
	(10,3,5),
	(11,3,3),
	(12,3,5),
	(13,3,2),
	(14,3,4),
	(15,4,3),
	(16,4,2),
	(17,4,4),
	(18,5,2),
	(19,5,2),
	(20,5,5)
;
select * from book_copies

---book loan information
insert into book_loans
	(bookID,branchID,cardNo,dateOut,dateDue) 
	values
	(1,1,'486458','11-01-2022','12-31-2022'),
	(4,1,'415487','10-05-2022','12-31-2022'),
	(6,2,'429875','11-01-2022','12-31-2022'),
	(10,3,'460098','10-05-2022','12-31-2022'),
	(13,3,'430842','11-01-2022','12-31-2022'),
	(15,4,'499721','11-01-2022','12-31-2022'),
	(15,4,'466753','10-05-2022','12-31-2022'),
	(16,4,'461643','10-05-2022','12-31-2022'),
	(18,5,'430842','10-05-2022','12-31-2022'),
	(20,5,'486458','11-01-2022','12-31-2022')
;

-- Queries
SELECT * 
FROM ((book_loans FULL OUTER JOIN borrower ON book_loans.cardNo = borrower.cardNo) 
	FULL OUTER JOIN books on book_loans.bookID = books.bookID)

--- Query that returns all book titles and author names
SELECT 
	books.title AS 'Book Title:',
	book_authors.authorName as 'Author:'
FROM books
	inner join book_authors on book_authors.bookID = books.bookID