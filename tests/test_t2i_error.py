import pytest

from image_creator import (
    FluxInfo,
    InitializeModelError,
    Order,
    OrderPromptIsNotExistsError,
    OutputPathIsNotExistsError,
    OutputPathNotFoundError,
    t2i,
)
from image_creator.utils import settings


class TestOrderPromptIsNotExistsError:
    def test_no_prompt(self):
        with pytest.raises(OrderPromptIsNotExistsError) as e:
            _ = Order(is_save=False)

        assert type(e.value) is OrderPromptIsNotExistsError


class TestInitializeModelError:
    def test_initialize_model_error(self):
        with pytest.raises(InitializeModelError) as e:
            fi = FluxInfo(base_model_id="xxx", use_gpu=settings.USE_GPU)
            _ = t2i(info=fi)

        assert type(e.value) is InitializeModelError


class TestOutputPathIsNotExistsError:
    def test_output_path_is_not_exists_error(self):
        with pytest.raises(OutputPathIsNotExistsError) as e:
            _ = Order(prompt="A beautiful sunset", is_save=True)

        assert type(e.value) is OutputPathIsNotExistsError


class TestOutputPathNotFoundError:
    def test_output_path_not_found_error(self):
        with pytest.raises(OutputPathNotFoundError) as e:
            fi = FluxInfo(base_model_id=settings.MODEL_ID, use_gpu=settings.USE_GPU)
            generator = t2i(info=fi)

            order = Order(
                prompt="A beautiful sunset",
                is_save=True,
                path="xxx/xxx.png",
                num_inference_steps=1,
            )
            _ = generator(order)
            generator.flush()

        assert type(e.value) is OutputPathNotFoundError
