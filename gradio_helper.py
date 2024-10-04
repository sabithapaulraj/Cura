# osteoarthritis_chatbot.py

import gradio as gr
from uuid import uuid4
from typing import Callable, Literal
import time

# Example Osteoarthritis context for English
english_examples = [
    ["What is Osteoarthritis?"],
    ["What are the symptoms of Osteoarthritis?"],
    ["How is Osteoarthritis diagnosed?"],
    ["What treatments are available for Osteoarthritis?"],
    ["What lifestyle changes can help manage Osteoarthritis?"],
    ["Explain the relationship between Osteoarthritis and joint pain."],
    ["Write a blog post on 'Latest Research in Osteoarthritis Treatments'."]
]

def get_uuid():
    """Universal unique identifier for thread"""
    return str(uuid4())

def handle_user_message(message, history):
    """Callback function for updating user messages and adding a bot reply"""
    # Append user's message to history
    history = history + [[message, ""]]

    # Simulate bot's response (for now, it's just a placeholder text)
    bot_reply = "This is a simulated response for: " + message

    # Append the bot's response to the chat history
    history[-1][1] = bot_reply

    return "", history  # Clear input box and return updated history

def make_demo(run_fn: Callable, stop_fn: Callable, title: str = "Osteoarthritis Diagnostic Interface", language: Literal["English"] = "English"):
    examples = english_examples

    with gr.Blocks(
        theme=gr.themes.Soft(),
        css="""
        body { background: linear-gradient(135deg, #f0f4c3, #e1f5fe); font-family: 'Arial', sans-serif; color: #333; }
        .header { text-align: center; margin-bottom: 20px; }
        .glow-text { color: #d32f2f; text-shadow: 0 0 10px #d32f2f, 0 0 20px #d32f2f; font-size: 24px; font-weight: bold; }
        h1 { color: #c2185b; text-shadow: 2px 2px 10px #880e4f; }
        .gr-button { background-color: #c2185b; border: 1px solid #880e4f; color: white; }
        .gr-button:hover { background-color: #880e4f; }
        .gr-textbox, .gr-slider-container { background-color: #fff; color: black; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); }
        .gr-box { padding: 20px; border-radius: 10px; margin-bottom: 20px; }
        .info-section { padding: 20px; background: #880e4f; border-radius: 10px; color: white; }
        footer { text-align: center; margin-top: 20px; }
        .gr-chatbot { background-color: #f9f9f9; height: 500px; border: 1px solid #e0e0e0; border-radius: 10px; }
        """,
    ) as demo:
        conversation_id = gr.State(get_uuid)

        # Header Section
        with gr.Row():
            gr.Markdown(f"""<h1>💻 Osteoarthritis Diagnostic Interface 🌐</h1>""", elem_classes="header")

        with gr.Row():
            # Left side for image upload and chatbot
            with gr.Column(scale=3):
                with gr.Row():
                    # Image Upload Section
                    with gr.Column(scale=1):
                        gr.Markdown("### Upload Image for Osteoarthritis Diagnosis")
                        image_input = gr.Image(label="Upload an Image", type="pil")

                        # Placeholder for classification status
                        classification_status = gr.Markdown("")

                    # Chat Message Box and Buttons
                    with gr.Column(scale=2):
                        msg = gr.Textbox(
                            label="Chat Message Box",
                            placeholder="Type your message here...",
                            show_label=False,
                            container=False,
                        )
                        chatbot = gr.Chatbot(label="Chat", height=500)

                        with gr.Row():
                            submit = gr.Button("Chat")
                            stop = gr.Button("Stop")
                            clear = gr.Button("Clear")
                            classify = gr.Button("Classify", elem_id="classify_button")

                # Advanced options section
                with gr.Accordion("Advanced Options:", open=False):
                    with gr.Row():
                        with gr.Column():
                            temperature = gr.Slider(
                                label="Temperature", value=0.1, minimum=0.0, maximum=1.0, step=0.1,
                                interactive=True, info="Higher values produce more diverse outputs",
                            )
                        with gr.Column():
                            top_p = gr.Slider(
                                label="Top-p (nucleus sampling)", value=1.0, minimum=0.0, maximum=1.0, step=0.01,
                                interactive=True, info="Sample from a set of tokens whose cumulative probability exceeds top_p.",
                            )
                        with gr.Column():
                            top_k = gr.Slider(
                                label="Top-k", value=50, minimum=0.0, maximum=200, step=1,
                                interactive=True, info="Sample from a shortlist of top-k tokens.",
                            )
                        with gr.Column():
                            repetition_penalty = gr.Slider(
                                label="Repetition Penalty", value=1.1, minimum=1.0, maximum=2.0, step=0.1,
                                interactive=True, info="Penalize repetition — 1.0 to disable.",
                            )

                # Examples section
                gr.Examples(examples, inputs=msg, label="Click on any example and press the 'Chat' button")

            # Right section for About Osteoarthritis
            with gr.Column(scale=1):
                gr.Markdown("""
                    <div class="info-section">
                        <h2 style='text-align: center;'>About Osteoarthritis Chatbot</h2>
                        <p>This chatbot provides information about <b>Osteoarthritis</b>, a common joint disorder that causes pain and stiffness. It can assist with diagnosis information, treatment options, and management strategies.</p>
                        <ul style='text-align: left;'>
                            <li>🚀 <b>Information on Osteoarthritis</b></li>
                            <li>⚡ <b>Diagnostic assistance</b> based on uploaded images</li>
                            <li>🩺 <b>Guidance on treatment and management</b></li>
                        </ul>
                    </div>
                """, elem_classes="info-section")

        # Footer Section
        with gr.Row():
            gr.Markdown(f"""<footer class="glow-text">✨ Built by Med Squad: Osteoarthritis AI Project © 2024 ✨</footer>""")

        # Function to handle classification
        def delayed_classification():
            time.sleep(5)
            return "Diagnosis: Osteoarthritis risk assessment in progress..."

        # Function to clear the chat history
        def clear_chat():
            return ""

        # Linking buttons to functions
        submit.click(handle_user_message, inputs=[msg, chatbot], outputs=[msg, chatbot])
        classify.click(fn=delayed_classification, inputs=[], outputs=[classification_status])
        clear.click(fn=clear_chat, inputs=[], outputs=[chatbot])

    return demo
