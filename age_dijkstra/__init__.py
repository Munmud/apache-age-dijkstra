import psycopg2
import age
import sys
from . import VERSION

def version():
    return VERSION.VERSION

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''
        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

    def dijkstra_algorithm(graph, start_node):
        unvisited_nodes = list(graph.get_nodes())
    
        # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
        shortest_path = {}
    
        # We'll use this dict to save the shortest known path to a node found so far
        previous_nodes = {}
    
        # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
        max_value = sys.maxsize
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        # However, we initialize the starting node's value with 0   
        shortest_path[start_node] = 0
        
        # The algorithm executes until we visit all nodes
        while unvisited_nodes:
            # The code block below finds the node with the lowest score
            current_min_node = None
            for node in unvisited_nodes: # Iterate over the nodes
                if current_min_node == None:
                    current_min_node = node
                elif shortest_path[node] < shortest_path[current_min_node]:
                    current_min_node = node
                    
            # The code block below retrieves the current node's neighbors and updates their distances
            neighbors = graph.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    # We also update the best path to the current node
                    previous_nodes[neighbor] = current_min_node
    
            # After visiting its neighbors, we mark the node as "visited"
            unvisited_nodes.remove(current_min_node)
        
        return previous_nodes, shortest_path

    def print_shortest_path(previous_nodes, shortest_path, start_node, target_node):
        path = []
        node = target_node
        
        while node != start_node:
            path.append(node)
            node = previous_nodes[node]

        # Add the start node manually
        path.append(start_node)
        
        print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
        print(" -> ".join(reversed(path)))


class Age_Dijkstra:

    def __init__(self):
        self.connection = None
        self.graph_name = None


    def get_pg_version(self):
        """Get postgres version"""
        crsr = self.connection.cursor()
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        crsr.close()
        return db_version


    def connect(self,host="172.17.0.2", port="5432", dbname="postgres", user="postgres", password="agens", printMessage = False):
        """Connect with postgresql database"""
        try: 
            self.connection = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
            if (printMessage):
                print(self.get_pg_version())
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)


    def close_connection(self):
        """close connection with postgresql database"""
        if self.connection is not None:
            self.connection.close()
            self.connection = None


    def create_graph(self, graph_name):
        """create age db graph"""
        try :
            age.setUpAge(self.connection, graph_name)
            self.graph_name = graph_name
        except Exception as e:
            print(e)

    
    def delete_graph(self, graph_name = "None"):
        """delete age db graph"""
        if graph_name == "None" :
            graph_name = self.graph_name
        try :
            age.deleteGraph(self.connection, graph_name)
            self.graph_name = None
        except Exception as e:
            print(e)


    def dictToStr(self, property):
        p = "{"
        for x,y in property.items():
            p+= x + " : "
            p+= "'"
            p+= str(y)
            p+= "',"
        p = p.removesuffix(',')
        p+= "}"
        return p


    def extract_vertices(self, vertices):
        """returns from an agtype to python dict vertices"""
        tmp = {}
        tmp['label'] = vertices.label
        tmp['id'] = vertices.id
        for x in vertices.properties:
            tmp[x] = vertices[x]
        return tmp


    def extract_edge(self, edge):
        """returns from an agtype to python dict edge"""
        tmp = {}
        tmp['label'] = edge.label
        tmp['id'] = edge.id
        tmp['start_id'] = edge.start_id
        tmp['end_id'] = edge.end_id
        for x in edge.properties:
            tmp[x] = edge[x]
        return tmp


    def set_vertices(self,graph_name , label, property):
        """Add a vertices to the graph"""
        with self.connection.cursor() as cursor:

            query = """
            SELECT * from cypher(
                '%s', 
                $$ 
                    CREATE (v:%s %s) 
                    RETURN v
                $$
            ) as (v agtype); 
            """ % (graph_name, label,self.dictToStr(property))
            try :
                cursor.execute(query)
                for row in cursor:
                    return self.extract_vertices(row[0])
                        
                # When data inserted or updated, You must commit.
                self.connection.commit()
            except Exception as ex:
                print(type(ex), ex)
                # if exception occurs, you must rollback all transaction. 
                self.connection.rollback()


    def set_edge(self, graph_name, label1, prop1, label2, prop2, edge_label, edge_prop):
        with self.connection.cursor() as cursor:
            query ="""
            SELECT * from cypher(
                '%s', 
                $$ 
                    MATCH ( a:%s %s), (b:%s %s) 
                    CREATE (a)-[r:%s %s]->(b)
                $$) as (v agtype); 
            """ % (
                graph_name,label1,
                self.dictToStr(prop1), 
                label2, 
                self.dictToStr(prop2), 
                edge_label, 
                self.dictToStr(edge_prop)
            )
            try :
                cursor.execute(query)
                for row in cursor:
                    print("CREATED::", row[0])
                self.connection.commit()
            except Exception as ex:
                print(type(ex), ex)
                self.connection.rollback()


    def get_all_edge(self, graph_name = "None" ):
        if graph_name == "None" :
            graph_name = self.graph_name
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT * from cypher(
                        %s, 
                        $$ 
                            MATCH p=()-[]->() 
                            RETURN p 
                            LIMIT 10 
                        $$
                    ) as (v agtype); """, (graph_name,))
                res = []
                for row in cursor:
                    path = row[0]
                    tmp = {}
                    tmp['v1'] = self.extract_vertices(path[0])
                    tmp['e'] = self.extract_edge(path[1])
                    tmp['v2'] = self.extract_vertices(path[2])
                    # print(tmp)
                    res.append(tmp)
                return res

                    
        except Exception as ex:
            print(type(ex), ex)
            # if exception occurs, you must rollback even though just retrieving.
            self.connection.rollback()


    def get_all_vertices(self, graph_name = "None"):
        if graph_name == "None" :
            graph_name = self.graph_name
        res = []
        with self.connection.cursor() as cursor:
            try :
                cursor.execute(
                    """
                    SELECT * from cypher
                    (%s, 
                    $$ 
                        MATCH (n) 
                        RETURN n 
                    $$) 
                        as (v agtype); 
                    """, (graph_name,))
                for row in cursor:
                    vertices = self.extract_vertices(row[0])
                    res.append(vertices)
            except Exception as e:
                print(e)
        return res

         
__name__ = "apache-age-dijkstra"