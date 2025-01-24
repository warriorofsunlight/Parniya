import torch
from diffusers import StableDiffusionPipeline

def generate(prompt):
    model_id = "CompVis/stable-diffusion-v1-4"
    device = "cuda"

    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16,
                                                revision="fp16")
    pipe = pipe.to(device)

    image = pipe(prompt).images[0]

    return image

if __name__ == '__main__':
    image = generate('a red mustang in rainy night, 4k')
    print(image)