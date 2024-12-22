import gc

import numpy as np
import torch
from diffusers import DiffusionPipeline

from image_creator.model.info import ModelInfo, Order
from image_creator.utils import (
    ImageGenerationError,
    OutputPathNotFoundError,
    InitializeModelError,
    gpu_monitor,
    logger,
    messenger,
)


class Base:
    def __init__(self, info: ModelInfo):
        """Initialize Base model

        Args:
            info (ModelInfo): ModelInfo object
        """
        logger.info(messenger("INFO", "IMC-I0010"))
        self.pipe = None
        self.device = "cuda" if info.use_gpu and torch.cuda.is_available() else "cpu"
        try:
            self._init_model(info)
        except Exception:
            raise InitializeModelError()

        # self.pipe.to(self.device)
        logger.info(messenger("INFO", "IMC-I0011", device=self.device))
        logger.info(messenger("INFO", "IMC-I0012", model=info.base_model_id))

    @gpu_monitor(interval=0.5)
    def __call__(self, order: Order):
        """Generate image

        Args:
            order (Order): Order object

        Returns:
            PIL.Image.Image: Image object

        Raises:
            ImageGenerationError: Image generation failed
            OutputPathIsNotExistsError: Output path is not setting
            OutputPathNotFoundError: No such file or directory
        """
        logger.info(messenger("INFO", "IMC-I0020"))
        logger.info(messenger("INFO", "IMC-I0021", prompt=order.prompt))

        image = self.generate(self.pipe, order)

        if order.is_save:
            self._save(image, order.path)

        logger.info(messenger("INFO", "IMC-I0022"))

        return image

    def _init_model(self, _: ModelInfo):
        """Initialize model

        Args:
            info (ModelInfo): ModelInfo object
        """
        pass

    @staticmethod
    def generate(pipe: DiffusionPipeline, order: Order):
        """Generate image from text prompt

        Args:
            pipe (DiffusionPipeline): DiffusionPipeline object
            order (Order): Order object

        Returns:
            PIL.Image.Image: Image object

        Raises:
            ImageGenerationError: Image generation failed
        """
        try:
            image = pipe(
                prompt=order.prompt,
                width=order.width,
                height=order.height,
                num_inference_steps=order.num_inference_steps,
                generator=order.get_generator(),
                guidance_scale=order.guidance_scale,
            ).images[0]
        except Exception as e:
            raise ImageGenerationError(error=e)

        return image

    @staticmethod
    def to_numpy(image):
        """Convert image tensor to numpy array

        Args:
            image (PIL.Image.Image): Image object

        Returns:
            np.ndarray: Image numpy array
        """
        return np.array(image)

    def _save(self, image, path):
        """Save image to disk

        Args:
            image (PIL.Image.Image): Image object
            path (str): File path

        Raises:
            OutputPathIsNotExistsError: Output path is not setting
            OutputPathNotFoundError: No such file or directory
        """
        try:
            image.save(path, path.suffix[1:].upper())
            logger.info(messenger("INFO", "IMC-I0030", path=path))
        except FileNotFoundError:
            raise OutputPathNotFoundError(path=path)

    def flush(self):
        if self.pipe is not None:
            del self.pipe
        gc.collect()
        torch.cuda.empty_cache()
        logger.info(messenger("INFO", "IMC-I0040"))
