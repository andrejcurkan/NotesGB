from storage.file_note_storage import FileNoteStorage

class NoteService:
    def __init__(self, storage=FileNoteStorage()):
        self.storage = storage

    def create_note(self, title: str, content: str) -> None:
        self.storage.create(title, content)

    def read_notes(self) -> list:
        return self.storage.read_all()

    def read_note(self, title: str) -> str:
        return self.storage.read(title)

    def update_note(self, title: str, content: str) -> bool:
        return self.storage.update(title, content)

    def delete_note(self, title: str) -> bool:
        return self.storage.delete(title)
