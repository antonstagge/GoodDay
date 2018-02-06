
DROP TABLE IF EXISTS data;

#data table
CREATE TABLE data(
    data_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    sleep TINYINT UNSIGNED NOT NULL,
    weather TINYINT UNSIGNED NOT NULL,
    breakfast TINYINT UNSIGNED NOT NULL,
    mindset TINYINT UNSIGNED NOT NULL,
    good_day BOOLEAN
);
