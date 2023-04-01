#Inisialisasi variabel graph sebagai dictionary yang berisi node dan neighbor-nya 

graph = {
    'A': ['Z', 'S', 'T'],
    'Z': ['O'],
    'O': ['S1'],
    'S1': ['F', 'R'],
    'F': ['B'],
    'B': [],
    'R': [],
    'S': ['O1', 'F1', 'R1'],
    'O1': [],
    'F1': ['B1'],
    'B1': [],
    'R1': ['C', 'P'],
    'C': [],
    'P': [],
    'T': ['L'],
    'L': ['M'],
    'M': ['D'],
    'D': []
}

#Inisialisasi variabel visited sebagai set untuk menyimpan data node yang sudah dikunjungi
visited = set()  

#Fungsi dfs untuk melakukan pencarian Depth First Search dengan parameter visited, graph, dan node
def dfs(visited, graph, node):
    #Jika node belum pernah dikunjungi, maka cetak node tersebut
    if node not in visited:
        print(node)
        #Tandai node yang telah dikunjungi
        visited.add(node)
        #Lakukan looping untuk mengakses semua neighbor dari node tersebut
        for neighbour in graph[node]:
            #Lakukan rekursif untuk mengakses neighbor dari node tersebut
            dfs(visited, graph, neighbour)

#Cetak "Depth First Search" 
print("Depth First Search")

#Panggil fungsi dfs dengan parameter visited, graph, dan node awal 'A'
dfs(visited, graph, 'A')

# Kodingan di atas merupakan implementasi dari algoritma Depth First Search (DFS). Algoritma ini digunakan untuk mencari jalur terpendek antara node awal dan tujuan. Kodingan di atas memiliki 2 variabel yaitu graph dan visited. Variabel graph berisi dictionary yang menyimpan node dan neighbor-nya. Sedangkan variabel visited digunakan untuk menyimpan data node yang sudah dikunjungi. Pada kodingan ini, fungsi dfs dipanggil dengan parameter visited, graph, dan node awal 'A'. Fungsi dfs akan melakukan pencarian Depth First Search dengan memeriksa node yang belum pernah dikunjungi, lalu menandai node tersebut sebagai node yang telah dikunjungi. Setelah itu, looping dilakukan untuk mengakses semua neighbor dari node tersebut, dan rekursif untuk mengakses neighbor dari node