"""
Simple Python Application for Jenkins Pipeline Demo
"""
import datetime
from typing import List, Union


class Calculator:
    """A simple calculator class with basic operations."""
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        return a + b
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract two numbers."""
        return a - b
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class GreetingService:
    """A service for generating greetings."""
    
    def __init__(self, name: str = "World"):
        self.name = name
    
    def get_greeting(self) -> str:
        """Get a greeting message."""
        return f"Hello {self.name} from Jenkins Pipeline!"
    
    def get_current_time(self) -> str:
        """Get current timestamp."""
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def is_weekend(self, date: datetime.date = None) -> bool:
        """Check if the given date (or today) is a weekend."""
        if date is None:
            date = datetime.date.today()
        return date.weekday() >= 5  # Saturday=5, Sunday=6


class ListUtils:
    """Utility functions for list operations."""
    
    @staticmethod
    def filter_even_numbers(numbers: List[int]) -> List[int]:
        """Filter even numbers from a list."""
        return [num for num in numbers if num % 2 == 0]
    
    @staticmethod
    def find_max(numbers: List[Union[int, float]]) -> Union[int, float]:
        """Find maximum number in a list."""
        if not numbers:
            raise ValueError("List cannot be empty")
        return max(numbers)
    
    @staticmethod
    def calculate_average(numbers: List[Union[int, float]]) -> float:
        """Calculate average of numbers in a list."""
        if not numbers:
            raise ValueError("List cannot be empty")
        return sum(numbers) / len(numbers)


def main():
    """Main function to demonstrate the application."""
    # Calculator demo
    calc = Calculator()
    print("=== Calculator Demo ===")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    
    # Greeting service demo
    greeting_service = GreetingService("Jenkins")
    print("\n=== Greeting Service Demo ===")
    print(greeting_service.get_greeting())
    print(f"Current time: {greeting_service.get_current_time()}")
    print(f"Is today weekend? {greeting_service.is_weekend()}")
    
    # List utilities demo
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("\n=== List Utilities Demo ===")
    print(f"Original numbers: {numbers}")
    print(f"Even numbers: {ListUtils.filter_even_numbers(numbers)}")
    print(f"Maximum: {ListUtils.find_max(numbers)}")
    print(f"Average: {ListUtils.calculate_average(numbers):.2f}")


if __name__ == "__main__":
    main()
