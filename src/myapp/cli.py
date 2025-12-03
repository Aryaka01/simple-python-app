"""
Command Line Interface for the Simple Python App
"""
import argparse
import sys
from .app import Calculator, GreetingService, ListUtils


def create_parser():
    """Create command line argument parser."""
    parser = argparse.ArgumentParser(description="Simple Python App CLI")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Calculator commands
    calc_parser = subparsers.add_parser('calc', help='Calculator operations')
    calc_parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'])
    calc_parser.add_argument('a', type=float, help='First number')
    calc_parser.add_argument('b', type=float, help='Second number')
    
    # Greeting commands
    greet_parser = subparsers.add_parser('greet', help='Greeting operations')
    greet_parser.add_argument('--name', default='World', help='Name to greet')
    greet_parser.add_argument('--time', action='store_true', help='Show current time')
    
    return parser


def main():
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    if args.command == 'calc':
        calc = Calculator()
        if args.operation == 'add':
            result = calc.add(args.a, args.b)
        elif args.operation == 'subtract':
            result = calc.subtract(args.a, args.b)
        elif args.operation == 'multiply':
            result = calc.multiply(args.a, args.b)
        elif args.operation == 'divide':
            try:
                result = calc.divide(args.a, args.b)
            except ValueError as e:
                print(f"Error: {e}")
                sys.exit(1)
        
        print(f"Result: {result}")
    
    elif args.command == 'greet':
        service = GreetingService(args.name)
        print(service.get_greeting())
        if args.time:
            print(f"Current time: {service.get_current_time()}")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
