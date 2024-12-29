from datetime import datetime
from pathlib import Path

from image_creator import FluxInfo, Order, t2i
from image_creator.utils import HuggingFace, settings


def main():
    output_dir = Path("/datadrive/output/debug")
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.png"

    HuggingFace.login(token=settings.HUGGINGFACE_API_TOKEN)

    order = Order(
        prompt="A beautiful sunset",
        category="portrait",
        num_inference_steps=50,
        is_save=True,
        path=output_dir / filename,
    )

    fi = FluxInfo(base_model_id="black-forest-labs/FLUX.1-dev", use_gpu=True)
    generator = t2i(info=fi)
    generator(order)


if __name__ == "__main__":
    main()
