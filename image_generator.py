import torch
from diffusers import StableDiffusionPipeline
import os

os.environ["HF_HUB_DISABLE_SYMLINKS"] = "1"

class ImageGenerator:
    def __init__(self, model_path):
        print("🚀 Stable Diffusion yükleniyor...")

        self.pipe = StableDiffusionPipeline.from_single_file(
            model_path,
            torch_dtype=torch.float16,
            safety_checker=None
        )

        self.pipe = self.pipe.to("cuda")
        self.pipe.enable_attention_slicing()

        self.negative_prompt = (
            "people, human, face, portrait, character, "
            "ugly, blurry, distorted, deformed, oversaturated, "
            "low quality, grain, noise, artifacts, "
            "watermark, text, logo, "
            "monster, demon, ghost, zombie, skull, blood, gore, "
            "distorted creature, horror face, scary creature, "
            "collage, split image, multiple scenes, multiple views, "
            "two scenes, panel, comic, grid, stacked image, "
        )

        print("✅ Model GPU’da hazır!")

    def generate(self, prompt, save_path, emotion, width=512, height=512):

        cfg_map = {
            "happy": 6.5,
            "neutral": 7.0,
            "sad": 7.5,
            "surprise": 7.5,
            "angry": 8.0,
            "fear": 8.5
        }
        cfg = cfg_map.get(emotion, 7.0)

        try:
            image = self.pipe(
                prompt=prompt,
                negative_prompt=self.negative_prompt,
                width=width,
                height=height,
                num_inference_steps=25,
                guidance_scale=cfg
            ).images[0]

            image.save(save_path)
            return True
        except Exception as e:
            print("❌ GENERATION ERROR:", e)
            return False
