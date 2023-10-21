-- Use the database
USE ecommerce_db;

-- Insert sample customers
INSERT INTO Customers (first_name, last_name, email, phone_number)
VALUES
    ('John', 'Doe', 'johndoe@example.com', '123-456-7890'),
    ('Jane', 'Smith', 'janesmith@example.com', '987-654-3210');

-- Insert sample products
INSERT INTO Products (name, description, price, stock_quantity)
VALUES
    ('Product 1', 'Description for Product 1', 19.99, 100),
    ('Product 2', 'Description for Product 2', 29.99, 50);

-- Insert sample orders
INSERT INTO Orders (customer_id, order_date, status)
VALUES
    (1, '2023-10-20', 'Processing'),
    (2, '2023-10-21', 'Shipped');

-- Insert sample order details
INSERT INTO OrderDetails (order_id, product_id, quantity, total_price)
VALUES
    (1, 1, 2, 39.98),
    (2, 2, 1, 29.99);
