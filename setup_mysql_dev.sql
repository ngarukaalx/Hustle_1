-- prepares a Mysql server for the hustle project

CREATE DATABASE IF NOT EXISTS hstl_dev_db;
CREATE USER IF NOT EXISTS 'hstl_dev'@'localhost' IDENTIFIED BY 'hstl_dev_pwd';
GRANT ALL PRIVILEGES ON `hstl_dev_db`.* TO 'hstl_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hstl_dev'@'localhost';
FLUSH PRIVILEGES;
