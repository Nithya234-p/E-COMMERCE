CREATE TABLE Products (
    id INT IDENTITY(1,1) PRIMARY KEY,
    cost FLOAT,
    category NVARCHAR(100),
    name NVARCHAR(255),
    brand NVARCHAR(100),
    retail_price FLOAT,
    department NVARCHAR(100),
    sku NVARCHAR(100),
    distribution_centre_id NVARCHAR(100)
);

INSERT INTO Products (
    cost, name, brand, retail_price, department, sku, category, distribution_centre_id
)
VALUES
(400.00, 'Product 1', 'Brand A', 499.99, 'Electronics', 'SKU001', 'Phones', 'DC001'),
(600.00, 'Product 2', 'Brand B', 799.00, 'Home appliances', 'SKU002', 'Kitchen', 'DC002');

SELECT TOP 10 * FROM Products;
