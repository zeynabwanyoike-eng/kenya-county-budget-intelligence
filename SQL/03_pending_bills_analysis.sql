-- KENYA COUNTY BUDGET INTELLIGENCE
-- PENDING BILLS ANALYSIS

-- 1. National pending bills by financial year
SELECT
    financial_year,
    ROUND(SUM(amount), 2) AS total_pending_bills_ksh_millions
FROM pending_bills
GROUP BY financial_year
ORDER BY LEFT(financial_year, 4)::INTEGER;


-- 2. Top 10 counties with highest pending bills in FY 2024/25
SELECT
    county,
    ROUND(amount, 2) AS pending_bills_ksh_millions
FROM pending_bills
WHERE financial_year = '2024/25'
ORDER BY amount DESC
LIMIT 10;


-- 3. Bottom 10 counties with lowest reported pending bills in FY 2024/25
SELECT
    county,
    ROUND(amount, 2) AS pending_bills_ksh_millions
FROM pending_bills
WHERE financial_year = '2024/25'
  AND amount IS NOT NULL
ORDER BY amount ASC
LIMIT 10;