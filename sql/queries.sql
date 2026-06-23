-- Query 1
SELECT * FROM "01_fund_master" LIMIT 10;

-- Query 2
SELECT AVG(nav)
FROM "02_nav_history";

-- Query 3
SELECT MAX(nav)
FROM "02_nav_history";

-- Query 4
SELECT MIN(nav)
FROM "02_nav_history";

-- Query 5
SELECT COUNT(*)
FROM "08_investor_transactions";

-- Query 6
SELECT COUNT(*)
FROM "07_scheme_performance";

-- Query 7
SELECT *
FROM "03_aum_by_fund_house"
LIMIT 5;

-- Query 8
SELECT *
FROM "05_category_inflows"
LIMIT 5;

-- Query 9
SELECT *
FROM "09_portfolio_holdings"
LIMIT 5;

-- Query 10
SELECT *
FROM "10_benchmark_indices"
LIMIT 5;