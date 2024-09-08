import numpy as np
from text_to_image.utils import settings
from PIL import Image

from text_to_image.api.model import TextToImageModel


class TestGenerate:
    def setup_class(self):
        self.generator = TextToImageModel(use_gpu=settings.USE_GPU)
        self.image = self.generator("A beautiful sunset", is_save=False)

    def test_generate_image(self):
        assert isinstance(self.image, Image.Image)

    def test_to_numpy(self):
        image_np = self.generator.to_numpy(self.image)
        assert type(image_np) is np.ndarray
