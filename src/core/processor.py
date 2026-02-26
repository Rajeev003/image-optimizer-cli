# src/core/processor.py
import os
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from typing import List
from PIL import Image
from src.core.schemas import SupportedFormat, OptimizationResult, DEFAULT_CONFIG

class ImageProcessor:
    @staticmethod
    def process_single_image(
        input_path: Path,
        output_dir: Path,
        target_format: SupportedFormat = "WEBP"
    ) -> OptimizationResult:
        """
        Lógica de processamento isolada para execução em paralelo.
        """
        original_size: int = input_path.stat().st_size
        output_path: Path = output_dir / f"{input_path.stem}.{target_format.lower()}"

        with Image.open(input_path) as img:
            # Garante compatibilidade de cores (RGB) para formatos que não suportam transparência
            if img.mode in ("RGBA", "P") and target_format not in ["WEBP", "PNG"]:
                img = img.convert("RGB")

            img.save(
                output_path,
                format=target_format,
                **DEFAULT_CONFIG
            )

        optimized_size: int = output_path.stat().st_size
        saved: int = original_size - optimized_size

        return {
            "filename": input_path.name,
            "original_size": original_size,
            "optimized_size": optimized_size,
            "saved_bytes": saved,
            "ratio": (saved / original_size) * 100 if original_size > 0 else 0
        }

    @classmethod
    def process_all(
        cls,
        files: List[Path],
        output_dir: Path,
        target_format: SupportedFormat = "WEBP"
    ) -> List[OptimizationResult]:
        """
        Gerencia o pool de processos para alta performance aproveitando múltiplos cores.
        """
        with ProcessPoolExecutor() as executor:
            futures = [
                executor.submit(cls.process_single_image, f, output_dir, target_format)
                for f in files
            ]
            return [future.result() for future in futures]