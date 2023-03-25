# Implementasi algoritma Dijkstra untuk mencari shortest-path

## Deskripsi
Pemerintah kota ingin mengoptimalkan jaringan transportasi di wilayahnya dengan cara memastikan bahwa setiap kendaraan dapat mencapai tujuan mereka dengan cara yang efisien. Pemerintah memiliki data mengenai jumlah kendaraan, kapasitas jalan, dan arus lalu lintas pada waktu tertentu. Tujuan utama adalah mengatur arus kendaraan untuk meminimalkan waktu perjalanan dan biaya transportasi. Masalah ini dapat diselesaikan dengan menggunakan algoritma teori graf seperti algoritma Bellman-Ford atau Dijkstra untuk mencari jalur terpendek antara dua titik, dan algoritma Ford-Fulkerson untuk memaksimalkan aliran melalui jaringan transportasi.

## Spesifikasi
- Directed.
- Weighted.
- Kemungkinan Dense.
- Karakteristik masalah sesuai dengan tipe: Network Flow.

## Contoh kode Python
```python
# Definisikan graf
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 4},
    'C': {'B': 2, 'D': 1},
    'D': {'A': 1, 'G': 2},
    'E': {'D': 1, 'G': 3},
    'F': {'E': 2, 'H': 1},
    'G': {'H': 2},
    'H': {}
}

# Definisikan fungsi Dijkstra
def dijkstra(graph, start, end):
    # Inisialisasi jarak ke semua node dengan nilai tak hingga
    distances = {node: float('inf') for node in graph}
    # Jarak dari start node ke start node adalah 0
    distances[start] = 0
    # Inisialisasi set node yang belum dikunjungi
    unvisited_nodes = graph.copy()
    # Inisialisasi set node yang telah dikunjungi
    visited_nodes = {}
    # Loop sampai semua node telah dikunjungi
    while unvisited_nodes:
        # Cari node dengan jarak terpendek dari start node
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        # Update jarak ke node tetangga
        for neighbor, distance in graph[current_node].items():
            if neighbor not in unvisited_nodes:
                continue
            new_distance = distances[current_node] + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
        # Tandai current node sebagai telah dikunjungi
        visited_nodes[current_node] = distances[current_node]
        del unvisited_nodes[current_node]
        # Jika current node adalah end node, keluar dari loop
        if current_node == end:
            break
    return visited_nodes

# Contoh penggunaan
start = 'A'
end = 'G'
print(dijkstra(graph, start, end))
```

## Output
Output dari kode di atas, jika dijalankan dengan parameter start='A' dan end='G', akan menghasilkan output sebagai berikut:
```
{'A': 0, 'C': 3, 'B': 5, 'D': 4, 'G': 6}
```
Output tersebut menunjukkan jarak terpendek dari node start (A) ke setiap node lain di dalam graf, termasuk jarak terpendek dari node start ke node end (G).