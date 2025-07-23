# Hexagonal Architecture Application

Este proyecto es un ejemplo de una aplicación que sigue la arquitectura hexagonal. La arquitectura hexagonal, también conocida como Ports and Adapters, permite que la aplicación sea independiente de las tecnologías externas, facilitando la prueba y el mantenimiento.

## Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas:

- **src**: Contiene el código fuente de la aplicación.
  - **application**: Contiene los servicios que implementan la lógica de negocio.
  - **domain**: Define las entidades, repositorios y objetos de valor del dominio.
  - **infrastructure**: Implementa la lógica de persistencia y la configuración de la API.
  - **main.ts**: Punto de entrada de la aplicación.

## Instalación

Para instalar las dependencias del proyecto, ejecute el siguiente comando:

```
npm install
```

## Ejecución

Para ejecutar la aplicación, use el siguiente comando:

```
npm start
```

## Contribuciones

Las contribuciones son bienvenidas. Si desea contribuir, por favor abra un issue o envíe un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulte el archivo LICENSE para más detalles.