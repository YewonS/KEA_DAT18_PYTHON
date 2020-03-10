class Machine:

    def __init(self):
        self.__power = 'off'
    
    @property
    def power(self):
        return self.__power
    
    @power.setter
    def power(self, power):
        if power.lower() == 'on':
            self.__power = power
        elif power.lower() == 'off':
            self.__power = power
        else:
            print("There is no option other than on or off")
    

class Paper:

    def __init__(self):
        self.__amount = 10
    
    @property
    def amount(self):
        return self.amount
    
    @amount.setter
    def amount(self, quantity):
        self.__amount = self.__amount - quantity

    
class Papertray(Paper):

    def __init__(self):
        super().__init(paper)
        self.__isEmpty = False
        self.__papers = 3
    
    @property
    def paper(self):
        return self._Paper__amount
    
    @property
    def isEmpty(self):
        return self.__isEmpty

    @property
    def papers(self):
        return self.__papers

    @paper.setter
    def paper(self, quantity):
        self._Paper__amount(quantity)

    @isEmpty.setter
    def isEmpty(self, empty):
        if paper == 0:
            pass

    @papers.setter
    def papers(self, papersUsed):
        if self.__papers > 0:
            self.__papers = self.__papers - papersUsed
            print(f"There are {self.__papers} left on the paper tray.")
        else:
            loadPaper()

    def loadPaper(self):
        if self.__papers > 0:
            pass
        else:
            paper = Paper()
            paper.amount = paper.amount(paper, 3)
            self.papers = 3


class Printer(Machine, Papertray):
    
    def __init__(self, machine, papertray):
        # If you inherit one class, you can do it this way
        # super().__init(model)
        # If you inherit multiple classes, you can do this way
        # Machine.__init__(self, model):
        Machine.__init__(self, machine)
        Papertray.__init__(self, papertray)

    if __name__ == "__main__":
        print(f"There are {Papertray.papers} papers on the paper tray.")
        print(f"If you want to proceed, turn on the machine.")
        userInput = input("Type in 'on' to turn on the machine: ")
        if userInput.lower() == 'on':
            Machine.power = 'on'
            print("The printer is on.")
        
        newInput = input("Type in 'off' to turn off the machine. Type 'print' to print: ")
        while (newInput.lower() != 'off'):
            if newInput == 'print':
                papertray = Papertray()
                Papertray.papers(1)
                print(f"Print completed. {Papertray.amount} papers left on the paper tray.")
            else:
                print("Invalid access. Try again.")

