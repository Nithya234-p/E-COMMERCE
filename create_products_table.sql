git init
git add create_products_table.sql
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
