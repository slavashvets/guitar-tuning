"""CLI entry point for the guitar tuning analysis using Typer with locale support."""

# Standard library imports

# Third-party library imports
import typer
import yaml
from formulas import analyze_guitar
from i18n import create_fluent_wrapper

# Internal/local imports
from models import GuitarConfig
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

app = typer.Typer()


def load_config(config_file: str) -> dict:
    """Load YAML configuration from the specified file.

    Args:
        config_file: Path to the YAML configuration file.

    Returns:
        A dictionary with configuration data.
    """
    with open(config_file, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def display_analysis(result, _ ) -> None:
    """Display the guitar analysis results using Rich and localized labels.

    Args:
        result: The GuitarAnalysisResult to display.
        _: Function to retrieve localized strings.
    """
    console = Console()
    console.print(f"[bold underline]{_('guitar-tuning-analysis')}[/]\n")

    # Display analysis for each string
    for string in result.strings:
        title = _("string_title", name=string.name, open_freq=f"{string.open_freq:.1f}")
        table = Table(title=title)
        table.add_column(_("fret"), justify="center")
        table.add_column(_("deviation"), justify="center")
        for fret, dev in sorted(string.deviations.items()):
            table.add_row(str(fret), f"{dev:+0.1f}")
        console.print(table)

        details = (
            f"[bold]{_('grouped_averages')}[/]\n"
            f"{_('low', value=f'{string.avg_low:+0.1f}')}\n"
            f"{_('mid', value=f'{string.avg_mid:+0.1f}')}\n"
            f"{_('high', value=f'{string.avg_high:+0.1f}')}\n\n"
            f"[bold]{_('recommendations')}[/]\n"
            f"{_('saddle', recommendation=string.recommendation_saddle)}\n"
            f"{_('nut', recommendation=string.recommendation_nut)}\n"
            f"{_('bridge', recommendation=string.recommendation_bridge)}\n"
            f"{_('truss_diff', value=f'{string.truss_diff:+0.1f}')}"
        )
        console.print(Panel(details, title=f"{_('string')}: {string.name}", expand=False))

    overall_details = (
        f"[bold]{_('overall_recommendation')}[/]\n"
        f"{_('average_truss_diff', value=f'{result.overall_truss:+0.1f}')}\n\n"
        f"{result.overall_recommendation}"
    )
    console.print(Panel(overall_details, title=_("overall"), expand=False))


@app.command()
def analyze(
    config_file: str = typer.Argument(
        "config.yaml", help="Path to the YAML configuration file"
    ),
    lang: str = typer.Option(
        "en_US", "--lang", "-l", help="Locale (e.g., en_US or ru_RU)"
    ),
):
    """CLI command to analyze guitar tuning using the provided configuration file with localization."""
    config_data = load_config(config_file)
    _ = create_fluent_wrapper(lang)
    config = GuitarConfig.model_validate(config_data)
    analysis_result = analyze_guitar(config, 3.0, 2.0, _)
    display_analysis(analysis_result, _)


if __name__ == "__main__":
    app()
