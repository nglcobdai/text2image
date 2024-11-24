import pytest

from image_creator import (
    ImageGenerationError,
    InitializeModelError,
    ModelInfoUnexpectedError,
    OrderPromptIsNotExistsError,
    OutputPathIsNotExistsError,
    OutputPathNotFoundError,
)


class TestModelInfoUnexpectedError:
    def test_model_info_unexpected_error(self):
        info = None
        with pytest.raises(ModelInfoUnexpectedError) as e:
            raise ModelInfoUnexpectedError(info=info)

        gt = ModelInfoUnexpectedError._MESSAGE_FORMAT.format(
            code=ModelInfoUnexpectedError._CODE,
            note=ModelInfoUnexpectedError._NOTE.format(info=info),
        )

        assert e.value.message == gt


class TestInitializeModelError:
    def test_initialize_model_error(self):
        with pytest.raises(InitializeModelError) as e:
            raise InitializeModelError()

        assert e.value.message == InitializeModelError().message


class TestImageGenerationError:
    def test_image_generation_error(self):
        with pytest.raises(ImageGenerationError) as e:
            raise ImageGenerationError(error=Exception())

        gt = ImageGenerationError._MESSAGE_FORMAT.format(
            code=ImageGenerationError._CODE,
            note=ImageGenerationError._NOTE.format(error=Exception()),
        )

        assert e.value.message == gt


class TestOutputPathIsNotExistsError:
    def test_output_path_is_not_exists_error(self):
        with pytest.raises(OutputPathIsNotExistsError) as e:
            raise OutputPathIsNotExistsError()

        assert e.value.message == OutputPathIsNotExistsError().message


class TestOutputPathNotFoundError:
    def test_output_path_not_found_error(self):
        path = "xxx/xxx.png"
        with pytest.raises(OutputPathNotFoundError) as e:
            raise OutputPathNotFoundError(path=path)

        gt = OutputPathNotFoundError._MESSAGE_FORMAT.format(
            code=OutputPathNotFoundError._CODE,
            note=OutputPathNotFoundError._NOTE.format(path=path),
        )

        assert e.value.message == gt


class TestOrderPromptIsNotExistsError:
    def test_no_prompt(self):
        with pytest.raises(OrderPromptIsNotExistsError) as e:
            raise OrderPromptIsNotExistsError()

        assert e.value.message == OrderPromptIsNotExistsError().message
