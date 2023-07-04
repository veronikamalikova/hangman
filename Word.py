import random


class Word:
    common_nouns = [
        "time",
        "year",
        "people",
        "way",
        "day",
        "man",
        "thing",
        "woman",
        "life",
        "child",
        "world",
        "school",
        "state",
        "family",
        "student",
        "group",
        "country",
        "problem",
        "hand",
        "part",
        "place",
        "case",
        "week",
        "company",
        "system",
        "program",
        "question",
        "work",
        "government",
        "number",
        "night",
        "point",
        "home",
        "water",
        "room",
        "mother",
        "area",
        "money",
        "story",
        "fact",
        "month",
        "lot",
        "right",
        "study",
        "book",
        "eye",
        "job",
        "word",
        "business",
        "issue",
        "side",
        "kind",
        "head",
        "house",
        "service",
        "friend",
        "father",
        "power",
        "hour",
        "game",
        "line",
        "end",
        "member",
        "law",
        "car",
        "city",
        "community",
        "name",
        "president",
        "team",
        "minute",
        "idea",
        "kid",
        "body",
        "information",
        "back",
        "parent",
        "face",
        "others",
        "level",
        "office",
        "door",
        "health",
        "person",
        "art",
        "war",
        "history",
        "party",
        "result",
        "change",
        "morning",
        "reason",
        "research",
        "girl",
        "guy",
        "moment",
        "air",
        "teacher",
        "force",
        "education"
    ]

    # creating a word guessed by the player
    def get_random_word(self):
        word = random.choice(self.common_nouns)
        return word.lower()

    def is_letter_in_word(self, letter, word):
        index = word.find(letter)
        return index != -1

    def get_hidden_word(self, word, guessed):
        result = []
        for letter in word:
            if letter in guessed:
                result.append(letter)
            else:
                result.append("_")
        return " ".join(result)

    def is_winner(self, word, guessed):
        for letter in word:
            if letter not in guessed:
                return False
        return True
