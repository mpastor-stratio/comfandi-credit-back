# Crédito Web
Este proyecto contiene el código desarrollado con el framework de flask en Python para el backend, y HTML, CSS y JavaScript para el Front-End de la página web. 
La necesidad de este proyecto surge al conocer que el área de crédito dispone archivos excel para sus terceros con información sensible y para mitigar este riesgo, se les propone realizar una página web donde a futuro dispondrán de diferentes aplicativos para el área. El aplicativo inicial presenta el resultado de algo denominado "Listas Restrictivas", donde tendrán dos buscadores uno para los titulares del crédito (donde buscarán si el titular está habilitado para crédito en comfandi o no) y otro buscador para el deudor solidario ( persona que en caso que el titular no pague el crédito, responderá) también en este último caso, se buscará si el deudor está habilitado para crédito comfandi o no.

Se busca que las personas ingresen con un Login por medio de usuario y contraseña que serán administradas por el administrador de la herramienta. y que manejará un mínimo de 15 caractéres entre los que tiene que existir mayúsculas, minúsculas, números y caracteres especiales.

Existen tres perfiles de usuario, un perfil administrador que a parte del módulo de Listas restrictivas, posee acceso para crear usuarios.

La información de los usuarios y de las listas restrictivas, se encuentran en la base de datos postgres de la plataforma. Se accede mediante usuario y certificados. Sería interesante poder gestionar esta conexión utilizando la captura de los certificados de conexión a la base de datos mediante vault. 

Adicionalmente, se han solicitado añadir un nuevo módulo a la página y solventar temas de seguridad de la página:

En esta segunda iteración se ha definido lo siguiente:

**Objetivo**: Realizar una segunda iteración del desarrollo que permita identificar las razones de
rechazo de los afiliados y mejore la experiencia de los usuarios en el momento del ingreso al
aplicativo.

**Objetivo específico**:
- Entregar una herramienta para el seguimiento de los afiliados evaluados que marque
el motivo de su rechazo. (Cuadro que permita visualizar las reglas establecidas y
marque el cumplimiento o no de las mismas).
- Mejorar las condiciones de logueo del aplicativo actual

**Tareas de desarrollo web**
Enlistar las tareas necesarias para obtener las siguientes mejoras en el aplicativo actual:
- Recuperación de contraseña.
- Eliminar usuarios asignados. (Opción para eliminar Usuarios)
- Editar usuarios creados. (Opción para editar usuarios creados)

Adicionalmente, con respecto a los temas de seguridad han saltado las siguientes alertas:

| Nombre                                               | Nivel de Riesgo |
| ---------------------------------------------------- | --------------- |
| SQL Injection                                        | Alta            |
| CSP: Wildcard Directive                              | Medio           |
| CSP: script-src unsafe-inline                        | Medio           |
| CSP: style-src unsafe-inline                         | Medio           |
| Content Security Policy (CSP) Header Not Set          | Medio           |
| Missing Anti-clickjacking Header                     | Medio           |
| CSP: Notices                                         | Bajo            |
| Cookie Without Secure Flag                            | Bajo            |
| Cookie without SameSite Attribute                     | Bajo            |
| Cross-Domain JavaScript Source File Inclusion         | Bajo            |
| Strict-Transport-Security Header Not Set              | Bajo            |
| X-Content-Type-Options Header Missing                 | Bajo            |


De igual forma cualquier duda o inquietud al respecto contactar a jcuevas@stratio.com 


