import pathlib

import gradio as gr
import open_clip
import torch
torch.cuda.empty_cache()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model, _, transform = open_clip.create_model_and_transforms(
    "coca_ViT-L-14",
    pretrained="mscoco_finetuned_laion2B-s13B-b90k"
)
model.to(device)

title = """<h1 align="center">CoCa: Contrastive Captioners</h1>"""
description = (
    """<br> An open source implementation of <strong>CoCa: Contrastive Captioners are Image-Text Foundation Models</strong> <a href=https://arxiv.org/abs/2205.01917>https://arxiv.org/abs/2205.01917.</a>
    <br> Built using <a href=https://github.com/mlfoundations/open_clip>open_clip</a> with an effort from <a href=https://laion.ai/>LAION</a>. 
    <br> For faster inference without waiting in queue, you may duplicate the space and upgrade to GPU in settings.<a href="https://huggingface.co/spaces/laion/CoCa?duplicate=true"> <img style="margin-top: 0em; margin-bottom: 0em" src="https://bit.ly/3gLdBN6" alt="Duplicate Space"></a>"""
)


def output_generate(image):
    im = transform(image).unsqueeze(0).to(device)
    with torch.no_grad(), torch.cuda.amp.autocast():
        generated = model.generate(im, seq_len=20)
    return open_clip.decode(generated[0].detach()).split("<end_of_text>")[0].replace("<start_of_text>", "")


def inference_caption(image, decoding_method="Beam search", rep_penalty=1.2, top_p=0.5, min_seq_len=5, seq_len=20):
    im = transform(image).unsqueeze(0).to(device)
    generation_type = "beam_search" if decoding_method == "Beam search" else "top_p"
    with torch.no_grad(), torch.cuda.amp.autocast():
        generated = model.generate(
            im,
            generation_type=generation_type,
            top_p=float(top_p),
            min_seq_len=min_seq_len,
            seq_len=seq_len,
            repetition_penalty=float(rep_penalty)
        )
    return open_clip.decode(generated[0].detach()).split("<end_of_text>")[0].replace("<start_of_text>", "")


paths = sorted(pathlib.Path("images").glob("*.jpg"))
with gr.Blocks() as iface:
    state = gr.State([])

    gr.Markdown(title)
    gr.Markdown(description)

    with gr.Row():
        with gr.Column(scale=1):
            image_input = gr.Image(type="pil")

            # with gr.Row():
            sampling = gr.Radio(
                choices=["Beam search", "Nucleus sampling"],
                value="Beam search",
                label="Text Decoding Method",
                interactive=True,
            )

            rep_penalty = gr.Slider(
                minimum=1.0,
                maximum=5.0,
                value=1.0,
                step=0.5,
                interactive=True,
                label="Repeat Penalty (larger value prevents repetition)",
            )

            top_p = gr.Slider(
                minimum=0.0,
                maximum=1.0,
                value=0.5,
                step=0.1,
                interactive=True,
                label="Top p (used with nucleus sampling)",
            )

            min_seq_len = gr.Number(
                value=5, label="Minimum Sequence Length", precision=0, interactive=True
            )

            seq_len = gr.Number(
                value=20, label="Maximum Sequence Length (has to higher than Minimum)", precision=0, interactive=True
            )

        with gr.Column(scale=1):
            with gr.Column():
                caption_output = gr.Textbox(lines=1, label="Caption Output")
                caption_button = gr.Button(
                    value="Caption it!", interactive=True, variant="primary"
                )
                caption_button.click(
                    inference_caption,
                    [
                        image_input,
                        sampling,
                        rep_penalty,
                        top_p,
                        min_seq_len,
                        seq_len
                    ],
                    [caption_output],
                )

    examples = gr.Examples(
        examples=[path.as_posix() for path in paths],
        inputs=[image_input],
    )
iface.launch(share=True)
