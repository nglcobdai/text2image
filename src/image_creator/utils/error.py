from nglcobdai_utils import TemplateError


class ModelInfoUnexpectedError(TemplateError):
    """Error raised when model info is not expected"""

    _CODE = "IMC-E0001"

    _NOTE = "Model info type is not expected: {info}. Check the model info type."


class InitializeModelError(TemplateError):
    """Error raised when model initialization fails"""

    _CODE = "IMC-E0002"

    _NOTE = "Initialization of the model failed. Check the model ID and the availability of the model."


class ImageGenerationError(TemplateError):
    """Error raised when image generation fails"""

    _CODE = "IMC-E0003"

    _NOTE = "Image generation failed. {error}"


class OutputPathIsNotExistsError(TemplateError):
    """Error raised when output path is not exists"""

    _CODE = "IMC-E0004"

    _NOTE = "Output path is not setting. Set the `path` in the settings."


class OutputPathNotFoundError(TemplateError):
    """Error raised when file not found"""

    _CODE = "IMC-E0005"

    _NOTE = "No such file or directory: {path}. Check the file path."


class OrderPromptIsNotExistsError(TemplateError):
    """Error raised when order prompt is not exists"""

    _CODE = "IMC-E0006"

    _NOTE = "Order prompt is not setting. Set the `prompt` in the order."
