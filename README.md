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
```
Ejemplo de respuesta

{
    "Token": "Bearer tu_token_de_autenticacion"
}
----------------------

# Endpoints de la API

A continuación se describen los principales endpoints de la API con ejemplos de solicitud y respuesta.

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
