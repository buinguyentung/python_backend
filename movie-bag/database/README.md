### HOW TO INIT DATABASE

$ sudo mysql -p -u root
mysql> create database TUNG_server;
mysql> exit
$ sudo mysql -u root -p TUNG_server < schema-20221123-111415.sql

### Get the mysql table columns data type
mysql> SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = 'movie';

### Insert some data
INSERT INTO movie (name, casts, genres) 
VALUES ('The Shawshank Redemption', '["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"]', '["Drama"]');
INSERT INTO movie (name, casts, genres) 
VALUES ('The Godfather', '["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"]', '["Crime", "Drama"]');



