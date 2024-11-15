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
