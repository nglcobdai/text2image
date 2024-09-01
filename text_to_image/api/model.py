import torch
from diffusers import DiffusionPipeline, LCMScheduler, UNet2DConditionModel
from huggingface_hub import hf_hub_download

from text_to_image.utils import logger


class TextToImageModel:

    def __init__(
        self,
        base_model_id="stabilityai/stable-diffusion-xl-base-1.0",
        repo_name="SYZhang0805/DisBack",
        ckpt_name="SDXL_DisBack.bin",
        use_gpu=False,
    ):
        """Initialize TextToImageModel

        Args:
            base_model_id (str, optional): Base model ID ("stabilityai/stable-diffusion-xl-base-1.0").
            repo_name (str, optional): Repository name ("SYZhang0805/DisBack").
            ckpt_name (str, optional): Checkpoint name ("SDXL_DisBack.bin").
        """
        base_model_id = base_model_id
        repo_name = repo_name
        ckpt_name = ckpt_name
        device = "cuda" if use_gpu else "cpu"

        # Proper usage of from_config
        unet_config = UNet2DConditionModel.load_config(base_model_id, subfolder="unet")
        unet = UNet2DConditionModel.from_config(unet_config).to("cuda", torch.float16)

        # Use weights_only=True to avoid security issues
        unet.load_state_dict(
            torch.load(
                hf_hub_download(repo_name, ckpt_name),
                map_location=device,
                weights_only=True,
            )
        )

        self.pipe = DiffusionPipeline.from_pretrained(
            base_model_id,
            unet=unet,
            torch_dtype=torch.float16,
            use_safetensors=True,
            variant="fp16",
        ).to(device)

        # Initialize LCMScheduler properly without unnecessary parameters
        self.pipe.scheduler = LCMScheduler.from_config(self.pipe.scheduler.config)

        logger.info("TextToImageModel initialized")

    def __call__(self, prompt, is_save=False, **kwargs):
        """Generate image from text prompt and save to disk

        Args:
            prompt (str): Text prompt
            is_save (bool, optional): Save image to disk (False).
            **kwargs: Arbitrary keyword
                {
                    filename (str): File name
                }

        Returns:
            PIL.Image.Image: Image object
        """
        logger.info(f"Generating image from prompt: {prompt}")
        image = self.generate(prompt)
        logger.info("Image generated")

        if is_save:
            try:
                path = kwargs.get("path")
            except AttributeError:
                return logger.error("Parameter 'path' is required for saving image")
            self.save(image, path)

        return image

    def generate(self, prompt):
        """Generate image from text prompt

        Args:
            prompt (str): Text prompt

        Returns:
            PIL.Image.Image: Image object
        """
        image = self.pipe(
            prompt=prompt,
            num_inference_steps=1,
            guidance_scale=0,
            timesteps=[399],
            height=1024,
            width=1024,
        ).images[0]
        return image

    def to_numpy(self, image):
        """Convert image tensor to numpy array

        Args:
            image (PIL.Image.Image): Image object

        Returns:
            np.ndarray: Image numpy array
        """
        return image.numpy()

    def save(self, image, path):
        """Save image to disk

        Args:
            image (torch.Tensor): Image tensor
            filename (str): File path
        """
        image.save(path, "PNG")
        logger.info(f"Image saved to {path}")
