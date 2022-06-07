import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation


def stp_read(stp_file):
    f = open(stp_file, mode="r")
    g = []
    flag = False
    for line in f:
        if line == "SECTION Graph\n":
            flag = True
            continue
        elif line == "END":
            break
        elif len(line.split()) < 4:
            continue
        if flag:
            au, u, v, c = line.split()
            if au == "E":
                g.append((int(v), int(u), int(c)))
            g.append((int(u), int(v), int(c)))
    return g


def update(idx):
    ax.clear()
    nx.draw_networkx_nodes(G, pos, ax=ax)

    nx.draw_networkx_edges(
        G, pos, edgelist=[elist[idx]], width=2, alpha=0.5, edge_color="yellow", style="dashed", ax=ax
    )

    nx.draw_networkx_edges(
        G, pos, edgelist=elist[:idx] + elist[idx + 1:], width=2, edge_color="g", ax=ax
    )

    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif", ax=ax)

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels, ax=ax)

    ax.set_title(f'Frame {idx}')


elist = stp_read("simple.stp")
print(elist)

G = nx.Graph()
G.add_weighted_edges_from(elist)
labels = nx.get_edge_attributes(G, "weight")
pos = nx.planar_layout(G)

fig, ax = plt.subplots(figsize=(len(elist), 4))

ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(elist), interval=1000, repeat=True)
plt.show()