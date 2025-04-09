CREATE DATABASE tax;
USE tax;
CREATE TABLE rates (Province CHAR(3), Rate FLOAT);
INSERT INTO rates VALUES
('BC', 0.12),
('AB', 0.05),
('SK', 0.05),
('MN', 0.12),
('ON', 0.13),
('QC', 0.14975),
('NL', 0.15),
('NS', 0.15),
('PEI', 0.15),
('NB', 0.15),
('YT', 0.05),
('NU', 0.05),
('NT', 0.05);

CREATE TABLE Data (Amount INT, Rate FLOAT);