# Builds heyai to be ready for use

import rich
import shutil
import os
from rich.panel import Panel
from rich.text import Text
from sys import argv

try:
    quickBuild = argv[1] == "!q"
except IndexError:
    quickBuild = False

console = rich.get_console()

console.print(Panel(
    "[red]WARNING:[/red] This [blue]will[/blue] add to path.\nType [green]y[/green] to [blue]accept[/blue]."
))

if not quickBuild: assert input("> ") == "y", "Add to Path required"

class Paths:
    root = os.curdir
    
    src = os.path.join(root, "src")
    backend = os.path.join(src, "backend")
    wrapper = os.path.join(src, "wrapper")
    
    dist = os.path.abspath(os.path.join(root, "dist"))
    
    dist_backend = os.path.join(dist, "backend")

## Build Process

### Move current backend to dist/

if os.path.isdir(Paths.dist): # check if dist is already created
    console.print("[red]WARNING:[/red] ./dist/ already exists. Are you sure you want to override it?\n[green]y[/green] to continue.")
    if not quickBuild:
        if not input("> ").lower() == "y":
            console.print("[red][bold]FATAL:[/bold][/red] Build Process ended. Overwriting ./dist/ declined.")
            quit()
    
    try:
        os.remove(Paths.dist)
    except PermissionError:
        os.chdir(Paths.root)
        os.system("rd dist /s /q")
        
    console.print("[green]./dist/ deleted.[/green]")

shutil.copytree(Paths.backend, Paths.dist_backend)


## Build Process for the wrapper