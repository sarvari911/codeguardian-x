import time

def ingest_repo(repo_url):
    """
    Simulates ingesting a GitHub repository.
    """
    time.sleep(2)  # Simulate network and parsing delay
    return {
        "repo_url": repo_url,
        "files_analyzed": 847,
        "lines_of_code": 94312,
        "tokens_used": 380450,
        "status": "Success",
        "message": "Entire repository ingested in a single pass (No chunking)"
    }
