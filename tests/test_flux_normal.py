import numpy as np
from PIL import Image

from image_creator import FluxInfo, Order, t2i
from image_creator.utils import settings


class TestFluxNormal:
    @classmethod
    def setup_class(self):
        fi = FluxInfo(base_model_id=settings.MODEL_ID, use_gpu=settings.USE_GPU)
        self.generator = t2i(info=fi)

        order = Order(
            prompt="A beautiful sunset",
            is_save=True,
            path="sample/test_flux.png",
            num_inference_steps=1,
        )
        self.image = self.generator(order)
        self.generator.flush()

    def test_generate_image(self):
        assert isinstance(self.image, Image.Image)

    def test_to_numpy(self):
        image_np = self.generator.to_numpy(self.image)
        assert type(image_np) is np.ndarray
