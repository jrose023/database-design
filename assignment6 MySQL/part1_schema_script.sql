
DROP TABLE IF EXISTS clubs;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS buildings;
DROP TABLE IF EXISTS club_members;

DROP TABLE IF EXISTS clubs;
CREATE TABLE clubs(
	club_ID char(2),
	club_name varchar(50),
	club_dept varchar(50),
	club_desc text,
	club_dues int(5),
	club_email varchar(30),
	club_location varchar(50),
	club_pres varchar(20),
	club_sec varchar(20),
	club_treas varchar(20),
	club_url text,
	PRIMARY KEY(club_ID),
	CONSTRAINT
		FOREIGN KEY (club_location) 
		REFERENCES buildings (build_name)
);
INSERT INTO clubs VALUES("c1","NYU Programming Team","Computer Science","This is a club. This club is at NYU.",20,"npt@gmail.com","Courant","Chris","Caty","Caroline","npt.com");
INSERT INTO clubs VALUES("c2","WinC","Computer Science","This is a club. This club is at NYU.",50,"wic@gmail.com","Leslie eLab","Will","Wendy","Wade","wic.com");
INSERT INTO clubs VALUES("c3","Economics Club","Economics","This is a club. This club is at NYU.",100,"ecc@gmail.com","KMEC","Bill","Bob","Betty","ecc.com");
INSERT INTO clubs VALUES("c4","Poltics Club","Liberal Studies","This is a club. This club is at NYU.",0,"lsp@gmail.com","726 Broadway","Paul","Pam","Pat","lsp.com");
INSERT INTO clubs VALUES("c5","Delta Kappa Alpha","Tisch","This is a club. This club is at NYU.",500,"dka@gmail.com","Vanderbilt","Tyler","Tina","Tim","dka.com");
INSERT INTO clubs VALUES("c6","Comm Club","Media, Culture & Communications","This is a club. This club is at NYU.",0,"cmc@gmail.com","Steinhardt","Mary","Matt","Max","cmc.com");


DROP TABLE IF EXISTS students;
CREATE TABLE students(
	stu_name varchar(20),
	stu_netid varchar(6) NOT NULL,
	stu_major varchar(50),
	stu_email varchar(30),
	stu_phone char(12),
	stu_enroll_year int(4),
	stu_grad_year int(4) DEFAULT 0,
	PRIMARY KEY(stu_netid),
	CONSTRAINT
		FOREIGN KEY (stu_major) 
		REFERENCES departments (maj_name)
	
);
INSERT INTO students VALUES("John","jde294","Computer Science","j.e@gmail.com","123-456-7890",2014,NULL);
INSERT INTO students VALUES("Josh","jso026","Film","j.o@gmail.com","223-456-7890",2013,2017);
INSERT INTO students VALUES("Jane","jps359","Liberal Studies","j.s@gmail.com","323-456-7890",2014,NULL);
INSERT INTO students VALUES("Jack","jvf036","Media, Culture & Communication","j.f@gmail.com","423-456-7890",2015,NULL);
INSERT INTO students VALUES("Jill","jpt347","Economics","j.t@gmail.com","523-456-7890",2012, 2016);
INSERT INTO students VALUES("Judy","jid351","Math","j.d@gmail.com","623-456-7890",2014,NULL);
INSERT INTO students VALUES("Julz","jar892","Computer Science","j.r@gmail.com","723-456-7890",2014,NULL);
INSERT INTO students VALUES("Jaad","jbp892","Math","j.p@gmail.com","823-456-7890",2015,NULL);


DROP TABLE IF EXISTS club_members;
CREATE TABLE club_members(
	cm_num INT,
	member_name varchar(30) NOT NULL,
	club_title varchar(30) NOT NULL,
	member_join_date date DEFAULT NULL,
	member_resig_date date DEFAULT NULL,
	PRIMARY KEY(cm_num),
	CONSTRAINT
		FOREIGN KEY (member_name) 
		REFERENCES students (stu_name),
	CONSTRAINT 
		FOREIGN KEY (club_title) 
		REFERENCES clubs (club_name)
);
INSERT INTO club_members VALUES(1,"John","NYU Programming Team","2015-11-11",NULL);
INSERT INTO club_members VALUES(2,"Josh","Delta Kappa Alpha","2013-11-11","2017-11-11");
INSERT INTO club_members VALUES(3,"Jane","Politics Club","2014-11-11","2016-11-11");
INSERT INTO club_members VALUES(4,"Jack","Comm Club","2016-11-11",NULL);
INSERT INTO club_members VALUES(5,"Jill","Economics Club","2012-11-11","2016-11-11");
INSERT INTO club_members VALUES(6,"Judy","WinC","2015-11-11",NULL);
INSERT INTO club_members VALUES(7,"Julz","WinC","2015-11-11",NULL);
INSERT INTO club_members VALUES(8,"Julz","Politics Club","2015-11-11",NULL);


DROP TABLE IF EXISTS departments;
CREATE TABLE departments(
	maj_name varchar(30) NOT NULL,
	PRIMARY KEY(maj_name)
);
INSERT INTO departments VALUES ("English");
INSERT INTO departments VALUES ("Computer Science");
INSERT INTO departments VALUES ("Media, Culture & Communication");
INSERT INTO departments VALUES ("Economics");
INSERT INTO departments VALUES ("Film");
INSERT INTO departments VALUES ("Math");


DROP TABLE IF EXISTS buildings;
CREATE TABLE buildings(
	build_name varchar(30) NOT NULL,
	PRIMARY KEY(build_name)
);
INSERT INTO buildings VALUES("Kimmel");
INSERT INTO buildings VALUES("Vanderbilt");
INSERT INTO buildings VALUES("Courant");
INSERT INTO buildings VALUES("726 Broadway");
INSERT INTO buildings VALUES("Steinhardt");
INSERT INTO buildings VALUES("Leslie eLab");





