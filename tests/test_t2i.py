import pytest

from text2image import ModelInfoUnexpectedError, t2i


class TestModelInfoUnexpectedError:
    def test_unexpected_error(self):
        fi = None

        with pytest.raises(ModelInfoUnexpectedError) as e:
            _ = t2i(info=fi)

        assert type(e.value) is ModelInfoUnexpectedError
