class StringCalculator:
    def add(self, numbers: str)-> int:
        if numbers == "":
           return 0
        
        if "," in numbers:
            
            returns int(numbers[0]) + int(numbers[1])

        return int(numbers)
        