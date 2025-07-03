class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        x = celsius + 273.15
        y = celsius * 1.80 + 32.00
        lst = []
        lst.append(x)
        lst.append(y)
        return lst
        
