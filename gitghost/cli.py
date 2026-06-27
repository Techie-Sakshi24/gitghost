"""
GitGhost CLI - Generate cinematic GitHub profile READMEs
"""

import os
import sys
import click
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.syntax import Syntax
from rich.table import Table
from rich import box

from gitghost.analyzer import get_github_data, build_profile_summary
from gitghost.generator import generate_readme

console = Console()


@click.command()
@click.argument("username", default="Techie-Sakshi24")
@click.option("--style", "-s",
              type=click.Choice(["cinematic", "minimal", "fun", "professional"]),
              default="cinematic", show_default=True,
              help="README style/tone")
@click.option("--output", "-o", default=None, metavar="FILE",
              help="Save README to file (e.g. README.md)")
@click.option("--github-token", envvar="GITHUB_TOKEN", default=None,
              help="GitHub token for higher API rate limits")
@click.option("--api-key", envvar="GROQ_API_KEY", default=None,
              help="Groq API key")
@click.option("--preview", is_flag=True, default=False,
              help="Show raw markdown preview in terminal")
@click.option("--stats", is_flag=True, default=False,
              help="Show detailed profile stats before generating")
def main(username, style, output, github_token, api_key, preview, stats):
    """
    \b
    GitGhost — cinematic GitHub README generator 👻

    Scans a GitHub profile and generates a personality-driven
    README.md using Groq AI (free).

    \b
    Examples:
      gitghost                               # generate for Techie-Sakshi24
      gitghost torvalds --style minimal
      gitghost Techie-Sakshi24 -o README.md
      gitghost Techie-Sakshi24 --style fun --preview
      gitghost Techie-Sakshi24 --stats
    """
    console.print()
    console.print(Rule("[bold cyan]GitGhost[/bold cyan] [dim]👻 cinematic README generator[/dim]"))
    console.print()

    # Step 1 - Fetch GitHub data
    console.print(f"[dim]Scanning GitHub profile:[/dim] [bold]@{username}[/bold]")
    try:
        data = get_github_data(username, token=github_token)
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)

    console.print(f"[dim]Found[/dim] [bold]{data['public_repos']}[/bold] [dim]repos ·[/dim] "
                  f"[bold]{data['total_stars']}[/bold] [dim]stars ·[/dim] "
                  f"[bold]{data['followers']}[/bold] [dim]followers[/dim]")

    top_langs = ", ".join(l for l, _ in data["top_languages"][:3])
    if top_langs:
        console.print(f"[dim]Top languages:[/dim] [bold]{top_langs}[/bold]")

    # Optional stats table
    if stats:
        console.print()
        table = Table(box=box.ROUNDED, border_style="dim", show_header=True, header_style="bold dim")
        table.add_column("Repo", style="bold")
        table.add_column("Stars", justify="right")
        table.add_column("Forks", justify="right")
        table.add_column("Language")
        table.add_column("Description", style="dim")
        for r in data["top_repos"]:
            table.add_row(
                r["name"],
                str(r["stars"]),
                str(r["forks"]),
                r["language"] or "—",
                r["description"][:50] if r["description"] else "—"
            )
        console.print(table)

    console.print()

    # Step 2 - Build summary
    profile_summary = build_profile_summary(data)

    # Step 3 - Generate README
    console.print(f"[dim]Generating[/dim] [bold]{style}[/bold] [dim]README with Groq AI...[/dim]")
    try:
        readme = generate_readme(profile_summary, style=style, api_key=api_key)
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)
    except Exception as e:
        console.print(f"[bold red]API error:[/bold red] {e}")
        sys.exit(1)

    console.print()

    # Step 4 - Output
    if preview:
        syntax = Syntax(readme, "markdown", theme="monokai", word_wrap=True)
        console.print(Panel(syntax, title="[bold]Generated README[/bold]", border_style="cyan"))
        console.print()

    if output:
        Path(output).write_text(readme, encoding="utf-8")
        console.print(f"[bold green]✓[/bold green] README saved to [bold]{output}[/bold]")
    else:
        console.print(Panel(
            f"[dim]Tip: Run with[/dim] [bold]-o README.md[/bold] [dim]to save, or[/dim] [bold]--preview[/bold] [dim]to see it here[/dim]",
            border_style="dim"
        ))
        print(readme)

    console.print()
    console.print(Rule("[dim]GitGhost 👻 — github.com/Techie-Sakshi24/gitghost[/dim]"))
    console.print()


if __name__ == "__main__":
    main()