
-- Customer Payment Data
-- customer_id	customer	mode	city
-- 101	Olivia Barrett	Netbanking	Portland
-- 102	Ethan Sinclair	Credit Card	Miami
-- 103	Maya Hernandez	Credit Card	Seattle
-- 104	Liam Donovan	Netbanking	Denver
-- 105	Sophia Nguyen	Credit Card	New Orleans
-- 106	Caleb Foster	Debit Card	Minneapolis
-- 107	Ava Patel	Debit Card	Phoenix
-- 108	Lucas Carter	Netbanking	Boston
-- 109	Isabella Martinez	Netbanking	Nashville
-- 110	Jackson Brooks	Credit Card	Boston


-- from this table find total payments according to each payment mehtod

SELECT mode, COUNT(*) as total_payments
FROM customer_payments
GROUP BY mode;