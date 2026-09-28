-- 1. Count of complaints per App
SELECT app_name, COUNT(*) as total_complaints
FROM raw_reviews
GROUP BY app_name
ORDER BY total_complaints DESC;

-- 2. Breakdown of specific issues (Failed Transactions vs App Freezes vs Slow Refunds)
SELECT 
    app_name,
    SUM(CASE WHEN review_text LIKE '%failed%' THEN 1 ELSE 0 END) as failed_tx,
    SUM(CASE WHEN review_text LIKE '%freeze%' THEN 1 ELSE 0 END) as app_freezes,
    SUM(CASE WHEN review_text LIKE '%refund%' THEN 1 ELSE 0 END) as slow_refunds
FROM raw_reviews
GROUP BY app_name;

-- 3. Identifying peak hours for server delays (For AI feature engineering)
SELECT hour_of_day, AVG(server_delay_occurred) as delay_rate
FROM transaction_logs
GROUP BY hour_of_day
ORDER BY delay_rate DESC;