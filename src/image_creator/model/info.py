from pathlib import Path
from typing import List

import torch
from pydantic import BaseModel, Field, PrivateAttr
from image_creator.utils import OrderPromptIsNotExistsError, OutputPathIsNotExistsError


class ModelInfo(BaseModel):
    """Model information class for managing model parameters.

    Attributes:
        base_model_id (str): Base model id.
        use_gpu (bool): Use GPU.
    """

    base_model_id: str = Field("", description="Base model id")
    use_gpu: bool = Field(True, description="Either to use GPU")

    class Config:
        """Pydantic configuration to allow alias usage."""

        populate_by_name = True


class FluxInfo(ModelInfo):
    """Flux-specific model information."""

    load_in_4bit: bool = Field(True, description="Load in 4-bit")

    def __init__(self, **data):
        super().__init__(**data)


class Order(BaseModel):
    """Prompt class for managing image generation parameters.

    Attributes:
        title (str): Title of the image.
        category (str): Category of the image.
        tags (List[str]): Tags of the image.
        prompt (str): Text prompt.
        width (int): Image width.
        height (int): Image height.
        num_inference_steps (int): Number of inference steps.
        guidance_scale (float): Guidance scale.
        seed (int): Random seed.
        is_save (bool): Save image to disk.
        path (str | Path): File output path.
    """

    title: str = Field("", description="Title of the image")
    category: str = Field("general", description="Category of the image")
    tags: List[str] = Field(default_factory=list, description="Tags of the image")
    prompt: str = Field(None, description="Text prompt")

    width: int = Field(1360, description="Image width")
    height: int = Field(768, description="Image height")
    num_inference_steps: int = Field(50, description="Number of inference steps")
    guidance_scale: float = Field(3.5, description="Guidance scale")
    seed: int = Field(123, description="Random seed")

    is_save: bool = Field(False, description="Save image to disk")
    path: str | Path = Field(None, description="File output path")

    # Private attribute for generator
    _generator: torch.Generator = PrivateAttr()

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)
        if isinstance(self.path, str):
            self.path = Path(self.path)
        if self.prompt is None:
            raise OrderPromptIsNotExistsError()
        if self.is_save and self.path is None:
            raise OutputPathIsNotExistsError()
        self._generator = torch.Generator().manual_seed(self.seed)

    def get_generator(self) -> torch.Generator:
        """Access the private generator."""
        return self._generator
