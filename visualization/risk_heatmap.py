import plotly.graph_objects as go
import networkx as nx

def generate_risk_heatmap(G):
    """
    Generates a Plotly network graph representing the risk heatmap of the codebase.
    Nodes in red represent vulnerable components in the attack chain.
    """
    pos = nx.spring_layout(G, seed=42)
    
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    node_text = []
    node_color = []
    
    vulnerable_nodes = ["api/routes/auth.py", "db/query_builder.py", "admin/admin_panel.py"]

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(node)
        
        if node in vulnerable_nodes:
            node_color.append('#ff4b4b') # Red
        else:
            node_color.append('#00d4b2') # Green

    # Create traces for safe and vulnerable nodes separately to show them in the legend
    safe_x, safe_y, safe_text = [], [], []
    vuln_x, vuln_y, vuln_text = [], [], []
    
    for node in G.nodes():
        x, y = pos[node]
        if node in vulnerable_nodes:
            vuln_x.append(x)
            vuln_y.append(y)
            vuln_text.append(node)
        else:
            safe_x.append(x)
            safe_y.append(y)
            safe_text.append(node)

    safe_trace = go.Scatter(
        x=safe_x, y=safe_y,
        mode='markers+text',
        name='Safe Module',
        hoverinfo='text',
        text=safe_text,
        textposition="top center",
        marker=dict(
            color='#00d4b2',
            size=20,
            line_width=2))
            
    vuln_trace = go.Scatter(
        x=vuln_x, y=vuln_y,
        mode='markers+text',
        name='Vulnerable Module',
        hoverinfo='text',
        text=vuln_text,
        textposition="top center",
        marker=dict(
            color='#ff4b4b',
            size=20,
            line_width=2))

    fig = go.Figure(data=[edge_trace, safe_trace, vuln_trace],
             layout=go.Layout(
                title=dict(
                    text="<br>Codebase Visual Risk Heatmap",
                    font=dict(size=16)
                ),
                showlegend=True,
                legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
    return fig
