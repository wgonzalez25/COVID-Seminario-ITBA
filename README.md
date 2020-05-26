# COVID/South America Seminario ITBA

El siguiente trabajo práctico se basa en el análisis de la situación de Suramérica con respecto al impacto del Coronavirus COVID 19.

El flujo de trabajo utilizado fue el siguiente:
1. Creación de la máquina Ubuntu 18.04 en AWS con una Memoria RAM de 16 Gb y 4 vCPU, y con disco de 30 Gb.
2. Instalación de los siguientes software:
    - Docker en Ubuntu.
    - Docker Compose.
    - Anaconda3.
    - Jupyter Notebook.
    - Postgres SQL.
    - Apache Superset utilizando la opción de docker (https://github.com/apache/incubator-superset/blob/master/docker/README.md)
    - Airflow.
3. Fuente de información proveniente del Repositorio COVID-19 por el "Center for Systems Science and Engineering (CSSE)" de Johns Hopkins University que se actualiza diariamente para todo los paises (https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports).
4. El proceso ETL (Extracción, Transformación, y Carga) se desarrollo en Python dentro del Jupyter Notebook de la máquina AWS, realizando la descarga de los archivos .csv (diarios), transformando parte de los datos utilizando data frame, y subiendo los datos en Tablas Postgres SQL. Finalmente, se realizaron tratamientos adicionales de los datos a través de comandos de SQL desde Jupyter Notebook.
5. Para la visualización de la información se utilizó el Apache Superset a través de un Dashboard conteniendo diferentes "pages" para los Casos Confirmados, Muertes, Recuperados, Activos y Mapa de COVID 19 en Suramérica.


<a href="https://ibb.co/YdWbvVr"><img src="https://i.ibb.co/6tZN6qd/covid-2020-05-26-T22-18-37-354-Z.jpg" alt="covid-2020-05-26-T22-18-37-354-Z" border="0"></a>
