permits-data
==============================

ETL pipeline for construction permit data in Los Angeles county, USA using bash, Python and PostgreSQL.

## Built With
The pipeline is built on these frameworks and platforms:
* [psycopg2](https://pypi.org/project/psycopg2/)
* [pandas](https://pandas.pydata.org/)
* [Google Maps Platform](https://developers.google.com/maps/documentation) ([Geocoding API](https://developers.google.com/maps/documentation/geocoding/start))
* [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)
* [PostgreSQL](https://www.postgresql.org/)
* [Docker](https://docs.docker.com/get-docker/)
* [GNU Make](https://www.gnu.org/software/make/)

In addition to the above packages, I built a straight-forward Object-Relational Mapper (ORM) on top of psycopg2 to interface with PostgreSQL. The ORM package contains two classes, Database and Table, which contain the basic functionality
to run the pipeline. The package module is located in `src/toolkits/postgresql.py`.

## Pipeline Overview
The permits-data pipeline initializes a PostgreSQL database instance running inside a Docker container and loads raw construction permit data from a csv file. It then extracts, transforms and reloads the data to make it ready for analysis. 

Everything can be run with a single command `make data` which will execute these steps:
1) Start a PostgreSQL Docker container 
2) Load the raw data from csv
3) Standardize the column names
4) Update the data types
5) Concatenate address fields into a single column `full_address`
6) Geocode missing GPS coordinates using the `full_address`
7) Create separate columns for `latitude` and `longitude`
8) Update the database with the new values

## Getting Started

### Prerequisites
1) Install [Anaconda](https://docs.anaconda.com/anaconda/install/) package manager
2) Install [Docker](https://docs.docker.com/get-docker/)
3) Acquire an [API key for Google Maps](https://developers.google.com/maps/documentation/geocoding/get-api-key). It may be necessary to set up a developer account.
4) Check that the .env file is correct:
   ```
   ### .env

   # PostgreSQL
   REPO=permits-data
   CONTAINER=postgres_db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=password
   POSTGRES_DB=permits
   DB_HOST=localhost
   DB_PORT=5432
   DATA_URL='https://data.lacity.org/api/views/yv23-pmwf/rows.csv?accessType=DOWNLOAD'
   PG_URI="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${DB_HOST}:${DB_PORT}/shield"
   PGDATA="${PWD}/postgres/pgdata"
   DATA_DIR="${PWD}/data"

   # Google Maps API
   GOOGLE_API_KEY="<your api key>"
   GOOGLE_AGENT="permits-data" # or the GCP Project ID used when creating the API key
   ```

### Setting up Environment

Clone the directory:
```
git clone <repo>
```
To create the environment run:
```
make create_env
conda activate permits-data-env
```
Populate the environment variables by running:
```
set -o allexport; source .env; set +o allexport;
```

### Running the Pipeline

To run the entire pipeline start to finish:
```
make data
```

To load the database and run the pipeline from Jupyter Notebook
```
make data \
&& cd notebooks \
&& jupyter notebook ## Select pipeline notebook
```

