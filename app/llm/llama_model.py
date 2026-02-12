from llama_cpp import Llama
import os

class LlamaModel:

    def __init__(self, model_name="mistral-7b-instruct.Q4_K_M.gguf"):
        from app.config import Config

        model_path = os.path.join(Config.MODELS_DIR, model_name)
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found: {model_path}")

        self.model = Llama(
            model_path=model_path,
            n_ctx=4096,
            n_threads=8,
            verbose=False
        )

    def generate(self, prompt, max_tokens=200):
        response = self.model(prompt, max_tokens=max_tokens)
        return response["choices"][0]["text"]
