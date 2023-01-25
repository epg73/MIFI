CREATE TABLE user_list (
id int(11) NOT NULL,
name varchar(255) NOT NULL,
surname varchar(255) NOT NULL
) ENGINE InnoDB DEFAULT CHARSET utf8;

INSERT INTO user_list (id,name,surname) VALUES
(1,'John','Doe'),
(2,'Harley','Davidson'),
(3,'Suzuki','Honda');
