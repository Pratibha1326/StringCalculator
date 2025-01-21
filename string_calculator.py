class StringCalculator:
    def add(self, numbers: str)-> int:
        if numbers == "":
           return 0
        
        if "," in numbers:
            
            nums = [int(num) for num in numbers.split(",")]
            return sum(nums)

        return int(numbers)
        