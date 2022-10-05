/**************************************************************************

	Lab02.sql
	
	BD del Lab01 (https://dbfiddle.uk/)
		- Probado en SQL Server
		- Probado en Postgre		

**************************************************************************/

-- Inner Join
SELECT *
FROM Cars INNER JOIN Invoices ON Cars.ID = Invoices.Car

-- Full join
SELECT *
FROM Cars FULL JOIN Invoices ON Cars.ID = Invoices.Car

-- Left join
SELECT *
FROM Cars LEFT JOIN Invoices ON Cars.ID = Invoices.Car
	
-- Right join
SELECT *
FROM Cars RIGHT JOIN Invoices ON Cars.ID = Invoices.Car

-- Exclusive left join
SELECT *
FROM Cars LEFT JOIN Invoices ON Cars.ID = Invoices.Car
WHERE Invoices.Car IS NULL

-- Exclusive right join
SELECT *
FROM Cars RIGHT JOIN Invoices ON Cars.ID = Invoices.Car
WHERE Cars.ID IS NULL

-- Exclusive full join
SELECT *
FROM Cars FULL JOIN Invoices ON Cars.ID = Invoices.Car
WHERE Cars.ID IS NULL OR Invoices.Car IS NULL

-- Cross join
SELECT *
FROM Cars CROSS JOIN Invoices

