create database dw2;
use dw2;
create table year ( id int  PRIMARY KEY AUTO_INCREMENT,year int UNIQUE NOT NULL);
create table branch (id int PRIMARY KEY AUTO_INCREMENT,branch_id varchar (100) NOT NULL, branch_name varchar (100) NOT NULL);
create table college (id int PRIMARY KEY AUTO_INCREMENT, college_id varchar (100)NOT NULL , college_name varchar (300) NOT NULL,college_address varchar (500),college_state varchar (100));
alter table college add time_stamp numeric;
alter table branch add time_stamp numeric;

create table fees( id int AUTO_INCREMENT Primary key,college_id varchar(100) references college(college_id), year int references year(year) ON DELETE CASCADE, tuition_fee numeric, hostel_fee numeric,mess_fee numeric, security_fee numeric, other numeric);
create table academics( id int AUTO_INCREMENT Primary key,college_id varchar(100) references college(college_id), year int references year(year) ON DELETE CASCADE, branch_id varchar(100) references branch(branch_id) ,seats int,faculty int, cutoff int);
create table extracurricular( id int AUTO_INCREMENT Primary key,college_id varchar(100) references college(college_id), year int references year(year) ON DELETE CASCADE, clubs int, societis int,fests int , sports int , audi int);
create table reputation (id int AUTO_INCREMENT Primary key, college_id varchar (100),year int, rating int , CHECK (rating in (1,2,3,4,5)));

create table placements (id int AUTO_INCREMENT Primary key, roll_number varchar(100) , college_id varchar(100) , passing_year int,company_name varchar(200),profile varchar (300),package numeric);

create table quality_education (id int AUTO_INCREMENT Primary key, roll_number varchar(100) , college_id varchar(100), passing_year int ,satisfaction int, CHECK (satisfaction in (1,2,3,4,5)));
create table carrer_progression (id int AUTO_INCREMENT Primary key, roll_number varchar(100) , college_id varchar(100), passing_year int ,overall_satisfaction int, CHECK (overall_satisfaction in (1,2,3,4,5)));
create table placement_stats (d int AUTO_INCREMENT Primary key, college_id varchar(100) NOT NULL,year int NOT NULL, avg_package float, highest_package float);

create table student (id int AUTO_INCREMENT Primary key, roll_no varchar (100) NOT NULL,college_id varchar(100) NOT NULL, passing_year int NOT NULL, student_name varchar(300),degree varchar(200),time_stamp numeric);
