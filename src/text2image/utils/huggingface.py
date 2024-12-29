from huggingface_hub import login
from text2image.utils.setup import logger, messenger
from text2image.utils.error import HuggingFaceValueError


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
