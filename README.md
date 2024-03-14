# Plantilla de Proyecto para Investigación en Computación Cognitiva e Inteligencia Artificial

¡Bienvenido a la Plantilla de Proyecto para Investigación en Computación Cognitiva e Inteligencia Artificial!

Esta plantilla proporciona una estructura básica para comenzar proyectos de investigación en el campo de la Computación Cognitiva e Inteligencia Artificial. Utiliza esta plantilla como punto de partida para tus proyectos, adaptándola según las necesidades específicas de tu investigación.

## Pre Requisitos
- Python 3.9+
- Astral UV

## Contenido

- README.md: Este archivo proporciona una descripción general del proyecto y cómo comenzar a trabajar en él.
- requirements.txt: Un archivo que lista las dependencias del proyecto, incluyendo bibliotecas de Python u otros recursos necesarios para ejecutar el código.
- src/: Un directorio que contiene el código fuente principal del proyecto.
- docs/: Un directorio para la documentación del proyecto, que puede incluir especificaciones, manuales de usuario, informes técnicos, etc.


## Cómo utilizar esta plantilla
1. Clona este repositorio: Utiliza el comando git clone para clonar este repositorio en tu máquina local:
```bash
git clone https://github.com/tu-usuario/plantilla-proyecto-ia.git
```

2. Instala Cookiecutter (si no lo has hecho): Si aún no tienes Cookiecutter instalado, puedes hacerlo mediante pip:
```bash
pip install cookiecutter
```
3. Genera un nuevo proyecto: Ejecuta Cookiecutter y proporciona la ruta al repositorio de esta plantilla:
```bash
cookiecutter ruta/al/template
```

4. Crea el ambiente virtual para el proyecto con Astral UV
```bash
uv venv .venv-<nombre-proyecto>
```

5. Instala las dependencias: Utiliza el archivo requirements.txt para instalar las dependencias del proyecto. Ejecuta el siguiente comando en tu entorno virtual de Python:

```bash
pip install -r requirements.txt
```

6. Personaliza el proyecto: Haz los cambios necesarios en los archivos para adaptar el proyecto a tus necesidades específicas. Esto puede incluir la actualización del README, la modificación del código fuente, la personalización de la documentación, etc.


7. Comienza a trabajar: ¡Ahora estás listo para comenzar a trabajar en tu proyecto! Utiliza el código fuente proporcionado como punto de partida y desarrolla tu investigación en Computación Cognitiva e Inteligencia Artificial.