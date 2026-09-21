## 1. Datos originales 

| OrderID | CustomerName | Phone | Address | ProductID | ProductName | Price | Quantity | SpecialRequest | DeliveryTime |
|---------|--------------|-------|---------|-----------|-------------|-------|----------|----------------|--------------|
| 001 | Alice  | 123-456-7890 | 123 Main St    | 101 | Cheeseburger | $8  | 2 | No onions     | 6:00 PM |
| 001 | Alice  | 123-456-7890 | 123 Main St    | 102 | Fries        | $3  | 1 | Extra ketchup | 6:00 PM |
| 002 | Bob    | 987-654-3210 | 456 Elm St     | 103 | Pizza        | $12 | 1 | Extra cheese  | 7:30 PM |
| 002 | Bob    | 987-654-3210 | 4th Avenue     | 102 | Fries        | $3  | 2 | None          | 7:30 PM |
| 003 | Claire | 555-123-4567 | 789 Oak St     | 105 | Salad        | $6  | 1 | No croutons   | 12:00 PM |
| 004 | Claire | 555-123-4567 | 464 Georgia St | 106 | Water        | $1  | 1 | None          | 5:00 PM |

La tabla original posee algunos errores como:
- Datos de clientes repetidos
- Datos de productos repetidos
- Una orden puede tener varios productos
- Algunos atributos dependen de CustomerID
- Otros de ProductID
- Otros de OrderID
- Un error importante es que Bob posee dos direcciones

## 2. Aplicacion de 1FN

| OrderID | CustomerName | Phone | Address | ProductID | ProductName | Price | Quantity | SpecialRequest | DeliveryTime |
|---------|--------------|-------|---------|-----------|-------------|-------|----------|----------------|--------------|
| 001 | Alice  | 123-456-7890 | 123 Main St    | 101 | Cheeseburger | $8  | 2 | No onions     | 6:00 PM |
| 001 | Alice  | 123-456-7890 | 123 Main St    | 102 | Fries        | $3  | 1 | Extra ketchup | 6:00 PM |
| 002 | Bob    | 987-654-3210 | 456 Elm St     | 103 | Pizza        | $12 | 1 | Extra cheese  | 7:30 PM |
| 002 | Bob    | 987-654-3210 | 4th Avenue     | 102 | Fries        | $3  | 2 | None          | 7:30 PM |
| 003 | Claire | 555-123-4567 | 789 Oak St     | 105 | Salad        | $6  | 1 | No croutons   | 12:00 PM |
| 004 | Claire | 555-123-4567 | 464 Georgia St | 106 | Water        | $1  | 1 | None          | 5:00 PM |

## Que cambio?
No es necesario hacer cambios en la estructura de la tabla. La tabla ya cumple con las condiciones necesarias para estar en 1FN.

## 3. Aplicacion de 2FN

| CustomerID | CustomerName | Phone        |
|------------|--------------|--------------|
| 1	         | Alice	    | 123-456-7890 |
| 2	         | Bob          | 987-654-3210 |
| 3	         | Claire       | 555-123-4567 |

| ProductID | ProductName  | Price |
| --------- | ------------ | ------|
| 101       | Cheeseburger |    $8 |
| 102       | Fries        |    $3 |
| 103       | Pizza        |   $12 |
| 105       | Salad        |    $6 |
| 106       | Water        |    $1 |

| OrderID | CustomerID | Address        | DeliveryTime |
| ------- | ---------  | -------------- | ------------ |
| 001     | 1          | 123 Main St    | 6:00 PM      |
| 002     | 2          | 456 Elm St     | 7:30 PM      |
| 003     | 3          | 789 Oak St     | 12:00 PM     |
| 004     | 4          | 464 Georgia St | 5:00 PM      |

| OrderItemID | OrderID | ProductID | Quantity | SpecialRequest |
| ----------  | ------- | --------- | -------  | -------------- |
| 1           | 001     | 101       |        2 | No onions      |
| 2           | 001     | 102       |        1 | Extra ketchup  |
| 3           | 002     | 103       |        1 | Extra cheese   |
| 4           | 002     | 102       |        2 | None           |
| 5           | 003     | 105       |        1 | No croutons    |
| 6           | 004     | 106       |        1 | None           |

## Que cambio? 
Se separan los datos de los clientes y de los productos en sus propias tablas. También se crea una tabla para relacionar cada producto con su respectiva orden. De esta manera, cada tabla contiene información relacionada entre sí y se evita guardar los mismos datos varias veces.

## 4. Aplicacion de 3FN
Se revisa nuevamente las tablas para asegurarnos de que cada dato dependa directamente de la información que identifica el registro. Por lo tanto, las tablas quedan separadas de manera que cada una contiene la información que le corresponde y no depende de otros datos que no sean necesarios para identificarla.
