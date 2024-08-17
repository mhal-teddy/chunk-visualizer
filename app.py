import gradio as gr
from chunking import jina_ai_chunking

CHUNKING_MODEL = ["JinaAI (cl100k_base)"]

EXAMPLE_TEXT = (
    "The Forgotten Melody\n"
    "In the bustling city of New York, Sarah Thompson lived a life consumed by her career as a high-powered attorney. "
    "Her days were filled with endless meetings, court appearances, and late nights at the office. "
    "She had everything she thought she wanted - success, money, and respect from her peers. "
    "Yet, something was missing.One rainy evening, as Sarah hurried home from work, "
    "she stumbled upon a small, dimly lit music shop tucked away in a quiet alley. "
    "Intrigued, she stepped inside, the bell above the door announcing her arrival. "
    "The shop was filled with instruments of all kinds, their polished surfaces gleaming in the soft light. "
    "An elderly man appeared from the back room, his eyes twinkling with wisdom. \"Welcome,\" he said warmly. "
    "\"I'm Mr. Hartley. What brings you here on this dreary night?\" Sarah hesitated, unsure of why she had entered. "
    "\"I... I'm not sure. I just felt drawn to this place.\" "
    "Mr. Hartley nodded knowingly. \"Perhaps you're searching for something you've lost?\" "
    "He reached behind the counter and pulled out an old, worn violin case. "
    "\"This belonged to a young woman many years ago. She, too, had forgotten something important.\" "
    "As Sarah opened the case, she gasped. The violin inside was exquisite, its wood smooth and rich with age. "
    "Without thinking, she lifted it to her chin and drew the bow across the strings. "
    "A hauntingly beautiful melody filled the air, stirring long-forgotten memories. "
    "Tears welled in Sarah's eyes as she remembered the passion she once had for music, a dream she had abandoned in pursuit of her legal career. "
    "The melody spoke of lost dreams and rediscovered purpose. "
    "When the last note faded, Sarah looked up to find Mr. Hartley smiling gently. "
    "\"Sometimes,\" he said, \"we need a reminder of who we truly are.\" From that day forward, Sarah's life changed. "
    "She found balance between her successful career and her rekindled love for music. "
    "The forgotten melody had awakened her soul, reminding her that true fulfillment comes from embracing all aspects of oneself."
)


def split_chunk(prompt: str, chunking_model: str) -> list[tuple[str, str]]:
    if chunking_model == CHUNKING_MODEL[0]:
        sentences = jina_ai_chunking(prompt)
    else:
        raise NotImprementedError

    highlighted_sentences = []
    for i, sentence in enumerate(sentences):
        highlighted_sentences.append((sentence + " ", f"Chunk {i}"))
    return highlighted_sentences


with gr.Blocks() as demo:
    gr.Markdown("# Chunk Visualizer")
    gr.Markdown("Application that visualizes the results of chunk splitting")
    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(lines=5, max_lines=10)
            chunking_model = gr.Dropdown(CHUNKING_MODEL, label="Chunking Model")
            submit_button = gr.Button("Submit")
        with gr.Column():
            outputs = gr.HighlightedText(
                label="Output",
                show_legend=True,
            )
    submit_button.click(fn=split_chunk, inputs=[prompt, chunking_model], outputs=outputs)

    examples = gr.Examples(
        examples=[[EXAMPLE_TEXT, CHUNKING_MODEL[0]]],
        inputs=[prompt, chunking_model],
        outputs=outputs,
    )

demo.launch()