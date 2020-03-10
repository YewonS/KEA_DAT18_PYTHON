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

    
class Papertray():

    def __init__(self, papers):
        self.__isEmpty = False
        self.__papers = papers

    @property
    def isEmpty(self):
        return self.__isEmpty

    @property
    def papers(self):
        return self.__papers

    @isEmpty.setter
    def isEmpty(self, empty):
        self.__isEmpty = empty

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
            self.__papers += 10


class Printer(Machine):
    
    def __init__(self, machine, papertray):
        # If you inherit one class, you can do it this way
        # super().__init(model)
        # If you inherit multiple classes, you can do this way
        # Machine.__init__(self, model):
        papers = Papertray(10)
        Machine.__init__(self, machine)
        Papertray.__init__(self, papertray)

    if __name__ == "__main__":
        printer = Printer()
        print(f"There are {printer.papers} papers on the paper tray.")
        print(f"If you want to proceed, turn on the machine.")
        userInput = input("Type in 'on' to turn on the machine: ")
        if userInput.lower() == 'on':
            Machine.power = 'on'
            print("The printer is on.")
        
        newInput = input("Type in 'off' to turn off the machine. Type 'print' to print: ")
        while (newInput.lower() != 'off'):
            if newInput == 'print':
                printer.papers.papers(1)
                print(f"Print completed. {papers.papers} papers left on the paper tray.")
            else:
                print("Invalid access. Try again.")

