class ConversationMemory:

    def __init__(self):
        self.sessions = {}

    def add_message(self, user_id: str, role: str, content: str):
        if user_id not in self.sessions:
            self.sessions[user_id] = []
        self.sessions[user_id].append({"role": role, "content": content})

    def get_context(self, user_id: str, max_messages=10):
        if user_id not in self.sessions:
            return ""
        messages = self.sessions[user_id][-max_messages:]
        return "\n".join([f"{m['role'].upper()}: {m['content']}" for m in messages])
