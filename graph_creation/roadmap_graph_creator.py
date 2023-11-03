from generation.roadmap_models import Roadmap
import plotly.graph_objects as go
import networkx as nx


class RoadmapGraphCreator:
    def __init__(self):
        self.fig = None

    def create(self, roadmap: Roadmap):
        # Create a directed graph
        graph = nx.DiGraph()
        for node in roadmap.nodes:
            graph.add_node(node.id, title=node.title, resources=node.resources)
            for prereq in node.prerequisites:
                graph.add_edge(prereq, node.id)

        # Get positions for the nodes using one of networkx's layout algorithms
        pos = nx.spring_layout(graph)

        # Create edges
        edge_x = []
        edge_y = []
        for edge in graph.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        # Create nodes
        node_x = [pos[node][0] for node in graph.nodes()]
        node_y = [pos[node][1] for node in graph.nodes()]
        node_text = [
            f"{data['title']}<br>{'<br>'.join([f'{resource.name}: {resource.url}' for resource in data['resources']])}"
            for node, data in graph.nodes(data=True)
        ]

        # Create figure
        self.fig = go.Figure()

        # Add edges
        self.fig.add_trace(
            go.Scatter(
                x=edge_x, y=edge_y,
                line=dict(width=0.5, color='#888'),
                hoverinfo='none',
                mode='lines'
            )
        )

        # Add nodes
        self.fig.add_trace(
            go.Scatter(
                x=node_x, y=node_y,
                text=node_text,
                hoverinfo='text',
                mode='markers',
                marker=dict(
                    showscale=False,
                    colorscale='YlGnBu',
                    colorbar=dict(
                        thickness=15,
                        title='Node Connections',
                        xanchor='left',
                        titleside='right'
                    ),
                    line_width=2
                )
            )
        )

        # Update layout
        self.fig.update_layout(
            title='Roadmap Graph',
            titlefont_size=16,
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20, l=5, r=5, t=40),
            annotations=[
                dict(
                    text="Python code: <a href='https://plotly.com/'> Plotly</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002
                )
            ],
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
        )

    def show(self):
        if self.fig is None:
            raise ValueError("No graph has been created. Call the 'create' method first.")
        self.fig.show()
