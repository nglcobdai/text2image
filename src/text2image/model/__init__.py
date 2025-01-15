from text2image.model.base import Base
from text2image.model.flux import Flux
from text2image.model.info import FluxInfo, ModelInfo, Order
from text2image.utils import ModelInfoUnexpectedError


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
