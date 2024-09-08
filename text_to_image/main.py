from datetime import datetime

from text_to_image.api.model import TextToImageModel
from text_to_image.order.order import Order
from text_to_image.utils import load_yaml, logger, settings
from pathlib import Path


def main():
    logger.info(f"Hello, {settings.PROJECT_NAME}!")

    order = Order(**load_yaml(Path("/root/workspace/config/order.yml")))

    output_dir = Path(settings.DATADRIVE) / "output" / order.category
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    path = output_dir / filename

    generator = TextToImageModel(use_gpu=settings.USE_GPU)
    generator(order.prompt(), is_save=True, path=path)


if __name__ == "__main__":
    main()
