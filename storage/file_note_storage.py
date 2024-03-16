import os
from .note_storage import NoteStorage

class FileNoteStorage(NoteStorage):
    NOTES_DIR = "notes"

    def __init__(self):
        self._initialize_notes_dir()

    def _initialize_notes_dir(self):
        if not os.path.exists(self.NOTES_DIR):
            os.makedirs(self.NOTES_DIR)

    def create(self, title: str, content: str) -> None:
        note_filename = os.path.join(self.NOTES_DIR, f"{title}.txt")
        with open(note_filename, "w") as note_file:
            note_file.write(content)

    def read_all(self) -> list:
        notes = []
        for filename in os.listdir(self.NOTES_DIR):
            with open(os.path.join(self.NOTES_DIR, filename), "r") as note_file:
                title = os.path.splitext(filename)[0]
                content = note_file.read()
                notes.append({"title": title, "content": content})
        return notes

    def read(self, title: str) -> str:
        note_filename = os.path.join(self.NOTES_DIR, f"{title}.txt")
        if os.path.exists(note_filename):
            with open(note_filename, "r") as note_file:
                return note_file.read()
        else:
            return None

    def update(self, title: str, content: str) -> bool:
        note_filename = os.path.join(self.NOTES_DIR, f"{title}.txt")
        if os.path.exists(note_filename):
            with open(note_filename, "w") as note_file:
                note_file.write(content)
            return True
        else:
            return False

    def delete(self, title: str) -> bool:
        note_filename = os.path.join(self.NOTES_DIR, f"{title}.txt")
        if os.path.exists(note_filename):
            os.remove(note_filename)
            return True
        else:
            return False
