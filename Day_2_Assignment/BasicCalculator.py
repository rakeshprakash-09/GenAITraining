from rich.console import Console
from rich.prompt import Prompt

console = Console()

def basic_calculator():
    console.print("\n[bold cyan]Welcome to the Basic Calculator[/bold cyan]\n")

    try:
        num1 = float(Prompt.ask("Enter the first number"))
        num2 = float(Prompt.ask("Enter the second number"))
        operation = Prompt.ask("Choose an operation", choices=["+", "-", "*", "/"])

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                console.print("[bold red]Error:[/bold red] Division by zero is not allowed.")
                return

        console.print(f"\n[green]Result:[/green] {num1} {operation} {num2} = [bold yellow]{result}[/bold yellow]")

    except ValueError:
        console.print("[bold red]Invalid input. Please enter numeric values only.[/bold red]")

if __name__ == "__main__":
    basic_calculator()
