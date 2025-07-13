from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

console.print(
    Panel(
        Text("Let's get started with your private \"Vibe Coding\" assistant.", justify="center"),
        title="[green]Welcome to HeyAI![/green]",
        expand=True,
    )
)
