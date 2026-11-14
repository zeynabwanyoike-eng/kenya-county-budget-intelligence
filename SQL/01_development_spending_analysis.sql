-- KENYA COUNTY BUDGET INTELLIGENCE
-- DEVELOPMENT SPENDING ANALYSIS

-- 1. National development spending by financial year
SELECT
    financial_year,
    ROUND(SUM(amount), 2) AS total_development_spending_ksh_millions
FROM development_spending
GROUP BY financial_year
ORDER BY LEFT(financial_year, 4)::INTEGER;


-- 2. Top 10 counties by development spending in FY 2024/25
SELECT
    county,
    ROUND(amount, 2) AS development_spending_ksh_millions
FROM development_spending
WHERE financial_year = '2024/25'
ORDER BY amount DESC
LIMIT 10;


-- 3. Bottom 10 counties by development spending in FY 2024/25
SELECT
    county,
    ROUND(amount, 2) AS development_spending_ksh_millions
FROM development_spending
WHERE financial_year = '2024/25'
ORDER BY amount ASC
LIMIT 10;