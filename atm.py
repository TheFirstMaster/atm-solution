class ATM :
    def __init__(self, bank_name, balance):
        self.bank_name = bank_name
        self.balance = balance
        print "Welcome to {} Bank, Current balance is  {} $ ".format(bank_name, balance)



    def withdraw(self, request):
        self.request = request
        if request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            self.balance -= request
            while request > 0:

                if request >= 100:
                    request -= 100
                    print("give 100")

                elif request >= 50:
                    request -= 50
                    print("give 50")

                elif request >= 20:
                    request -= 20
                    print("give 20")

                elif request >= 10:
                    request -= 10
                    print("give 10")

                elif request >= 5:
                    request -= 5
                    print("give 5")

                elif request < 5:
                    print("give " + str(request))
                    request = 0
                    print "the new balance = " , balance
                    return balance
            print "You are Welcome"

s1 = ATM('ak', 9000)
s1.withdraw(2000)
