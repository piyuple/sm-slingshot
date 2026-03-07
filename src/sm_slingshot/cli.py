import typer

from sm_slingshot.utils import setup_logging

app = typer.Typer(name="sm-slingshot", help="Sagemaker deployment tool", no_args_is_help=True)


@app.callback()
def main(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable debug logging"),
) -> None:
    setup_logging(verbose=verbose)
