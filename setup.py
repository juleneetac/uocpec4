from setuptools import setup, find_packages


setup(
    name="pec4",
    version="0.1.0",
    author="Julen",
    author_email="jgarralaga@uoc.es",
    description="PEC4 de la asignatura Programación para la ciencia de datos",
    packages=find_packages(where="pec4"),
    data_files="/data",
    install_requires=[
        "arrow==1.3.0",
        "attrs==23.2.0",
        "binaryornot==0.4.4",
        "branca==0.7.2",
        "certifi==2024.6.2",
        "cffi==1.16.0",
        "chardet==5.2.0",
        "charset-normalizer==3.3.2",
        "click==8.1.7",
        "colorama==0.4.6",
        "ConfigUpdater==3.2",
        "contourpy==1.2.1",
        "coverage==7.5.3",
        "cycler==0.12.1",
        "exceptiongroup==1.2.1",
        "folium==0.16.0",
        "fonttools==4.53.0",
        "h11==0.14.0",
        "idna==3.7",
        "importlib_resources==6.4.0",
        "Jinja2==3.1.4",
        "kiwisolver==1.4.5",
        "markdown-it-py==3.0.0",
        "MarkupSafe==2.1.5",
        "matplotlib==3.9.0",
        "mdurl==0.1.2",
        "numpy==1.26.4",
        "outcome==1.3.0.post0",
        "packaging==24.1",
        "pandas==2.2.2",
        "pillow==10.3.0",
        "platformdirs==3.11.0",
        "pycparser==2.22",
        "Pygments==2.18.0",
        "pyparsing==3.1.2",
        "PySocks==1.7.1",
        "python-dateutil==2.9.0.post0",
        "python-slugify==8.0.4",
        "pytz==2024.1",
        "PyYAML==6.0.1",
        "requests==2.32.3",
        "rich==13.7.1",
        "selenium==4.21.0",
        "setuptools-scm==8.1.0",
        "six==1.16.0",
        "sniffio==1.3.1",
        "sortedcontainers==2.4.0",
        "text-unidecode==1.3",
        "tomli==2.0.1",
        "tomlkit==0.12.5",
        "trio==0.25.1",
        "trio-websocket==0.11.1",
        "types-python-dateutil==2.9.0.20240316",
        "typing_extensions==4.12.2",
        "tzdata==2024.1",
        "urllib3==2.2.1",
        "wsproto==1.2.0",
        "xyzservices==2024.6.0",
        "zipp==3.19.2"
    ],
)