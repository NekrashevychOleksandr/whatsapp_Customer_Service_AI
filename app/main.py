from app.llm.llama_model import LlamaModel
from app.memory.conversation_memory import ConversationMemory
from app.config import Config
from queue import Queue
from threading import Thread
import pyttsx3

# Setup
model = LlamaModel()
memory = ConversationMemory()
TTS_queue = Queue()

# TTS Worker
def TTS_worker():
    engine = pyttsx3.init()
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    while True:
        sentence = TTS_queue.get()
        if sentence is None:
            break
        engine.say(sentence)
        engine.runAndWait()
        TTS_queue.task_done()

Thread(target=TTS_worker, daemon=True).start()

def generate_and_speak(user_id, prompt):
    context = memory.get_context(user_id)
    full_prompt = context + "\nASSISTANT: " + prompt
    response = model.generate(full_prompt)
    memory.add_message(user_id, "assistant", response)
    TTS_queue.put(response)
    return response

if __name__ == "__main__":
    user_id = "test_user"
    while True:
        user_input = input("YOU: ")
        if user_input.lower() in ["exit", "quit"]:
            TTS_queue.put(None)  # Stop TTS worker
            break
        memory.add_message(user_id, "user", user_input)
        reply = generate_and_speak(user_id, user_input)
        print(f"AI: {reply}")
