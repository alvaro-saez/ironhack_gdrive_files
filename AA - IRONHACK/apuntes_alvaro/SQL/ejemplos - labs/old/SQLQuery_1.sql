SELECT TOP 20pc.Name as  CategoryName, p.name as ProductName
FROM SalesLT.ProductCategory pc JOIN SalesLT.Product p ON pc.productcategoryid = p.productcategoryid
ORDER BY CategoryName;