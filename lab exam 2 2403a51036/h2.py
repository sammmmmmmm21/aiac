import heapq

def dijkstra(graph, source):
    # Step 1: Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    visited = set()
    heap = [(0, source)]  # (distance, node)

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)

        # Step 2: Edge relaxation for neighbors
        for neighbor, weight in graph[current_node].items():
            if neighbor in visited:
                continue
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return distances

# Example usage:
if __name__ == "__main__":
    graph = {'A': {'B': 1, 'C': 4},
             'B': {'C': 2, 'D': 5},
             'C': {'D': 1},
             'D': {}}
    print(dijkstra(graph, 'A'))