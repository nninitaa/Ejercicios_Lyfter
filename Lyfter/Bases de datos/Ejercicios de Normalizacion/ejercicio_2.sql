CREATE TABLE InsuranceCompany (
    CompanyID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(50),
);

CREATE TABLE VehicleModel (
    ModelID INTEGER PRIMARY KEY AUTOINCREMENT,
    Make VARCHAR(50),
    Model VARCHAR(50),
    Year INT,
    UNIQUE (Make, Model, Year)
);

CREATE TABLE Vehicle (
    VIN INT PRIMARY KEY,
    ModelID INT,
    Color VARCHAR(20),
    FOREIGN KEY (ModelID) REFERENCES VehicleModel(ModelID)
);

CREATE TABLE Owner (
    OwnerID INT PRIMARY KEY,
    Name VARCHAR(50),
    PhoneNumber VARCHAR(15)
);

CREATE TABLE Owner_Car (
    OwnerCarID INTEGER PRIMARY KEY AUTOINCREMENT, 
    OwnerID INT,
    VIN INT,
    InsuranceCompanyID INT,
    InsurancePolicy VARCHAR(50),
    FOREIGN KEY (OwnerID) REFERENCES Owner(OwnerID),
    FOREIGN KEY (VIN) REFERENCES Vehicle(VIN),
    FOREIGN KEY (InsuranceCompanyID) REFERENCES InsuranceCompany(CompanyID)
);

INSERT INTO InsuranceCompany (CompanyID, Name) VALUES
    (1, 'ABC Insurance'),
    (2, 'XYZ Insurance'),
    (3, 'DEF Insurance'),
    (4, 'GHI Insurance');

INSERT INTO VehicleModel (ModelID, Make, Model, Year) VALUES
    (1, 'Honda', 'Accord', 2003),
    (2, 'Honda', 'CR-V', 2014),
    (3, 'Chevrolet', 'Volt', 2015);

INSERT INTO Vehicle (VIN, ModelID, Color) VALUES
    (1, 1, 'Blue'),
    (2, 2, 'Red'),
    (3, 3, 'White');

INSERT INTO Owner (OwnerID, Name, PhoneNumber) VALUES
    (1, 'Alice', '123-456-7890'),
    (2, 'Bob', '987-654-3210'),
    (3, 'Claire', '555-123-4567'),
    (4, 'Dave', '111-222-3333');

INSERT INTO Owner_Car (OwnerID, VIN, InsuranceCompanyID, InsurancePolicy) VALUES
    (1, 1, 1, 'Fire & Theft'),
    (2, 2, 2, 'Full Cover'),
    (3, 3, 3, 'Collision'),
    (4, 1, 4, 'Basic Legal');

SELECT * FROM Vehicle;
SELECT * FROM Owner;
SELECT * FROM Owner_Car;
  