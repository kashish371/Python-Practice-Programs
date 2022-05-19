#creating and defining class
class cars:
    def __init__(self, b_name, model, Type):
        self.b_name=b_name
        self.model=model
        self.Type=type
#creation of object
car1=cars("Maruti", "Caiz", "Sedan")
print("Model of car1 is : ",car1.model)
#print(car1)
