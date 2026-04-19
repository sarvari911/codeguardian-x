import networkx as nx

def build_dependency_graph():
    """
    Simulates building a dependency graph of the codebase.
    Returns a networkx graph object.
    """
    G = nx.DiGraph()
    
    # Adding nodes (files/modules)
    nodes = [
        "api/routes/auth.py",
        "db/query_builder.py",
        "models/user.py",
        "utils/sanitizer.py",
        "admin/admin_panel.py",
        "config/settings.py",
        "app.py"
    ]
    G.add_nodes_from(nodes)
    
    # Adding edges (dependencies)
    edges = [
        ("app.py", "api/routes/auth.py"),
        ("api/routes/auth.py", "db/query_builder.py"),
        ("api/routes/auth.py", "models/user.py"),
        ("api/routes/auth.py", "utils/sanitizer.py"), # Normally sanitized, but missing in vulnerable path
        ("db/query_builder.py", "admin/admin_panel.py"),
        ("models/user.py", "db/query_builder.py"),
        ("admin/admin_panel.py", "config/settings.py")
    ]
    G.add_edges_from(edges)
    
    return G
