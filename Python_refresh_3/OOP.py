class BaseModel:
    def __init__(self, name):
        self.name = name
    def prifict(self, x):
        raise NotImplementedError("Subclasses must implement this method.")
    
class LinearModel(BaseModel):
    def __init__(self, name, weight, bias):
        super().__init__(name)
        self.weight = weight
        self.bias = bias    
    
    def prifict(self, x):
        return self.weight * x + self.bias
model = LinearModel("Linear Regression", weight = 2, bias = 1)
print(model.prifict(5))  # Output: 11