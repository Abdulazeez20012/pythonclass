class Entry:
    def __init__(self, entry_id, title, content):
        self.entry_id = entry_id
        self.title = title
        self.content = content

    def __str__(self):
        return f"ID: {self.entry_id}\nTitle: {self.title}\nContent: {self.content}"
