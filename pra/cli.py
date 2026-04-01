from click import help_option
import typer

app = typer.Typer()


@app.command()
def hello():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, "hello", "help_option", "ss"]
    print(a)
    print("Hello")


@app.command()
def goodby():
    print("goodbye")


if __name__ == "__main__":
    app()
