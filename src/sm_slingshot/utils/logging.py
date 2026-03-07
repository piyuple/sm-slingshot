import logging

from rich.console import Console
from rich.logging import RichHandler

console = Console(stderr=True)


def setup_logging(verbose: bool = False) -> None:
    """Configure logging for the app

    Args:
        verbose: if True, sets log level to debug. Otherwise info.
    """
    level = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%x]",
        handlers=[
            RichHandler(console=console, rich_tracebacks=True, show_path=verbose, markup=True)
        ],
    )


def get_logger(name: str) -> logging.Logger:
    """Get a logger for a module

    Args:
        name: __name__ from the calling module

    Returns:
        instance of Logger
    """
    return logging.getLogger(name)
