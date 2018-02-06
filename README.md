## SET UP
To set up the database just go into mysql using mysql -u root -p.
Then type:
* CREATE DATABASE GoodDay;
* CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'test123';
* GRANT ALL PRIVILEGES ON 'GoodDay'.* TO 'testuser'@'localhost';

Then quit mysql and type:
`mysql -u testuser -p GoodDay < build_database.sql`
