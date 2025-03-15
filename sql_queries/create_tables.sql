CREATE TABLE dbo.customer_transactions (
    customer_id VARCHAR(50),
    purchase_date DATE,
    total_spend FLOAT,
    avg_basket_size FLOAT,
    num_transactions INT,
    PRIMARY KEY (customer_id, purchase_date)
);
