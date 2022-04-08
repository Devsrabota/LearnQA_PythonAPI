#
class TestExample:
    def test_input(self):
     phrase = input("Set Phrase : ")
     per_phrase = str(phrase)
     assert 15 >= len(per_phrase),f"error len > 15 '{per_phrase}'"
