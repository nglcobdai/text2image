from huggingface_hub import login
from image_creator.utils.setup import logger, messenger
from image_creator.utils.error import HuggingFaceValueError


class HuggingFace:
    @staticmethod
    def login(token: str):
        """Login to Hugging Face

        Args:
            token (str): Hugging Face API token
        """
        logger.info(messenger("INFO", "IMC-I0050"))
        try:
            login(token=token)
        except ValueError as e:
            raise HuggingFaceValueError(error=e)
        logger.info(messenger("INFO", "IMC-I0051"))
