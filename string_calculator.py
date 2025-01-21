import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        # Handle multiple delimiters and delimiters of any length
        if numbers.startswith("//"):
            delimit_section, numbers = numbers.split("\n", 1)
            delimit = self._extract_delimiters(delimit_section)
            numbers = numbers.replace("\n", ",")

            # Replace custom delimiters with comma
            for delimiter in delimit:
                numbers = numbers.replace(delimiter, ",")
        else:
            # Case where commas and newlines are the delimiters
            numbers = numbers.replace("\n", ",")

        # Split numbers and filter out those greater than 1000
        nums = [int(num) for num in numbers.split(",") if num and int(num) <= 1000]

        # Check for negative numbers and raise an error if found
        negatives = [num for num in nums if num < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

        return sum(nums)

    def _extract_delimiters(self, delimiter_section: str):
        """Extracts delimiters from the delimiter section of the input."""
        # Match for single or multiple delimiters (e.g., [*], [***], [*][%])
        delimiters = re.findall(r'\[([^\]]+)\]', delimiter_section)
        if not delimiters:
            # In case no delimiters are found, default to a single character delimiter
            delimiters = [delimiter_section[2:]]
        return delimiters

