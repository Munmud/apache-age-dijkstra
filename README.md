# Implement Shortest Path (Dijkstra) with Apache AGE

[Apache AGE](https://age.apache.org/) is a PostgreSQL extension that provides graph database functionality. The goal of the Apache AGE project is to create single storage that can handle both relational and graph model data so that users can use standard ANSI SQL along with openCypher, the Graph query language. This repository hosts the development of the Python driver for this Apache extension (currently in Incubator status). Thanks for checking it out.

Apache AGE is:

- **Powerful** -- AGE adds graph database support to the already popular PostgreSQL database: PostgreSQL is used by organizations including Apple, Spotify, and NASA.
- **Flexible** -- AGE allows you to perform openCypher queries, which make complex queries much easier to write.
- **Intelligent** -- AGE allows you to perform graph queries that are the basis for many next level web services such as fraud & intrustion detection, master data management, product recommendations, identity and relationship management, experience personalization, knowledge management and more.

### Features
* Shortest Path implemented using dijkstra algorithm
* Used Apache AGE graph database

## Installation

### Requirements
* Python 3.9 or higher
* This module runs on [psycopg2](https://www.psycopg.org/) and [antlr4-python3](https://pypi.org/project/antlr4-python3-runtime/)

```cmd
sudo apt-get update
sudo apt-get install python3-dev libpq-dev
pip install --no-binary :all: psycopg2
```

### Install via PIP
```cmd
pip install apache-age-dijkstra
pip install antlr4-python3-runtime==4.9.3
```

### Build from Source
```cmd
git clone https://github.com/Munmud/apache-age-dijkstra
cd apache-age-python
python setup.py install
```

### View Samples
- [Shortest Distance between cities](https://github.com/Munmud/apache-age-dijkstra/blob/master/samples/sample1.py)

## Instruction

### Import
```py
from age_dijkstra import Age_Dijkstra
```

### Making connection to postgresql (when using [this docker reepository](https://github.com/Munmud/apache_age))
```py
con = Age_Dijkstra()
con.connect(
    host="localhost",       # default is "172.17.0.2" 
    port="5430",            # default is "5432"
    dbname="postgresDB",    # default is "postgres"
    user="postgresUser",    # default is "postgres"
    password="postgresPW",  # default is "agens"
    printMessage = True     # default is False
)
```

### Get all edges
```py
edges = con.get_all_edge()
```
- structure : 
`
{
    v1 : start_vertex, 
    v2 : end_vertex,
    e : edge_object
}
`

### Get all vertices
```py
nodes = []
for x in con.get_all_vertices():
    nodes.append(x['property_name'])
```

### Create adjacent matrices using edges
```py
init_graph = {}
for node in nodes:
    init_graph[node] = {}
for edge in edges :
    v1 = edge['v1']['vertices_property_name']
    v2 = edge['v2']['vertices_property_name']
    dist = int(edge['e']['edge_property_name'])
    init_graph
    init_graph[v1][v2] = dist
```

### Initialized Graph
```py
from age_dijkstra import  Graph
graph = Graph(nodes, init_graph)
```

### Use dijkstra Algorithm
```py
previous_nodes, shortest_path = Graph.dijkstra_algorithm(graph=graph, start_node="vertices_property_name")
```

### Print shortest Path
```py
Graph.print_shortest_path(previous_nodes, shortest_path, start_node="vertices_property_name", target_node="vertices_property_name")
```

### Create Vertices
```py
con.set_vertices(
    graph_name = "graph_name", 
    label="label_name", 
    property={"key1" : "val1",}
    )
```

### Create Edge
```py
con.set_edge( 
    graph_name = "graph_name", 
    label1="label_name1", 
    prop1={"key1" : "val1",}, 
    label2="label_name2", 
    prop2={"key1" : "val1",}, 
    edge_label = "Relation_name", 
    edge_prop = {"relation_property_name":"relation_property_value"}
)
```

### For more information about [Apache AGE](https://age.apache.org/)
* Apache Incubator Age: https://age.apache.org/
* Github: https://github.com/apache/incubator-age
* Documentation: https://age.incubator.apache.org/docs/
* apache-age-dijkstra GitHub: https://github.com/Munmud/apache-age-dijkstra
* apache-age-python GitHub: https://github.com/rhizome-ai/apache-age-python

### License
[Apache-2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
