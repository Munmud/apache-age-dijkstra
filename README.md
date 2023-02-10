# Shortest Path (Dijkstra) : Apache AGE Python Driver

[Apache AGE](https://age.apache.org/) is a PostgreSQL extension that provides graph database functionality. The goal of the Apache AGE project is to create single storage that can handle both relational and graph model data so that users can use standard ANSI SQL along with openCypher, the Graph query language. This repository hosts the development of the Python driver for this Apache extension (currently in Incubator status). Thanks for checking it out.

A graph consists of a set of vertices (also called nodes) and edges, where each individual vertex and edge possesses a map of properties. A vertex is the basic object of a graph, that can exist independently of everything else in the graph. An edge creates a directed connection between two vertices. A graph database is simply composed of vertices and edges. This type of database is useful when the meaning is in the relationships between the data. Relational databases can easily handle direct relationships, but indirect relationships are more difficult to deal with in relational databases. A graph database stores relationship information as a first-class entity. Apache AGE gives you the best of both worlds, simultaneously.

Apache AGE is:

- **Powerful** -- AGE adds graph database support to the already popular PostgreSQL database: PostgreSQL is used by organizations including Apple, Spotify, and NASA.
- **Flexible** -- AGE allows you to perform openCypher queries, which make complex queries much easier to write.
- **Intelligent** -- AGE allows you to perform graph queries that are the basis for many next level web services such as fraud & intrustion detection, master data management, product recommendations, identity and relationship management, experience personalization, knowledge management and more.

### Features
* Cypher query support for Psycopg2 PostreSQL driver (enables cypher queries directly)
* Deserialize AGE result (AGType) to Vertex, Edge, Path
* Shortest Path dijkstra algorithm implemented

### Requirements
* Python 3.9 or higher
* This module runs on [psycopg2](https://www.psycopg.org/) and [antlr4-python3](https://pypi.org/project/antlr4-python3-runtime/)

```cmd
sudo apt-get update
sudo apt-get install python3-dev libpq-dev
pip install --no-binary :all: psycopg2
pip install antlr4-python3-runtime==4.11.1
```

### Install via PIP
```cmd
pip install apache-age-dijkstra 
```

### Build from Source
```cmd
git clone https://github.com/rhizome-ai/apache-age-python
cd apache-age-python
python setup.py install
```

### import
```
from age_dijkstra import Age_Dijkstra
```

### Making connection to postgresql (when using [docker reepository](https://github.com/Munmud/apache_age))
```cmd
con = Age_Dijkstra(host="localhost", port="5430", dbname="postgresDB", user="postgresUser", password="postgresPW",printMessage = True)
```


### For more information about [Apache AGE](https://age.apache.org/)
* Apache Incubator Age: https://age.apache.org/
* Github: https://github.com/apache/incubator-age
* Documentation: https://age.incubator.apache.org/docs/
* apache-age-python GitHub: https://github.com/rhizome-ai/apache-age-python

### License
[Apache-2.0 License](https://www.apache.org/licenses/LICENSE-2.0)