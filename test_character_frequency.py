import unittest

from character_frequency import CharacterFrequency


class TestCharacterFrequency(unittest.TestCase):

    def test_empty_string(self):
        characterFrequency = CharacterFrequency("")
        result =  characterFrequency.count_characters()
        self.assertEqual(result, {})

    def test_for_single_Character_of_string_eg_a_1(self):
        characterFrequency  = CharacterFrequency("a")
        result =  characterFrequency .count_characters()
        self.assertEqual(result, {'a': 1})

    def test_for_multiple_charcters_of_string_it_should_return_the_number_of_character_frequency(self):
        characterFrequency = CharacterFrequency("Semicolon.africa")
        result = characterFrequency.count_characters()
        self.assertEqual(result,{'S':1,'e':1,'m':1,'i':2,'c':2,'o':2,'l':1,'n':1,'a':2,'f':1,'r':1,'.':1})

    def test_for_case_sensitive_in_the_strings(self):
        characterFrequency = CharacterFrequency("BIbi")
        result = characterFrequency.count_characters()
        self.assertEqual(result,{'B':1,'I':1,'b':1,'i':1})

        