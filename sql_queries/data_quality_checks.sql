-- Check for NULL values
SELECT COUNT(*) AS NullCount
FROM dbo.customer_transactions
WHERE customer_id IS NULL OR purchase_date IS NULL;

-- Check data freshness
SELECT MAX(purchase_date) AS LatestData
FROM dbo.customer_transactions;
