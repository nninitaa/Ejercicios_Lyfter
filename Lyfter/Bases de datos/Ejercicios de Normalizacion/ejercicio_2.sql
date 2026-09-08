CREATE TABLE Car (
    VIN INT PRIMARY KEY,
    Make VARCHAR(50),
    Model VARCHAR(50),
    Year INT,
    Color VARCHAR(20)
);

CREATE TABLE Owner (
    OwnerID INT PRIMARY KEY,
    Name VARCHAR(50),
    PhoneNumber VARCHAR(15),
    VIN INT,
    FOREIGN KEY (VIN) REFERENCES Car(VIN)
);

CREATE TABLE Owner_Car (
    OwnerCarID INTEGER PRIMARY KEY AUTOINCREMENT, 
    OwnerID INT,
    VIN INT,
    InsuranceCompany VARCHAR(50),
    InsurancePolicy VARCHAR(50),
    FOREIGN KEY (OwnerID) REFERENCES Owner(OwnerID),
    FOREIGN KEY (VIN) REFERENCES Car(VIN)
);

INSERT INTO Car (VIN, Make, Model, Year, Color) VALUES
    (1, 'Honda', 'Accord', 2003, 'Silver'),
    (2, 'Honda', 'Accord', 2003, 'Silver'),
    (3, 'Honda', 'CR-V', 2014, 'Blue'),
    (4, 'Chevrolet', 'Volt', 2015, 'Red');

INSERT INTO Owner (OwnerID, Name, PhoneNumber, VIN) VALUES
    (1, 'Alice', '123-456-7890', 1),
    (2, 'Bob', '987-654-3210', 2),
    (3, 'Claire', '555-123-4567', 3),
    (4, 'Dave', '111-222-3333', 2);

INSERT INTO Owner_Car (OwnerID, VIN, InsuranceCompany, InsurancePolicy) VALUES
    (1, 1, 'ABC Insurance', 'Fire & Theft'),
    (2, 2, 'XYZ Insurance', 'Full Cover'),
    (3, 3, 'DEF Insurance', 'Collision'),
    (4, 2, 'GHI Insurance', 'Basic Legal');

SELECT * FROM Car;
SELECT * FROM Owner;
SELECT * FROM Owner_Car;
  