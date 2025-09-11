import json
import os

class CandidateDB:
    def __init__(self, file_path="data/candidates.json"):
        self.file_path = file_path
        self.candidates = self._load()

    def _load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def add_candidate(self, name, role, skills, status="Applied"):
        candidate = {
            "name": name,
            "role": role,
            "skills": skills,
            "status": status
        }
        self.candidates.append(candidate)
        self._save()

    def update_status(self, name, status):
        for c in self.candidates:
            if c["name"].lower() == name.lower():
                c["status"] = status
        self._save()

    def list_candidates(self, role=None):
        if role:
            return [c for c in self.candidates if c["role"].lower() == role.lower()]
        return self.candidates

    def _save(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.candidates, f, indent=4)
