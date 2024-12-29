import pytest

from image_creator.utils import HuggingFace, HuggingFaceValueError, settings


class TestHuggingFaceLogin:
    def test_login(self):
        token = settings.HUGGINGFACE_API_TOKEN
        HuggingFace.login(token=token)
        assert True

    def test_login_error(self):
        with pytest.raises(HuggingFaceValueError):
            HuggingFace.login(token="")


# class TestHuggingFaceLogout:
#     @classmethod
#     def setup_class(self):
#         token = settings.HUGGINGFACE_API_TOKEN
#         HuggingFace.login(token=token)

#     def test_logout(self):
#         HuggingFace.logout()
#         assert True
