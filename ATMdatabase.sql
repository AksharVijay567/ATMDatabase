CREATE DATABASE atmdatabase;
use atmdatabase;
CREATE TABLE customers (
    customername varchar(255),
    customerpin int,
    customeramount double,
    customerid int
);
INSERT INTO customers (customername, customerpin, customeramount, customerid)
VALUES ('akshar', '1111', '10000', '1');
SELECT * FROM customers;
DROP DATABASE atmdatabase;

