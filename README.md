# Brandon Cazares
# CECS-427 Section 1 
# Assignment #1 Graphs

Objective 
# In this assignment, we're going to write a Python program based on graphs to understand how they work because we need to implement Erdos-Renyi graphs. 
# We'll use both NetworkX and matplotlib to generate graphs, store those in a file, read graphs from a file, compute all shortest paths from a specified node using graph algorithms and visualize them by using shortest paths. 

Requirement 
# We need to use this command to excute the graph.py file located in the current directory, because it either reads the file graph_file.gml or creates a random graph. 
# We need to know that the graph_file.gml or the created graph is the graph used for analysis because the format is Graph Modeling Language (GML) which desribes the graph's structure based on attributes. 
python ./graph.py --input graph_file.gml --create_random_graph n c --plot --BFS a --output out_graph_file.gml
# The program should read the attributes of both the nodes and edges in a file. 

Description of Parameters
# We must also understand that the script graph.py must be located in the current directory because it ensures a robust file handling mechanisms such as checking errors, file existence validation and approriate error messages. 
# This parameter graph_file.gml describes the graph's structure because it has attributes to read from the graph data. This parameter requires us to provide initial graph data for either analysis or modification. 

-- create_random_graph n c 
# This indicates that a new graph should be created because this parameter overrides the use of the provided input file when it generates a graph based on the subsequent parameters (--nodes and --constant). This relabels nodes as strings because the node of node 0 is "0", "1" and so on. 
# This parameter n defines the number of nodes to be included in the formula (c ln n) / n where we finally get our number of nodes. 

-- BFS a
# This specifies a node (a) to compute all the shortest paths (BFS). When we use this parameter, we need to both calculate and display the shortest path distances involving the special node.
-- plot 
# This requests all graphs to be plotted. This parameter also triggers the graph's visualization, which includes both edges and plotting nodes. 
-- output out_graph_file.gml 

# This defines the file (out_graph_file.gml) where the resulting graph should be saved. This parameter is used to save the modified or newly created graph to a specified file in the Graph Modeling Language (.gml) format. 


