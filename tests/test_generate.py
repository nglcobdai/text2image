from PIL import Image
import numpy as np
from text_to_image.api.model import TextToImageModel
from text_to_image.utils import logger


class TestGenerate:
    def setup_class(self):
        self.generator = TextToImageModel(use_gpu=True)
        self.image = self.generator("A beautiful sunset", is_save=False)
        logger.info("Generate image")

    def test_generate_image(self):
        assert isinstance(self.image, Image.Image)

    def test_to_numpy(self):
        image_np = self.generator.to_numpy(self.image)
        assert type(image_np) is np.ndarray
