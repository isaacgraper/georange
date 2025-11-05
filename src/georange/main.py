import typer

from georange.features.spatial import average_distance, distance, nearest_point
from georange.io.reader import read

app = typer.Typer(help="georange CLI — Geospatial analysis toolkit")

state = {"geosets": None}


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    source: str = typer.Argument(..., help="Path to the geospatial file (e.g., .kml)"),
):
    """
    georange CLI entrypoint. Specify the source file and then a subcommand.
    """
    geosets = read(source)
    ctx.obj = {"geosets": geosets}

    if ctx.invoked_subcommand is None:
        for g in geosets:
            typer.echo(f"- {g.name}: {g.coord}")


@app.command()
def analyze(ctx: typer.Context):
    """
    List all loaded geospatial points.
    """

    geosets = ctx.obj["geosets"]
    for i, g in enumerate(geosets):
        typer.echo(f"{i} - {g.name}: {g.coord}")


@app.command()
def distances(ctx: typer.Context):
    """
    Compute pairwise distances.
    """

    geosets = ctx.obj["geosets"]
    typer.echo("[bold green]Pairwise distances (km):[/bold green]")

    for i, a in enumerate(geosets):
        for b in geosets[i + 1 :]:
            typer.echo(f"{a.name} ↔ {b.name}: {distance(a, b):.2f} km")


@app.command()
def nearest(
    ctx: typer.Context, target: int = typer.Option(0, help="Index of target point")
):
    """
    Find the nearest point to the given target.
    """

    geosets = ctx.obj["geosets"]
    target = geosets[target]
    nearest_pt = nearest_point([g for g in geosets if g != target], target)

    typer.echo(f"Nearest to {target.name}: {nearest_pt.name}")


@app.command()
def avgdist(ctx: typer.Context):
    """
    Compute the average distance.
    """

    geosets = ctx.obj["geosets"]
    avg = average_distance(geosets)

    typer.echo(f"Average distance: {avg:.2f} km")


if __name__ == "__main__":
    app()
