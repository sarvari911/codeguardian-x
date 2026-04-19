import plotly.graph_objects as go

def generate_chain_visualization(chain_steps):
    """
    Generates a simple flowchart-like visualization for the attack chain steps.
    """
    # Simple vertical flowchart
    y_vals = list(range(len(chain_steps), 0, -1))
    x_vals = [1] * len(chain_steps)
    
    fig = go.Figure(data=[go.Scatter(
        x=x_vals,
        y=y_vals,
        mode='markers+text',
        text=[step.split(' — ')[0] for step in chain_steps],
        textposition="middle right",
        marker=dict(size=20, color='red', symbol='square'),
        hovertext=chain_steps
    )])
    
    # Add connecting lines
    for i in range(len(y_vals)-1):
        fig.add_shape(
            type="line",
            x0=1, y0=y_vals[i]-0.2, x1=1, y1=y_vals[i+1]+0.2,
            line=dict(color="red", width=2)
        )
        # Add arrow
        fig.add_annotation(
            x=1, y=y_vals[i+1]+0.2,
            ax=1, ay=y_vals[i]-0.2,
            xref='x', yref='y', axref='x', ayref='y',
            showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor="red"
        )
        
    fig.update_layout(
        title="Attack Chain Execution Flow",
        xaxis=dict(visible=False, range=[0, 3]),
        yaxis=dict(visible=False, range=[0, len(chain_steps)+1]),
        showlegend=False,
        plot_bgcolor="white"
    )
    
    return fig
