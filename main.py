from MSCS532_ProjectPhase1_Deliverable1 import graph, hashTable, priorityQueue

# Example usage of the hash table
user_preferences = hashTable()
user_preferences.insert('user1', {'product1': 5, 'product2': 3})

# Example usage of the graph
product_graph = graph()
product_graph.add_edge('product1', 'product2', 0.9)

# Example usage of the priority queue
pq = priorityQueue()
pq.push('product1', 5)
pq.push('product2', 3)

while not pq.is_empty():
    print(pq.pop())
