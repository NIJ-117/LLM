import streamlit as st
from PIL import Image
import model_loader
import pipeline
from transformers import CLIPTokenizer
import torch

def app():

    # Assuming `model_loader` and `pipeline` are modules with the necessary functions
    # and that your model and tokenizer are loaded globally for simplicity.

    # Initialize model and tokenizer
    DEVICE = "cpu"
    ALLOW_CUDA = True
    ALLOW_MPS = False

    # Setup device
    if torch.cuda.is_available() and ALLOW_CUDA:
        DEVICE = "cuda"
    elif (torch.has_mps or torch.backends.mps.is_available()) and ALLOW_MPS:
        DEVICE = "mps"
    else:
        DEVICE = "cpu"

    tokenizer_path = "/content/tokenizer_vocab.json"  # Update this path
    merges_file_path = "/content/tokenizer_merges.txt"  # Update this path
    model_file_path = "/content/drive/MyDrive/stable diffusion/Copy of v1-5-pruned-emaonly (1).ckpt"  # Update this path


    tokenizer = CLIPTokenizer(tokenizer_path, merges_file=merges_file_path)
    models = model_loader.preload_models_from_standard_weights(model_file_path, DEVICE)

    # Streamlit app
    st.title("AI Image Generator")

    # User input for the prompt
    prompt = st.text_input("Enter a prompt for the image:", "A scenic landscape with mountains and a clear sky.")

    # Parameters for image generation
    cfg_scale = st.slider("CFG Scale", min_value=1, max_value=14, value=8)
    num_inference_steps = st.slider("Number of Inference Steps", min_value=1, max_value=100, value=50)
    seed = st.number_input("Seed", value=42)

    # Generate button
    if st.button("Generate Image"):
        output_image = pipeline.generate(
            prompt=prompt,
            uncond_prompt="",
            input_image=None,
            strength=0.9,
            do_cfg=True,
            cfg_scale=cfg_scale,
            sampler_name="ddpm",
            n_inference_steps=num_inference_steps,
            seed=seed,
            models=models,
            device=DEVICE,
            idle_device="cpu",
            tokenizer=tokenizer,
        )

        # Display the image
        st.image(Image.fromarray(output_image), caption="Generated Image")

    # Running the Streamlit app:
    # To run this Streamlit app, save the code to a file named `streamlit_app.py` and
    # execute `streamlit run streamlit_app.py` in your terminal.
