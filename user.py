class user:
    def __init__(self, username,email_address):
        self.name = username
        self.email = email_address
        self.account_balance =0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrow(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print("hello",self.name, "your net Available Balance is", self.account_balance)
    def transfer_money(self, amount):
        self.account_balance -= amount
elias = user ("Elias W" , "elias.woldeselassie@gmail.com")
jone = user ("jone dan" , "jone_dan@gmail.com")
jappy = user ("jappy assfa" , "jappy_a@gmail.com")

elias.make_deposit(200)
elias.make_deposit(400)
elias.make_deposit(300)
elias.make_withdrow(150)
elias.display_user_balance()

jone.make_deposit(2000)
jone.make_deposit(1000)
jone.make_withdrow(400)
jone.make_withdrow(150)
jone.display_user_balance()

jappy.make_deposit(4000)
jappy.make_withdrow(300)
jappy.make_withdrow(400)
jappy.make_withdrow(600)
jappy.display_user_balance()