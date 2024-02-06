# 아래 클래스를 수정하시오.
class StringRepeater:
    def repeat_string(self, repeat, str_1):
        self.repeat = repeat
        self.str_1 = str_1
        for i in range(self.repeat):
            print(self.str_1)

    


repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")