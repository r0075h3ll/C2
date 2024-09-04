-- using postgresql

CREATE TABLE tasks (
    ID int NOT NULL serial,
    UUID varchar(100) NOT NULL,
    TASK text NOT NULL,

    PRIMARY KEY (ID)
    -- FOREIGN KEY (UUID) REFERENCES agents(UUID)
);

CREATE TABLE agents (
    ID int NOT NULL serial,
    UUID varchar(100) NOT NULL UNIQUE,
    PRIMARY KEY (ID)
);

CREATE TABLE users (
    ID int NOT NULL,
    username text NOT NULL UNIQUE,
    password text NOT NULL,

    PRIMARY KEY (ID)
);

INSERT INTO tasks values ('test-uid-inserted', 'ls -alt');

ALTER TABLE tasks
ADD CONSTRAINT fk_uuid
FOREIGN KEY (UUID) REFERENCES agents(UUID);


INSERT INTO tasks values (0,'7770abb0-587b-4428-9c67-801c6a62d99a', 'ls -alt');
INSERT INTO tasks values (1,'7540f7fa-9ec7-4b62-801f-661f9c7884c0', 'ls -alt');
INSERT INTO tasks values (2,'730f538a-5a91-42cc-a6ff-0b2520fc5629', 'ls -alt');
INSERT INTO tasks values (3,'17ba1ccc-151b-42c6-98a3-21fbf5ede07b', 'ls -alt');
INSERT INTO tasks values (4,'19fc4d9f-b99f-423c-b98e-7a68cf0d0a12', 'ls -alt');


INSERT INTO users values (0,'hardik', 'hardik');