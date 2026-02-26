# src/main.py
import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table
from src.core.processor import ImageProcessor
from src.core.schemas import SupportedFormat  # Importação vital para o Mypy

app = typer.Typer(help="CLI Profissional para Otimização de Assets")
console = Console()

@app.command()
def optimize(
    input_dir: Path = typer.Option(..., "--input", "-i", help="Diretório de origem"),
    output_dir: Path = typer.Option(..., "--output", "-o", help="Diretório de destino"),
    # Alteramos de 'str' para 'SupportedFormat' para satisfazer o Mypy e o Typer
    format: SupportedFormat = typer.Option("WEBP", "--format", "-f", help="Formato de saída")
) -> None:
    """
    Escaneia o diretório e otimiza assets em paralelo usando múltiplos cores.
    """
    if not input_dir.exists():
        console.print(f"[bold red]Erro:[/] Diretório '{input_dir}' não encontrado.")
        raise typer.Exit(code=1)

    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    valid_extensions: list[str] = [".jpg", ".jpeg", ".png"]
    files_to_process = [
        f for f in input_dir.iterdir()
        if f.suffix.lower() in valid_extensions
    ]

    if not files_to_process:
        console.print("[yellow]Nenhum asset compatível encontrado.[/]")
        return

    table = Table(title="Relatório de Otimização", border_style="bright_blue")
    table.add_column("Arquivo", style="cyan")
    table.add_column("Original", style="magenta")
    table.add_column("Otimizado", style="green")
    table.add_column("Economia", style="bold green")

    with console.status(f"[bold green]Processando {len(files_to_process)} imagens...") as status:
        # Agora o Mypy aceita pois 'format' é do tipo SupportedFormat (Literal)
        results = ImageProcessor.process_all(files_to_process, output_dir, target_format=format)

        for res in results:
            table.add_row(
                res["filename"],
                f"{res['original_size'] / 1024:.1f} KB",
                f"{res['optimized_size'] / 1024:.1f} KB",
                f"{res['ratio']:.2f}%"
            )

    console.print(table)
    console.print(f"\n[bold green]✔[/] Sucesso! Processo finalizado.")

if __name__ == "__main__":
    app()