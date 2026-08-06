# Fundamentos de Internet 

## 1. Del Cliente al Servidor

Qué hace el cliente (navegador).
- El navegador envia un request para pedir la pagina, y luego recibe y da la respuesta al usuario

Qué papel cumple el DNS.
- El DNS traduce el nombre a una direccion IP para que el navegador encuentre el servidor correcto

Qué ocurre con la dirección IP.
- Es la que identifica al servidor donde se encuentra la pagina web, y con la IP el navegador sabe a que servidor debe conectarse

Qué hace el servidor.
- El servidor recibe la solicitud del navegador, procesa la petición y envía la página web como respuesta

Cómo entra en juego el protocolo HTTP/HTTPS.
- Como es el que envia request y recibe responses, al escribir www.youtube.com el HTTP hace un request al servidor de Youtube.


## 2. Frontend y Backend en acción

Indique qué parte del sistema correspondería al frontend y cuál al backend.
- El frontend se encarga de mostrar los botones de agendar cita, citas pendientes, y uno para consultas. Ademas, un formulario donde el usuario ingresa nombre de usuario, contraseña y cedula. El backend se encargara de guardar los datos para la cita, guardar los datos para las citas pendientes como horario, dia y motivo de la cita, y mostrar consultas o hacer una. 

Mencione tres tecnologías posibles para cada uno.
Front end:
JavaScript
CSS
HTML

Back End:
JavaScript
C#
Python

Explique brevemente cómo el frontend se comunicaría con el backend (mencione los conceptos de API, HTTP y request/response).
- El front end se comunica a travez de una API mediante request utilizando protocolos como HTTP o HTTPS. Cuando el usuario quiere realizar una consulta, le envia un request a la API. Luego procesa la informacion y devuelve una respuesta con los datos de consulta que el Frontend mostrara al usuario.

## 3. REST vs SOAP vs GraphQL

Cómo completar la tabla:
Usa términos concisos (p. ej., “JSON/XML” en formato de datos).
En “nivel de flexibilidad”, piensa: ¿quién controla mejor lo que se envía/recibe, cliente o servidor?
En “dificultad de implementación”, considera curva de aprendizaje, herramientas y mantenimiento.
En “uso actual”, valora su presencia en proyectos modernos (Alta/Media/Baja).

| Tipo de API | Formato de datos usado | Nivel de flexibilidad  | Dificultad de implementación     | Uso actual (Alta / Media / Baja) 
|-------------|------------------------|------------------------|-------------------------------   |-----------------------------------|
| REST        |  Json                  |Muy flexible            | Medio, facil de comprender       | Alta                            
| SOAP        |  XML                   |Medio (Rigidos y estructurados)| Alto, complejo de entender| Baja                            
| GraphQL     |  Json                  |Muy flexible            | Bajo, mas moderno y facil        | Medio                              

**¿Cuál es más apropiada para una startup moderna? ¿Por qué?**
REST, es mas apropiado para una startup moderna ya que es un estandar muy utilizado, es facil de poder comprender e implementar, ademas es sencilla de manejar y altamente flexible.  

## 4. Explorando APIs con Postman

### 4.1 Selección de la API
- **Nombre de la API:** JSONPlaceholder
- **Descripción:** Es una API publica que permite realizar pruebas con HTTP y hace operaciones como GET, POST, PUT, entre otros.

### 4.2 Configuración en Postman
- **Nombre de la colección:** JSONPlaceholder API 
- **Solicitudes agregadas:**
  - GET - Obtener publicacion
  - POST - Crear publicacion
  - PUT/PATCH/DELETE - (PUT) Actualizar publicacion

### 4.3 Ejecución y análisis

GET
| Codigo de estado | Cuerpo de la respuesta | Headers revelantes | 
|------------------|------------------------|--------------------|       
|  200             |    JSON                | content-type, cache-control |

POST
| Codigo de estado | Cuerpo de la respuesta | Headers revelantes | 
|------------------|------------------------|--------------------|       
|   201            |      Json              |  content-length, location          |

PUT
| Codigo de estado | Cuerpo de la respuesta | Headers revelantes | 
|------------------|------------------------|--------------------|       
|     200          |        Json            |     content-type, cache-control         |

### 4.4 Explicación técnica

#### [Obtener publicacion]
- **Método HTTP:** GET
- **Endpoint:** https://www.postman.com/nina-araya-rojas-373186/workspace/irina-lyfter/request/57105817-64131ff2-a698-4659-9ad5-be83cd62c884?action=share&creator=57105817
- **Parámetros:** ID 1
- **Body:** 
{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
- **Descripción de la respuesta:** El contenido que esta escrito en el titulo y en el body es un texto de prueba que devuelve la API para simular la informacion.

- **Método HTTP:** POST
- **Endpoint:** https://www.postman.com/nina-araya-rojas-373186/workspace/irina-lyfter/request/57105817-01b1372b-a750-47ed-9bdc-de3e6f1c1680?action=share&creator=57105817
- **Parámetros:** No tiene
- **Body:** 
{
    "title": "Mi primera publicación",
    "body": "Hola desde Postman",
    "userId": 1,
    "id": 101
}
- **Descripción de la respuesta:** El body tiene la informacion que se envia al servidor para crear una nueva publicacion

- **Método HTTP:** PUT
- **Endpoint:** https://www.postman.com/nina-araya-rojas-373186/workspace/irina-lyfter/request/57105817-01b1372b-a750-47ed-9bdc-de3e6f1c1680?action=share&creator=57105817
- **Parámetros:** ID 1
- **Body:** 
{
    "id": 1,
    "title": "Título actualizado",
    "body": "Contenido actualizado",
    "userId": 1
}
- **Descripción de la respuesta:** Contiene la informacion actualizada de la publicacion que se hizo anteriormente, remplazando los datos anteriores por nuevos valores enviados.

### 4.5 Reflexión final

**¿Qué aprendiste del proceso?**

Realizar esta breve practica fue un proceso algo lento para mi, tomo mucho tiempo poder realizar cada ejercicio y completar con exito cada instruccion. A pesar de eso, me ayudo mucho a expandir mis ideas sobre el internet y generar mas conocimiento clave para el futuro. Me gusto aprender cosas como las APIs, los DNS, y terminos como Request-Response. Tambien me genero curiosidad cuando comenze a usar Postman, y aun siento que me falta mucho por poder aprender. Sin embargo, siento mucha emocion por ver que mas puedo estudiar y conocer sobre el internet.

