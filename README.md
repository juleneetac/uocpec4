# Programación para la ciencia de datos - PEC4

El objetivo de este ejercicio será desarrollar un paquete de Python fuera del entorno de Notebooks, que nos permita resolver el problema dado. Trabajaréis en archivos Python planos .py. Éste tendrá que incluir el correspondiente código organizado lógicamente (separado por módulos, organizados por funcionalidad,...), la documentación del código (docstrings) y tests. Además, tendréis que incluir los correspondientes archivos de documentación de alto nivel (README) así como los archivos de licencia y dependencias (requirements.txt) comentados en la teoría.

Para la realización de esta práctiva se ha usado Visual Studio Code en mi máquina host Windows

# Instalación

**Creación del entorno virtual**

En la terminald el proyecto se deberá poner el siguiente comando:

```shell
python -m venv venvpec4
```

**Activación del entorno virtual**
```shell
venvpec4\Scripts\activate 
```

**Instalar requirements**
```shell
pip install -r requirements.txt
```

# Instrucciones para el Run

**Ejecución del main en 1 step**
```shell
python pec4/main.py
```

o

```shell
python pec4/main.py --f all
```

**Ejecución de cada ejercicio uno a uno**

Para este caso, se podrá ejecutar cada ejercicio individualmente añadiendo un argumento, pero en muchos casos será necesario ejecutar
el ejercicio anterior para un funcionamiento correcto, puesto que hay dependencias de ejercicios anteriores.

| Ejercicio | Argumento |
| ------ | ------ |
| ejercicio 1 | --f ex1 |
| ejercicio 2 | --f ex2 |
| ejercicio 3 | --f ex3 |
| ejercicio 4 | --f ex4 |
| ejercicio 5 | --f ex5 |
| ejercicio 6 | --f ex6 |

Ejemplo:

```shell
python pec4/main.py --f ex6
```

**Nota:** Es importante usar "python" y no "python3" ya que sinó la librería folium no funcionará.

# Ver los mapas interactivos en html

Para ver los mapas generados en el ejercicio 6 de forma interactiva, se aconseja visitar
la web [HTML Online Editor](https://onecompiler.com/html/) y pegar el código html guardado en 
la carpeta data.