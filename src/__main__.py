from datetime import datetime
from pathlib import Path

from image_creator import t2i, Order, FluxInfo
from image_creator.utils import settings


def main():
    output_dir = Path(settings.DATADRIVE) / "output" / "debug"
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.png"

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
