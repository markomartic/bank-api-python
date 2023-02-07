CREATE TABLE IF NOT EXISTS clients (
    id serial NOT NULL PRIMARY KEY, 
    firstName varchar(255) NOT NULL, 
    lastName varchar(255) NOT NULL, 
    emailId varchar(255) NOT NULL
);