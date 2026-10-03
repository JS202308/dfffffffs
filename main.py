import json
import csv
import sys


def load_graph(filename):
    if filename.lower().endswith(".json"):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)

        graph = {}
        for vertex, neighbors in data.items():
            graph[str(vertex)] = [str(v) for v in neighbors]

        for neighbors in list(graph.values()):
            for vertex in neighbors:
                if vertex not in graph:
                    graph[vertex] = []

        return graph

    if filename.lower().endswith(".csv"):
        graph = {}

        with open(filename, "r", encoding="utf-8", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if not row:
                    continue

                vertex = row[0].strip()

                if vertex not in graph:
                    graph[vertex] = []

                for neighbor in row[1:]:
                    neighbor = neighbor.strip()
                    if neighbor:
                        graph[vertex].append(neighbor)
                        if neighbor not in graph:
                            graph[neighbor] = []

        return graph

    raise ValueError("Підтримуються лише файли JSON та CSV")


def dfs(graph, start, visited):
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def get_connected_components(graph):
    visited = set()
    components = []

    for vertex in graph:
        if vertex not in visited:
            component = set()

            def visit(current):
                visited.add(current)
                component.add(current)

                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visit(neighbor)

            visit(vertex)
            components.append(component)

    return components


def get_weakly_connected_components(graph):
    undirected = {vertex: [] for vertex in graph}

    for vertex in graph:
        for neighbor in graph[vertex]:
            undirected[vertex].append(neighbor)
            undirected[neighbor].append(vertex)

    visited = set()
    components = []

    for vertex in undirected:
        if vertex not in visited:
            component = set()
            stack = [vertex]

            while stack:
                current = stack.pop()

                if current in visited:
                    continue

                visited.add(current)
                component.add(current)

                for neighbor in undirected[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)

            components.append(component)

    return components


def is_connected(graph):
    if not graph:
        return True

    components = get_weakly_connected_components(graph)
    return len(components) == 1


def find_cycle(graph):
    state = {vertex: 0 for vertex in graph}
    path = []
    positions = {}

    def dfs_cycle(vertex):
        state[vertex] = 1
        positions[vertex] = len(path)
        path.append(vertex)

        for neighbor in graph[vertex]:
            if state[neighbor] == 0:
                cycle = dfs_cycle(neighbor)
                if cycle:
                    return cycle

            elif state[neighbor] == 1:
                start = positions[neighbor]
                return path[start:] + [neighbor]

        path.pop()
        positions.pop(vertex, None)
        state[vertex] = 2
        return None

    for vertex in graph:
        if state[vertex] == 0:
            cycle = dfs_cycle(vertex)
            if cycle:
                return cycle

    return None


def tarjan_scc(graph):
    index = 0
    stack = []
    on_stack = set()
    indices = {}
    lowlink = {}
    components = []

    def strongconnect(vertex):
        nonlocal index

        indices[vertex] = index
        lowlink[vertex] = index
        index += 1

        stack.append(vertex)
        on_stack.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in indices:
                strongconnect(neighbor)
                lowlink[vertex] = min(
                    lowlink[vertex],
                    lowlink[neighbor]
                )
            elif neighbor in on_stack:
                lowlink[vertex] = min(
                    lowlink[vertex],
                    indices[neighbor]
                )

        if lowlink[vertex] == indices[vertex]:
            component = []

            while True:
                current = stack.pop()
                on_stack.remove(current)
                component.append(current)

                if current == vertex:
                    break

            components.append(component)

    for vertex in graph:
        if vertex not in indices:
            strongconnect(vertex)

    return components


def print_graph(graph):
    print("\nГраф:")
    for vertex, neighbors in graph.items():
        print(f"{vertex}: {', '.join(neighbors) if neighbors else '-'}")


def connectivity_menu(graph):
    components = get_weakly_connected_components(graph)

    if len(components) == 1:
        print("\nГраф є зв'язним.")
    else:
        print("\nГраф не є зв'язним.")
        print("Зв'язні компоненти:")

        for i, component in enumerate(components, 1):
            print(f"{i}: {', '.join(sorted(component))}")


def cycle_menu(graph):
    cycle = find_cycle(graph)

    if cycle:
        print("\nУ графі знайдено цикл:")
        print(" -> ".join(cycle))
    else:
        print("\nЦиклів у графі не знайдено.")


def scc_menu(graph):
    components = tarjan_scc(graph)

    print("\nКомпоненти сильної зв'язності:")

    for i, component in enumerate(components, 1):
        print(f"{i}: {', '.join(sorted(component))}")


def main():
    if len(sys.argv) < 2:
        filename = input("Введіть назву файлу графа: ").strip()
    else:
        filename = sys.argv[1]

    try:
        graph = load_graph(filename)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return
    except (ValueError, json.JSONDecodeError) as error:
        print(f"Помилка: {error}")
        return

    print_graph(graph)

    while True:
        print("\nМеню:")
        print("1. Перевірити зв'язність графа")
        print("2. Знайти цикл")
        print("3. Знайти компоненти сильної зв'язності")
        print("4. Показати граф")
        print("0. Вихід")

        choice = input("Оберіть операцію: ").strip()

        if choice == "1":
            connectivity_menu(graph)
        elif choice == "2":
            cycle_menu(graph)
        elif choice == "3":
            scc_menu(graph)
        elif choice == "4":
            print_graph(graph)
        elif choice == "0":
            print("Завершення роботи.")
            break
        else:
            print("Невірний вибір.")


if __name__ == "__main__":
    main()

#python main.py graph.json я знаю що ви знаєте як це запустити але на всяк випадок 