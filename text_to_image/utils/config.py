from pathlib import Path

import yaml
from pydantic import ConfigDict
from pydantic_settings import BaseSettings

from text_to_image.utils.log import logger


class Settings(BaseSettings):
    PROJECT_NAME: str
    DOCKER_SHM_SIZE: str

    LOGGING_LEVEL: str

    USE_GPU: bool

    DATADRIVE: str

    model_config = ConfigDict(env_file=".env", env_file_encoding="utf-8")

    def __init__(self, **data):
        super().__init__(**data)
        self.DATADRIVE = Path(self.DATADRIVE)


def load_yaml(path):
    """yamlファイルを読み込む

    Args:
        path (Path): yamlファイルのパス

    Returns:
        dict: yamlファイルの内容
    """
    if not path.exists():
        raise logger.error(f"{path} not found")

    with open(path, "r") as f:
        file = f.read()
        return yaml.safe_load(file)


settings = Settings()
