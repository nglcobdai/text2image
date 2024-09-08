import yaml


def load_yaml(path):
    """yamlファイルを読み込む

    Args:
        path (Path): yamlファイルのパス

    Returns:
        dict: yamlファイルの内容
    """
    if not path.exists():
        raise FileNotFoundError(f"{path} not found")

    with open(path, "r") as f:
        file = f.read()
        return yaml.safe_load(file)
