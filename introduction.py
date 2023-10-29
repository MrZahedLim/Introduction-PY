# intro.py

class Introduction:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def introduce(self):
        intro = f"Hello, I am {self.name}! {self.description}"
        print(intro)


if __name__ == "__main__":
    intro_obj = Introduction("MrZahedLim", "I am a passionate learner and aspiring developer.")
    intro_obj.introduce()