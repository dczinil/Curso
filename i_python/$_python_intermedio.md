# Python Intermedio

## Zen de python
* Bello es mejor que feo.
* Explícito es mejor que implícito.
* Simple es mejo que complicado.
* Complejo es mejor que complicado.
* Plano es mejor que anidado.
* Espaciado es mejor que denso.
* La legibilidad es importante.
* Los casos especiales no son lo suficientemente especiales como para romper las reglas.
* Sin embargo, la practicidad le gana a la pireza.
* Los errores nunca deberían pasar silenciosamente.
* A menos que se silencien explícitamente.
* Frente a la ambugüedad, evitar la tentación de adivinar.
* Debería haber una, y preferible solo una, maneraobvia de hacerlo.
* A pesar de que esa manera no sea obvia a menos que seas Holandés.
* Ahora es mejor que nunca.
* a Pesar de que nunfa es muchas veces mejor que *ahora* mismo.
* Si la implementación es difícil de explicar, es una mala idea.
* Si la implementación es dácil de explicar, puede que sea una buena idea.
* Los espacios de nombre son una gran idea, ¡tengamos más de esos!


### PEP
Los PEP son los qu enos dicen como funciona el lenguaje y como deberíamos de usar lo.

### Modulo
Es codigo ya realizado por otros desarrolladores para poder implementar en tu implementación.

### Entorno virtual
Es una versión de python para un solo proyecto. Y esta pensado para quesolo funcione para ese proyecto que tiene sus propios modulos.<br>

*   Es un flag "-m" que indica que se va a llamar un modulo,
*   Es el nombre más avitual para las carpetas de los modulos de virtualizaciónes "venv".

```
py -m  venv venv
```
Windows
```
.\venv\Scripts\activate
```
Linux
```
source venv/bin/active
```
### PIP
Hay modolulos que no estan en python cuando los instalamos, por lo hay que instala los de forma externa, por lo que utilizamos "Package Installer for Puython -> PIP", algunos de los modulos que podemos instalar son;

````
Requests            ->  Web Scraping
BeautifulSoup4      ->  Web Scraping
Pandas              -> Ciencia de datos
Numpy               -> Ciencia de datos
Pytest              -> developers test
````
Se sugiere estar en venv para poder instalar nuevos modulos.

Instalar un modulo, ejemplo pandas.
````
pip install pandas
Collecting pandas
  Downloading pandas-1.4.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.7 MB)
     |████████████████████████████████| 11.7 MB 2.5 MB/s
Collecting pytz>=2020.1
  Downloading pytz-2022.1-py2.py3-none-any.whl (503 kB)
     |████████████████████████████████| 503 kB 18.1 MB/s
Collecting numpy>=1.21.0
  Downloading numpy-1.22.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
     |████████████████████████████████| 16.8 MB 25.3 MB/s
Collecting python-dateutil>=2.8.1
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     |████████████████████████████████| 247 kB 33.0 MB/s
Collecting six>=1.5
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, pytz, python-dateutil, numpy, pandas
Successfully installed numpy-1.22.3 pandas-1.4.2 python-dateutil-2.8.2 pytz-2022.1 six-1.16.0
````
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;Puede resaltar que se estan isntalando otros modulos esto es porque "pandas" es un modulo complejo con varias dependencias.

Lista los modulos que tienes instalados.<br>

````
pip3 freeze
numpy==1.22.3
pandas==1.4.2
python-dateutil==2.8.2
pytz==2022.1
six==1.16.0
````
Para mandar las dependencias a un archivo que se pueda compartir en las nubes de git (GitHub, GitLab, Bitbucket).

````
pip freeze > requirements.txt
````
Para poder instalar las dependecias de otros proyectos con este mismo archivo se usa.
````
pip install -r requirements.txt
````
Aparte de pip hay otros instaladores de dependencias en python.

## Los primeros pasos para iniciar un proyecto de desarrollo.
Se genera la carpeta del proyecto o desarrollo.<br>

    mkdir "Nombre de la carpeta haciendo alución al desarrollo"

Se abre el editor de codigo "Visual Studio Code".<br>

    code .


Dentro de la carpeta del desarrollo se iniciar "git".<br>

    git init

Se fgenera un entornovirtual de python dentro de la carpeta de desarrollo.<br>

    python3 -m venv venv

Se agrega el archivo ".gitignore" y se le agrega el entorno virtual.<br>

    touch .gitignore && echo venv/ > .gitignore
