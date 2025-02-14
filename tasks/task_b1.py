def task_b1(path: str):
    if not path.startswith("data/"):
        raise ValueError("Access denied: Path is outside /data")