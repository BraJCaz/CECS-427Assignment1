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

#
