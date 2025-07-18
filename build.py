# Builds heyai to be ready for use

import rich
from rich.panel import Panel
from rich.text import Text

console = rich.get_console()

console.print(Panel(
    "[red]WARNING:[/red] This [blue]will[/blue] add to path.\nType [green]y[/green] to [blue]accept[/blue]."
))

assert input("> ") == "y", "Add to Path required"
    