# 0x0E. SQL - More queries

# Types of joins
```
* INNER JOINS - An inner join between two tables will return only records where a joining field, such as a key, finds a match in both tables.
* SELF JOIN - Self-joins are used to compare values in a table to other values of the same table by joining different parts of a table together.
* LEFT JOIN -  left join keeps all of the original records in the left table and returns missing values for any columns from the right table where the joining field did not find a match.
* RIGHT JOIN - right join keeps all of the original records in the right table and returns missing values for any columns from the left table where the joining field did not find a match.
* CROSS JOIN - creates all possible combinations of two tables. CROSS JOIN does not require a field to join ON.
* UNION - UNION operator is used to vertically combine the results of two SELECT statements.
* INTERSECT - INTERSECT operator returns only identical rows from two tables.
* ANTI JOIN - chooses records in the first table where a condition is NOT met in the second table. It makes use of a WHERE clause to use exclude values from the second table.```
