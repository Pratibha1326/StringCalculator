class StringCalculator:
    def add(self, numbers: str)-> int:
        if numbers == "":
           return 0
        
        if "," in numbers:
            numbers = numbers.replace("\n", ",")
            nums = [int(num) for num in numbers.split(",")]
            return sum(nums)

        delimiter = ","    
        if numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers[4:]
        numbers = numbers.replace("\n", delimiter)
        nums = numbers.split(delimiter)
        nums = [int(num) for num in nums]
        return sum(nums)
        