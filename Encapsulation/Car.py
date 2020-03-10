class Car:
    
    def __init__(self, make, model, bhp, mph):
        self.__make = make
        self.__model = model
        self.__bhp = bhp
        self.__mph = mph

    # getters
    @property
    def make(self):
        return self.__make
    
    @property
    def model(self):
        return self.__model
    
    @property
    def bhp(self):
        return self.__bhp

    @property
    def mph(self):
        return self.__mph

    # setters
    @make.setter
    def make(self, make):
        if(make[0].lower() != self.__make[0]):
            print("Nope, you can't do this :P")
        else:
            self.__make = make
    
    @model.setter
    def model(self, model):
        self.__model = model

    @bhp.setter
    def bhp(self, bhp):
        self.__bhp = bhp

    @mph.setter
    def mph(self, mph):
        self.__mph = mph

    