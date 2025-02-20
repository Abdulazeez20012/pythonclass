from Dsa_Function.diary import Diary

class Diaries:
    def __init__(self):
        self.diaries = {}

    def create_diary(self, diary_id):
        self.diaries[diary_id] = Diary(diary_id)

    def delete_diary(self, diary_id):
        if diary_id in self.diaries:
            del self.diaries[diary_id]
        else:
            raise ValueError("Diary not found")

    def get_diary(self, diary_id):
        if diary_id in self.diaries:
            return self.diaries[diary_id]
        else:
            raise ValueError("Diary not found")
