class StringCalculator:
    def add(self, numbers: str)-> int:
        if numbers == "":
           return 0
        
        delimiter = ","
        if numbers.startswith("//["):
            end_delimiter = numbers.find("]\n")
            delimiter = numbers[3:end_delimiter]
            numbers = numbers[end_delimiter + 2:]
            numbers = numbers.replace("\n", delimiter)
        elif numbers.startswith("//"):
            delimiter = numbers[2]
            numbers = numbers[4:]
            numbers = numbers.replace("\n", delimiter)
        else:
            # Handle default case where \n acts as a delimiter
            numbers = numbers.replace("\n", delimiter)
        nums = [int(num) for num in numbers.split(delimiter) if int(num) <= 1000]

        negatives = [num for num in nums if num < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

        return sum(nums)

        if "," in numbers or "\n" in numbers:
            numbers = numbers.replace("\n", ",")
            nums = [int(num) for num in numbers.split(",") if int(num) <= 1000]
            return sum(nums)

        