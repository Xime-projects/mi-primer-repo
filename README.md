# Sistema de Facturación en Python 

Este proyecto es una aplicación de consola interactiva que simula un carrito de compras y genera una factura final detallada con cálculo de impuestos.

---

## Descripción

El script permite a los usuarios visualizar un catálogo de 15 productos con sus respectivos precios. Los usuarios pueden seleccionar elementos mediante su índice numérico para agregarlos a un carrito virtual. Al finalizar la compra, el sistema calcula automáticamente:
* El subtotal de los productos adquiridos.
* El valor del IVA (19%).
* El total definitivo a pagar.

---

## Lenguaje Utilizado

* **Python 3.x** (Sin dependencias externas, utiliza únicamente la biblioteca estándar).

---

## Cómo Ejecutar el Proyecto

Sigue estos pasos para correr la aplicación en tu computadora:

1. **Clonar o descargar el archivo:** Asegúrate de tener el archivo `factura.py` en una carpeta de tu sistema.
2. **Abrir la terminal:** Entra a la consola de comandos (Terminal, CMD o PowerShell) y navega hasta la carpeta del archivo.
3. **Ejecutar el script:** Escribe el siguiente comando y presiona `Enter`:
   ```bash
   python factura.py
   ```

---

## Autor

* **Tu Nombre / Nombre de Usuario** - *Desarrollador Principal* - [Tu GitHub](https://github.com)

---

## Investigación sobre Archivos README.md

A continuación, se detalla la investigación requerida sobre la documentación de proyectos de software.

### 1. ¿Qué es un README.md?
Un archivo `README.md` es la **carta de presentación** de un proyecto de software. Es el primer archivo que leen los usuarios o desarrolladores cuando entran a un repositorio. Su objetivo es explicar de forma rápida y clara qué hace el proyecto, por qué es útil, cómo instalarlo y cómo usarlo.

### 2. ¿Qué secciones debe tener?
Un README profesional varía según la complejidad del proyecto, pero generalmente incluye:
* **Título y Descripción:** Nombre del software y su propósito general.
* **Requisitos Previos:** Herramientas o programas necesarios antes de la instalación.
* **Instalación:** Comandos precisos para configurar el entorno de ejecución.
* **Uso/Ejemplos:** Instrucciones o fragmentos de código que demuestran cómo funciona.
* **Contribución:** Reglas para que otros desarrolladores ayuden a mejorar el código.
* **Licencia:** Los derechos legales de uso (por ejemplo, MIT, Apache).

### 3. ¿Qué es Markdown y cómo se usa?
**Markdown** es un lenguaje de marcado ligero que permite aplicar formato a un texto plano de manera sencilla, utilizando caracteres especiales que luego se convierten a código HTML de forma visual. 

A continuación se muestra cómo aplicar sus componentes principales:

#### Títulos
Se crean utilizando el símbolo de numeral (`#`) antes del texto. La cantidad de numerales define el nivel del título:
```markdown
# Título Principal (H1)
## Subtítulo (H2)
### Sección Menor (H3)
```

#### Listas
* **Listas desordenadas (viñetas):** Se utiliza un asterisco (`*`), un guion (`-`) o un signo de más (`+`) seguido de un espacio.
* **Listas ordenadas:** Se coloca el número seguido de un punto y un espacio (`1. `, `2. `).
```markdown
* Elemento A
* Elemento B

1. Primer paso
2. Segundo paso
```

#### Enlaces
Para insertar un hipervínculo, se coloca el texto visible entre corchetes `[ ]` y la URL de destino inmediatamente después entre paréntesis `( )`.
```markdown
[Visita GitHub](https://github.com)
```

#### Imágenes
Su sintaxis es idéntica a la de los enlaces, pero se antepone un signo de exclamación `!`. El texto entre corchetes actúa como el texto alternativo (alt) en caso de que la imagen no cargue.
```markdown
![Texto alternativo de la imagen](https://url-de-la-imagen.com)
```

