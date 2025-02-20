from Dsa_Function.entry import Entry
class Entries:
    def __init__(self):
        self.entries = {}

    def create_entry(self, entry_id, title, content):
        self.entries[entry_id] = Entry(entry_id, title, content)

    def update_entry(self, entry_id, title, content):
        if entry_id in self.entries:
            self.entries[entry_id].title = title
            self.entries[entry_id].content = content
        else:
            raise ValueError("Entry not found")

    def delete_entry(self, entry_id):
        if entry_id in self.entries:
            del self.entries[entry_id]
        else:
            raise ValueError("Entry not found")

    def view_entry(self, entry_id):
        if entry_id in self.entries:
            return self.entries[entry_id]
        else:
            raise ValueError("Entry not found")

    def find_entry_by_id(self, entry_id):
        return self.view_entry(entry_id)

    def list_entries(self):
        return self.entries.values()
