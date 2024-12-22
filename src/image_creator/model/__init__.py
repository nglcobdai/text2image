from image_creator.model.base import Base
from image_creator.model.flux import Flux
from image_creator.model.info import FluxInfo, ModelInfo, Order
from image_creator.utils import ModelInfoUnexpectedError


def t2i(info: ModelInfo | None) -> Flux:
    """Initialize TextToImage

    Args:
        info (ModelInfo): ModelInfo object

    Returns:
        Flux: Flux object
    """
    match info:
        case FluxInfo():
            return Flux(info)
        case _:
            raise ModelInfoUnexpectedError(info=str(info))
