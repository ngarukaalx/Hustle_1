-- prepares a Mysql server for the hustle project/test

CREATE DATABASE IF NOT EXISTS hstl_test_db;
CREATE USER IF NOT EXISTS 'hstl_test'@'localhost' IDENTIFIED BY 'hstl_test_pwd';
GRANT ALL PRIVILEGES ON `hstl_test_db`.* TO 'hstl_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hstl_test'@'localhost';
FLUSH PRIVILEGES;
