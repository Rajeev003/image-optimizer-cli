# src/core/types.py
from typing import TypedDict, Literal, Final

# Formatos de saída suportados para garantir profissionalismo exato
SupportedFormat = Literal["WEBP", "AVIF", "PNG", "JPEG"]

class OptimizationResult(TypedDict):
    filename: str
    original_size: int
    optimized_size: int
    saved_bytes: int
    ratio: float

# Configurações padrão de compressão (Pillow)
class CompressionConfig(TypedDict):
    quality: int
    optimize: bool
    lossless: bool

DEFAULT_CONFIG: Final[CompressionConfig] = {
    "quality": 80,
    "optimize": True,
    "lossless": False
}