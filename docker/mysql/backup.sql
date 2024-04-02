create table user(
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    fecha DATE,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT
CHARSET=latin1;