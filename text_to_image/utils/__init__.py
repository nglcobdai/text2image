from nglcobdai_utils import Logger, Settings

from text_to_image.utils.yml import load_yaml

settings = Settings()
logger = Logger(settings.PROJECT_NAME, f"logs/text-to-image.log").logger
