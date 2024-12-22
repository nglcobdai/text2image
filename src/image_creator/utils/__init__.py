from nglcobdai_utils import Messenger, Settings, get_logger

from image_creator.utils.error import (
    ImageGenerationError,
    InitializeModelError,
    ModelInfoUnexpectedError,
    OutputPathIsNotExistsError,
    OutputPathNotFoundError,
    OrderPromptIsNotExistsError,
)
from image_creator.utils.gpu_monitor import gpu_monitor

from nglcobdai_utils import (
    ConsoleHandlerInfo,
    FileHandlerInfo,
    get_logger,
)


settings = Settings()
ch = ConsoleHandlerInfo(log_level="INFO")
fh = FileHandlerInfo(log_level="DEBUG", log_file="logs/app.log")
logger = get_logger(name=settings.PROJECT_NAME, ch_info=ch, fh_info=fh)
messenger = Messenger("src/config/message.ini")
