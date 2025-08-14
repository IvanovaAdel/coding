CREATE TABLE customer(
    customer_id int primary key AUTO_INCREMENT,
    name VARCHAR(50),
    phone VARCHAR(15)
);



CREATE TABLE pizzas (
pizza_id int primary key AUTO_INCREMENT,
name VARCHAR(50),
price DECIMAL(5,2) CHECK (price >= 0)
);

CREATE TABLE employees(
employee_id int primary key AUTO_INCREMENT,
name VARCHAR(50),
role VARCHAR(30),
salary DECIMAL(8,2) CHECK (salary > 0)
);

CREATE TABLE orders (
order_id int primary key AUTO_INCREMENT,
customer_id int ,
order_date DATE,
employee_id int,
 FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);


CREATE TABLE order_items(
order_id int,
pizza_id int,
quantity int CHECK (quantity > 0),
PRIMARY KEY (order_id, pizza_id),
FOREIGN KEY (order_id) REFERENCES orders(order_id),
FOREIGN KEY (pizza_id) REFERENCES pizzas(pizza_id)
);


INSERT INTO customer (name, phone)
VALUES 
('Анна Иванова', '89990001122'),
('Петр Смирнов', '89990003344'),
('Сергей Кузнецов', '89990005566');
SELECT * FROM customer;

INSERT INTO employees (name, role, salary)
VALUES
('Мария Петрова', 'Курьер', 45000.00),
('Игорь Соколов', 'Повар', 40000.00);

INSERT INTO pizzas (name, price)
VALUES
('Четыре сыра', 750.00),
('Сезонная', 650.00),
('Маргарита', 500.00);

INSERT INTO orders (customer_id, order_date, employee_id)
VALUES (1, CURDATE(), 2);

INSERT INTO order_items (order_id, pizza_id, quantity)
VALUES 
(1, 1, 1),
(1, 2, 1);

SELECT * FROM orders;
SELECT * FROM order_items;


INSERT INTO orders (customer_id, order_date, employee_id)
VALUES (2, CURDATE(), 1);


INSERT INTO order_items (order_id, pizza_id, quantity)
VALUES (2, 3, 2);  


SELECT * FROM orders WHERE order_id = 2;
SELECT * FROM order_items WHERE order_id = 2;



UPDATE pizzas 
SET price = price * 1.15;

SELECT * FROM pizzas;

UPDATE customer
SET phone = '89998887766'
WHERE customer_id = 3;

ALTER TABLE pizzas
ADD category VARCHAR(20);

UPDATE pizzas
SET category = CASE 
    WHEN name = 'Четыре сыра' THEN 'Классическая'
    WHEN name = 'Сезонная' THEN 'Классическая'
    WHEN name = 'Маргарита' THEN 'Острая'
END;


CREATE TABLE suppliers(
supplier_id int primary key AUTO_INCREMENT,
name VARCHAR(50),
phone VARCHAR(20)
);

INSERT INTO suppliers (name, phone)
VALUES 
('Ирина Иванова', '89990001122'),
('Григорий Смирнов', '89990003344');

ALTER TABLE pizzas
ADD supplier_id INT;

ALTER TABLE pizzas
ADD FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id);

UPDATE pizzas SET supplier_id = 1 WHERE pizza_id IN (1, 2);
UPDATE pizzas SET supplier_id = 2 WHERE pizza_id = 3;
