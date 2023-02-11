from age_dijkstra import Age_Dijkstra, Graph

con = Age_Dijkstra()
con.connect(
    host="localhost",       # default is "172.17.0.2" 
    port="5430",            # default is "5432"
    dbname="postgresDB",    # default is "postgres"
    user="postgresUser",    # default is "postgres"
    password="postgresPW",  # default is "agens"
    printMessage = True     # default is False
)

con.create_graph( graph_name = "munmud_graph")

con.set_vertices(
    graph_name = "munmud_graph", 
    label="Country", 
    property={"name" : "Dhaka",}
    )
con.set_vertices(
    graph_name = "munmud_graph", 
    label="Country", 
    property={"name" : "Rajshahi",}
    )
con.set_vertices(
    graph_name = "munmud_graph", 
    label="Country", 
    property={"name" : "Sylhet",}
    )
con.set_vertices(
    graph_name = "munmud_graph", 
    label="Country", 
    property={"name" : "Chittagong",}
    )

con.set_edge( 
    graph_name = "munmud_graph", 
    label1="Country", 
    prop1={"name" : "Dhaka",}, 
    label2="Country", 
    prop2={"name" : "Rajshahi"}, 
    edge_label = "Neighbour", 
    edge_prop = {"distance":"5"}
)
con.set_edge( 
    graph_name = "munmud_graph", 
    label1="Country", 
    prop1={"name" : "Dhaka",}, 
    label2="Country", 
    prop2={"name" : "Sylhet"}, 
    edge_label = "Neighbour", 
    edge_prop = {"distance":"2"}
)
con.set_edge( 
    graph_name = "munmud_graph", 
    label1="Country", 
    prop1={"name" : "Sylhet",}, 
    label2="Country", 
    prop2={"name" : "Rajshahi"}, 
    edge_label = "Neighbour", 
    edge_prop = {"distance":"2"}
)
con.set_edge( 
    graph_name = "munmud_graph", 
    label1="Country", 
    prop1={"name" : "Dhaka",}, 
    label2="Country", 
    prop2={"name" : "Chittagong"}, 
    edge_label = "Neighbour", 
    edge_prop = {"distance":"6"}
)
con.set_edge( 
    graph_name = "munmud_graph", 
    label1="Country", 
    prop1={"name" : "Rajshahi",}, 
    label2="Country", 
    prop2={"name" : "Chittagong"}, 
    edge_label = "Neighbour", 
    edge_prop = {"distance":"1"}
)
con.set_edge( 
    graph_name = "munmud_graph", 
    label1="Country", 
    prop1={"name" : "Sylhet",}, 
    label2="Country", 
    prop2={"name" : "Chittagong"}, 
    edge_label = "Neighbour", 
    edge_prop = {"distance":"4"}
)

edges = con.get_all_edge()
nodes = []
for x in con.get_all_vertices():
    nodes.append(x['name'])

init_graph = {}
for node in nodes:
    init_graph[node] = {}
    
for edge in edges :
    v1 = edge['v1']['name']
    v2 = edge['v2']['name']
    dist = int(edge['e']['distance'])
    init_graph
    init_graph[v1][v2] = dist

graph = Graph(nodes, init_graph)
previous_nodes, shortest_path = Graph.dijkstra_algorithm(graph=graph, start_node="Dhaka")
Graph.print_shortest_path(previous_nodes, shortest_path, start_node="Dhaka", target_node="Chittagong")

con.delete_graph( graph_name = "munmud_graph")
con.close_connection()
