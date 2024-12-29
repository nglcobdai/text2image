import numpy as np
from PIL import Image

from image_creator import FluxInfo, Order, t2i
from image_creator.utils import HuggingFace, settings
from pathlib import Path


class TestFluxNormal:
    @classmethod
    def setup_class(self):
        self.path = Path("sample/test_flux.png")
        HuggingFace.login(token=settings.HUGGINGFACE_API_TOKEN)

        fi = FluxInfo(base_model_id=settings.MODEL_ID, use_gpu=settings.USE_GPU)
        self.generator = t2i(info=fi)

        order = Order(
            prompt="A beautiful sunset",
            is_save=True,
            path=self.path,
            num_inference_steps=1,
        )
        self.image = self.generator(order)
        self.generator.flush()

    def test_generate_image(self):
        assert isinstance(self.image, Image.Image)

    def test_to_numpy(self):
        image_np = self.generator.to_numpy(self.image)
        assert type(image_np) is np.ndarray

    @classmethod
    def teardown_class(self):
        self.path.unlink()
