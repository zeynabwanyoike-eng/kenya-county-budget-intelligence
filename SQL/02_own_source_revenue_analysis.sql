-- KENYA COUNTY BUDGET INTELLIGENCE
-- OWN-SOURCE REVENUE ANALYSIS

-- 1. National own-source revenue by financial year
SELECT
    financial_year,
    ROUND(SUM(amount), 2) AS total_own_source_revenue_ksh_millions
FROM own_source_revenue
GROUP BY financial_year
ORDER BY LEFT(financial_year, 4)::INTEGER;


-- 2. Top 10 counties by own-source revenue in FY 2024/25
SELECT
    county,
    ROUND(amount, 2) AS own_source_revenue_ksh_millions
FROM own_source_revenue
WHERE financial_year = '2024/25'
ORDER BY amount DESC
LIMIT 10;


-- 3. Bottom 10 counties by own-source revenue in FY 2024/25
SELECT
    county,
    ROUND(amount, 2) AS own_source_revenue_ksh_millions
FROM own_source_revenue
WHERE financial_year = '2024/25'
ORDER BY amount ASC
LIMIT 10;