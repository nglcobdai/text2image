from pathlib import Path

from nglcobdai_utils import (
    ConsoleHandlerInfo,
    Messenger,
    RotatingFileHandlerInfo,
    Settings,
    get_logger,
)

settings = Settings()
ch = ConsoleHandlerInfo(log_level="INFO")
fh = RotatingFileHandlerInfo(
    log_level="DEBUG", filename="/datadrive/logs/text2image.log"
)
logger = get_logger(name=settings.PROJECT_NAME, ch_info=ch, fh_info=fh)
messenger = Messenger(Path(__file__).resolve().parent.parent / "config/message.ini")
