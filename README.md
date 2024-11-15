# Endpoints de la API

A continuación se describen los principales endpoints de la API con ejemplos de solicitud y respuesta.

## Autenticación

### Obtener token de autenticación

- **Método**: POST
- **Endpoint**: `/login`
- **Encabezado de la solicitud**:
  - `Authorization`: Credenciales en formato básico (`username:password` codificados en base64).

#### Cuerpo de la solicitud

```json
{
    "username": "tu_usuario",
    "password": "tu_contraseña"
}

Ejemplo de respuesta
{
    "Token": "Bearer tu_token_de_autenticacion"
}

```


## Usuarios

### Obtener y crear usuarios

Este endpoint permite listar todos los usuarios o crear un nuevo usuario. La creación de usuarios solo está permitida para administradores.

- **Método**: `GET` | `POST`
- **Endpoint**: `/users`
- **Encabezado de la solicitud**:
  - `Authorization`: Token JWT (Bearer token).

### Obtener usuarios

#### Ejemplo de solicitud (GET)

```http
GET /users HTTP/1.1
Host: tu-dominio.com
Authorization: Bearer tu_token_de_autenticacion
```

#### Ejemplo de respuesta para administradores

```json
[
  {
    "id": 1,
    "usuario": "admin",
    "is_admin": true
  },
  {
    "id": 2,
    "usuario": "user1",
    "is_admin": false
  }
]
```

#### Ejemplo de respuesta para usuarios no administradores

```json
[
  {
    "usuario": "user1"
  },
  {
    "usuario": "user2"
  }
]
```

### Crear un nuevo usuario

#### Ejemplo de solicitud (POST)

- **Requiere permisos de administrador**.

```http
POST /users HTTP/1.1
Host: tu-dominio.com
Content-Type: application/json
Authorization: Bearer tu_token_de_autenticacion
```

#### Cuerpo de la solicitud

```json
{
    "usuario": "nuevo_usuario",
    "contrasenia": "nueva_contrasenia"
}
```

#### Ejemplo de respuesta exitosa

```json
{
    "Mensaje": "Usuario creado correctamente",
    "Usuario": {
        "id": 3,
        "usuario": "nuevo_usuario",
        "is_admin": false
    }
}
```

#### Ejemplo de respuesta en caso de error

```json
{
    "Mensaje": "Fallo la creacion del nuevo usuario"
}
```

### Respuesta para usuarios no administradores al intentar crear un usuario

```json
{
    "Mensaje": "Solo el admin puede crear nuevos usuarios"
}
```

## Perfumes

### Obtener, crear, actualizar y eliminar perfumes

Este endpoint permite listar, crear, actualizar y eliminar perfumes. La creación, actualización y eliminación solo están permitidas para usuarios autenticados, y algunas operaciones requieren permisos de administrador.

### Obtener todos los perfumes

- **Método**: `GET`
- **Endpoint**: `/perfumes`
- **Encabezado de la solicitud**:
  - `Authorization`: Token JWT (Bearer token).

#### Ejemplo de solicitud (GET)

```http
GET /perfumes HTTP/1.1
Host: tu-dominio.com
Authorization: Bearer tu_token_de_autenticacion
```

#### Ejemplo de respuesta

```json
[
  {
    "id": 1,
    "nombre": "Perfume A",
    "marca": "Marca A",
    "precio": 100.0,
    "tipo": "Eau de Parfum",
    "sexo": "Unisex"
  },
  {
    "id": 2,
    "nombre": "Perfume B",
    "marca": "Marca B",
    "precio": 150.0,
    "tipo": "Eau de Toilette",
    "sexo": "Masculino"
  }
]
```

### Crear un nuevo perfume

- **Método**: `POST`
- **Endpoint**: `/perfumes`
- **Encabezado de la solicitud**:
  - `Authorization`: Token JWT (Bearer token).

#### Cuerpo de la solicitud

```json
{
    "nombre": "Nuevo Perfume",
    "marca": "Marca X",
    "precio": 120.0,
    "tipo": "Eau de Cologne",
    "sexo": "Femenino"
}
```

#### Ejemplo de respuesta exitosa

```json
{
    "id": 3,
    "nombre": "Nuevo Perfume",
    "marca": "Marca X",
    "precio": 120.0,
    "tipo": "Eau de Cologne",
    "sexo": "Femenino"
}
```

#### Ejemplo de respuesta en caso de error

```json
{
    "precio": ["Debe ser un número positivo"]
}
```

### Obtener, actualizar o eliminar un perfume por ID

- **Métodos**: `GET` | `PUT` | `DELETE`
- **Endpoint**: `/perfumes/<int:id>`
- **Encabezado de la solicitud**:
  - `Authorization`: Token JWT (Bearer token).

#### Ejemplo de solicitud (GET)

```http
GET /perfumes/1 HTTP/1.1
Host: tu-dominio.com
Authorization: Bearer tu_token_de_autenticacion
```

#### Ejemplo de respuesta

```json
{
    "id": 1,
    "nombre": "Perfume A",
    "marca": "Marca A",
    "precio": 100.0,
    "tipo": "Eau de Parfum",
    "sexo": "Unisex"
}
```

#### Ejemplo de solicitud (PUT)

```http
PUT /perfumes/1 HTTP/1.1
Host: tu-dominio.com
Content-Type: application/json
Authorization: Bearer tu_token_de_autenticacion
```

#### Cuerpo de la solicitud

```json
{
    "nombre": "Perfume Actualizado",
    "precio": 130.0
}
```

#### Ejemplo de respuesta exitosa

```json
{
    "id": 1,
    "nombre": "Perfume Actualizado",
    "marca": "Marca A",
    "precio": 130.0,
    "tipo": "Eau de Parfum",
    "sexo": "Unisex"
}
```

### Eliminar un perfume

- **Método**: `DELETE`
- **Endpoint**: `/perfumes/<int:id>`
- **Encabezado de la solicitud**:
  - `Authorization`: Token JWT (Bearer token).

#### Ejemplo de solicitud (DELETE)

```http
DELETE /perfumes/1 HTTP/1.1
Host: tu-dominio.com
Authorization: Bearer tu_token_de_autenticacion
```

#### Ejemplo de respuesta exitosa

```json
{
    "message": "Perfume eliminado correctamente"
}
```

#### Ejemplo de respuesta para usuarios no autorizados

```json
{
    "error": "No tienes permisos para realizar esta acción"
}
```
