import json
import os

class HRMemory:
    def __init__(self, file_path="memory/state.json"):
        self.file_path = file_path
        self.memory = self._load_memory()

    def _load_memory(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def save_context(self, key, value):
        self.memory[key] = value
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.memory, f, indent=4)

    def get_context(self, key, default=None):
        return self.memory.get(key, default)

    def clear(self):
        self.memory = {}
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
