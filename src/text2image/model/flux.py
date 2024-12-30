import torch
from diffusers import FluxPipeline
from transformers import BitsAndBytesConfig, T5EncoderModel

from text2image.model.base import Base
from text2image.model.info import FluxInfo


class Flux(Base):
    def __init__(self, info: FluxInfo = FluxInfo()):
        """Initialize Flux model

        Args:
            info (FluxInfo, optional): FluxInfo object. Defaults to FluxInfo().
        """
        super().__init__(info)

    def _init_model(self, info):
        """Initialize model

        Args:
            info (FluxInfo): FluxInfo object
        """
        textencoder_config = BitsAndBytesConfig(
            load_in_4bit=info.load_in_4bit,
            bnb_4bit_use_double_quant=True,  # ダブル量子化を有効化
            bnb_4bit_quant_type="nf4",  # メモリ効率の高いNF4量子化
        )
        text_encoder_2 = T5EncoderModel.from_pretrained(
            info.base_model_id,
            subfolder="text_encoder_2",
            quantization_config=textencoder_config,
            torch_dtype=torch.bfloat16,
        )

        self.pipe = FluxPipeline.from_pretrained(
            info.base_model_id,
            text_encoder_2=text_encoder_2,
            torch_dtype=torch.bfloat16,
            device_map="balanced",
        )
