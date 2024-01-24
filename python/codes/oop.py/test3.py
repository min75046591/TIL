class Account:
    total_account = 0

    @classmethod
    def show_count(cls):
        pass

    def __init__(self, name):
        self.name = name
        Account.total_account = Account.total_account + 1

    def show_count(self):
        print(f'가입한 고객의 이름은 {self.name}이고, 총 계좌수는 {Account.total_account}입니다')

p1 = Account('민수')
p1.show_count()

p2 = Account('민주')
p2.show_count()

p3 = Account('민정')
p3.show_count()