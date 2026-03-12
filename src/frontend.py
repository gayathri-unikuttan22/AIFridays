import gradio as gr
from src.backend import process_question

def create_ui(qa_chain):
    def chat(chat_history, user_input):
        answer = process_question(user_input, qa_chain)
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": answer})
        return chat_history

    with gr.Blocks() as demo:
        gr.Markdown('# HR Policies Bot')

        with gr.Tab("Ask Chatbot"):
            chatbot = gr.Chatbot(height=300)
            message = gr.Textbox(label='Please type your query and press Enter.')
            clear = gr.ClearButton([message, chatbot])

            message.submit(chat, [chatbot, message], chatbot)
            message.submit(lambda: gr.update(value=""), None, [message])

    return demo
