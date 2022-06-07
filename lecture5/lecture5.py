import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation

elist = [(1, 2, 5.0), (2, 3, 3.0), (1, 3, 1.0), (3, 4, 7.3)]

G = nx.Graph()
G.add_weighted_edges_from(elist)

labels = nx.get_edge_attributes(G, 'weight')
# упаковка графа на плоскость. существует несколько возможных конфигураций (layout)
pos = nx.spring_layout(G, seed=7)

fig, ax = plt.subplots(figsize=(len(elist), 4))


def update(idx):
    ax.clear()
    # рендер вершин
    nx.draw_networkx_nodes(G, pos, ax=ax)

    # рендер рёбер
    nx.draw_networkx_edges(
        G, pos, edgelist=[elist[idx]], width=6, alpha=0.5, edge_color="r", style="dashed", ax=ax
    )

    nx.draw_networkx_edges(
        G, pos, edgelist=elist[:idx] + elist[idx + 1:], width=7, edge_color="b", ax=ax
    )

    # рендер меток вершин
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif", ax=ax)

    # рендер меток рёбер
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels, ax=ax)

    ax.set_title(f'Frame {idx}')


ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(elist), interval=1000, repeat=True)
plt.show()
