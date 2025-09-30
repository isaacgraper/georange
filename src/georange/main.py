from io import read

import typer

app = typer.Typer()


@app.command()
def process(source: str = typer.Argument(..., help="Geospatial file path")):
    """
    Process a file and extract placemarks.
    """
    file = read(source, layer=None)

    return print(file.head())


if __name__ == "__main__":
    app()
