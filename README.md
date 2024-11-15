# Documentación de la API

Esta API permite la autenticación básica para obtener un token de acceso, utilizando un endpoint protegido.

## Endpoints

### **POST** `/login`

Este endpoint permite a los usuarios autenticarse con sus credenciales y recibir un token de acceso. El token tiene una validez de 20 minutos y contiene información adicional sobre el usuario autenticado, como si es administrador.

#### **Autenticación**
- **Tipo:** Autenticación básica
- **Encabezados requeridos:**
  - `Authorization`: Debe contener las credenciales del usuario en formato básico (`username:password`).

#### **Parámetros de entrada**

El encabezado `Authorization` debe incluir:
- **username**: Nombre de usuario.
- **password**: Contraseña del usuario.

#### **Ejemplo de solicitud**

```bash
curl -X POST http://localhost:5000/login \
    -u username:password
