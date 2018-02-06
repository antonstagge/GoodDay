DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS data;

#data table
#data_id nad which_day has to be first 2 and good_day has to be last. 
CREATE TABLE data(
    data_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    which_day DATE NOT NULL,
    sleep TINYINT UNSIGNED NOT NULL,
    weather TINYINT UNSIGNED NOT NULL,
    breakfast TINYINT UNSIGNED NOT NULL,
    mindset TINYINT UNSIGNED NOT NULL,
    good_day BOOLEAN
);

#user table
CREATE TABLE user(
    user_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    lower_char CHAR(1) NOT NULL,
    upper_char CHAR(1) NOT NULL,
    current_data INT UNSIGNED,
    FOREIGN KEY (current_data) REFERENCES data(data_id)
);



INSERT INTO data(which_day, sleep, weather, breakfast, mindset) VALUES
("2018-02-06",5,3,5,4);

INSERT INTO user(first_name, last_name, lower_char, upper_char, current_data) VALUES
("Anton", "Stagge", 'a', 'A', 1),
("Cristian", "Osorio Bretti", 'c', 'C', NULL),
("Fredrik", "Omstedt", 'f', 'F', NULL),
("Erik", "Björck", 'e', 'E', NULL);
