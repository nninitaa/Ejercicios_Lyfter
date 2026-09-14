## 1. Datos originales 

| VIN         | Make      | Model  | Year | Color  | Owner ID | Owner Name | Owner Phone  | Insurance Company | Insurance Policy |
| ----------- | --------- | ------ | ---- | ------ | -------  | ---------- | ------------ | ----------------- | ---------------- |
| 1HGCM82633A | Honda     | Accord | 2003 | Silver |      101 | Alice      | 123-456-7890 | ABC Insurance     | Fire & Theft     |
| 1HGCM82633A | Honda     | Accord | 2003 | Silver |      102 | Bob        | 987-654-3210 | XYZ Insurance     | Full Cover       |
| 5J6RM4H79EL | Honda     | CR-V   | 2014 | Blue   |      103 | Claire     | 555-123-4567 | DEF Insurance     | Collision        |
| 1G1RA6EH1FU | Chevrolet | Volt   | 2015 | Red    |      104 | Dave       | 111-222-3333 | GHI Insurance     | Basic Legal      |


La tabla original posee algunos errores como:
- Un vehiculo puede pertenecer a personas diferentes
- Datos que no dependen de una misma PK
- Informacion del seguro pertenece a una relacion y no directamente del carro o propietario
- Relacion de propietario y vehiculo no esta representada para asociar un vehiculo con varios propietarios


## 2. Aplicacion de 1FN

| VIN         | Make      | Model  | Year | Color  | Owner ID | Owner Name | Owner Phone  | Insurance Company | Insurance Policy |
| ----------- | --------- | ------ | ---- | ------ | -------  | ---------- | ------------ | ----------------- | ---------------- |
| 1HGCM82633A | Honda     | Accord | 2003 | Silver |      101 | Alice      | 123-456-7890 | ABC Insurance     | Fire & Theft     |
| 1HGCM82633A | Honda     | Accord | 2003 | Silver |      102 | Bob        | 987-654-3210 | XYZ Insurance     | Full Cover       |
| 5J6RM4H79EL | Honda     | CR-V   | 2014 | Blue   |      103 | Claire     | 555-123-4567 | DEF Insurance     | Collision        |
| 1G1RA6EH1FU | Chevrolet | Volt   | 2015 | Red    |      104 | Dave       | 111-222-3333 | GHI Insurance     | Basic Legal      |

## Que cambio?
Esta tabla ya cumple con la regla de 1FN, y no es necesario realizar modificaciones en la tabla original. 

## 3. Aplicacion de 2FN

- Vehicle

| VIN | ModelID | Color |
|:---:|:-------:|:------|
|    1|        1| Blue  |
|    2|        2| Red   |
|    3|        3| White |

- Owner

| OwnerID | Name   | PhoneNumber  |
|:-------:|:-------|:-------------|
|       1 | Alice  | 123-456-7890 |
|       2 | Bob    | 987-654-3210 |
|       3 | Claire | 555-123-4567 |
|       4 | Dave   | 111-222-3333 |

- Owner_Car

| OwnerCarID | OwnerID | VIN | InsuranceCompanyID | InsurancePolicy |
|:----------:|:-------:|:---:|:------------------:|:----------------|
|          1 |       1 |   1 |                 1  | Fire & Theft    |
|          2 |       2 |   2 |                 2  | Full Cover      |
|          3 |       3 |   3 |                 3  | Collision       |
|          4 |       4 |   1 |                 4  | Basic Legal     |


## Que cambio? 
Ahora se separa la informacion, Vehicle contiene la informacion propia de cada vehiculo, Owner contiene la informacion de cada propietario y Owner_Car representa una relacion entre propietario y vehiculos, junto con la informacion del seguro correspondiente. 

## 4. Aplicacion de 3FN
Después de aplicar 2FN, se verifica que no existan dependencias transitivas. Cada atributo no clave depende directamente de la PK de su tabla, por lo que las relaciones cumplen con 3FN.