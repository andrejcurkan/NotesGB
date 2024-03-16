from service.note_service import NoteService

if __name__ == "__main__":
    note_service = NoteService()

    while True:
        print("\nNote Taking App")
        print("1. Create Note")
        print("2. Read Notes")
        print("3. Read Note")
        print("4. Update Note")
        print("5. Delete Note")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            note_service.create_note(title, content)
            print("Note created successfully.")

        elif choice == "2":
            notes = note_service.read_notes()
            if notes:
                print("List of Notes:")
                for index, note in enumerate(notes):
                    print(f"{index + 1}. {note['title']}")
            else:
                print("No notes found.")

        elif choice == "3":
            title = input("Enter note title to read: ")
            note = note_service.read_note(title)
            if note:
                print(f"Note: {note}")
            else:
                print("Note not found.")

        elif choice == "4":
            title = input("Enter note title to update: ")
            content = input("Enter updated content: ")
            if note_service.update_note(title, content):
                print("Note updated successfully.")
            else:
                print("Note not found.")

        elif choice == "5":
            title = input("Enter note title to delete: ")
            if note_service.delete_note(title):
                print("Note deleted successfully.")
            else:
                print("Note not found.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
