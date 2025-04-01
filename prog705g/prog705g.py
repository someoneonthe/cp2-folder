class person:
    def __init__(self, fn, ln):
        self._first = fn
        self._last = ln

    def get_name(self):
        return self._first + " " + self._last

class student(person):
    def __init__(self, fn, ln, gpa):
        super().__inti__(fn, ln)
        self.gpa = gpa

class Teacher(person):
    def __init__(self, fn, ln, Num_stu):
        super().__inti__(fn, ln)
        self.Num_stu = Num_stu

class admin(person):
    def __init__(self, fn, ln, Fade_word):
        super().__inti__(fn, ln)
        self.Fade_word = Fade_word
        