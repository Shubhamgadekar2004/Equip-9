from collections import deque

def find_shortest_path(n, edges, availability, start, target_equipment):
    graph = {}
    for a, b in edges:
        graph.setdefault(a, []).append(b)
    if target_equipment in availability.get(start, []):
        return [start]
    queue = deque([[start]])
    visited = set([start])
    while queue:
        path = queue.popleft()
        provider = path[-1]
        for neighbor in graph.get(provider, []):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if target_equipment in availability.get(neighbor, []):
                    return new_path
                queue.append(new_path)
                visited.add(neighbor)    
    return -1
def main():
    print("=== Equipment Rental Path Finder ===")    
    while True:
        try:
            n = int(input("Enter number of providers: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")    
    edges = []
    print("Enter connections (providerA providerB), type 'next' to finish:")
    while True:
        edge = input().strip()
        if edge.lower() == 'next':
            break
        try:
            edges.append(tuple(map(int, edge.split())))
        except ValueError:
            print("Invalid input. Please enter two space-separated integers.") 
    availability = {}
    print("Enter availability (provider equipment1,equipment2,...), type 'next' to finish:")
    while True:
        data = input().strip()
        if data.lower() == 'next':
            break
        parts = data.split()
        try:
            availability[int(parts[0])] = parts[1].split(',') if len(parts) > 1 else []
        except ValueError:
            print("Invalid input. Please enter provider ID followed by a comma-separated list of equipment.")    
    while True:
        try:
            start = int(input("Enter starting provider: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")    
    target_equipment = input("Enter target equipment: ").strip()    
    result = find_shortest_path(n, edges, availability, start, target_equipment)    
    if result == -1:
        print(f"No provider has {target_equipment} available.")
    else:
        print(f"Shortest path: {result}")
        print(f"Number of connections: {len(result) - 1}")
        print(f"Final provider: {result[-1]}")
if __name__ == "__main__":
    main()
