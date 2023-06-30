import matplotlib.pyplot as plt
plt.style.use("dark_background")


def draw_network(G: dict, points: list) -> plt.plot:
    line_points = []
    plt.axis("off")

    for k, v in G.items():
        plt.annotate(f"{k}", (points[0][k], points[1][k]), 
                    color="k", verticalalignment='center', 
                    horizontalalignment='center',
                    zorder=420
                    )
        for link in v:
        
            line_points.append([points[0][k], points[0][link]])
            line_points.append([points[1][k], points[1][link]])
            

            
    plt.plot(*line_points, c="gray", alpha=.5, zorder=1)
    plt.scatter(*points, s=242, zorder=42)
    plt.show()
