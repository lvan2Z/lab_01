import typer

from . import calculator
from . import converter

app = typer.Typer()

@app.command()
def calc(expression: str):
    typer.echo(calculator.calc(expression))

@app.command()
def convert(value: int, unit1: str, unit2: str):
    typer.echo(converter.convert(value, unit1, unit2))

if __name__ == "__main__":
    app()

