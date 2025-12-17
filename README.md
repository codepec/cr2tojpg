
# CR2 to JPG Batch Converter

A Python script for recursively converting Canon CR2 RAW files to JPG while preserving the existing folder structure.

## Features

- Recursive folder processing
- Camera white balance (rawpy)
- sRGB color space
- High-quality JPG output (95%, no subsampling)
- Detailed debug output
- File-level error handling

## Technical Details

- Demosaicing: AHD
- Color space: sRGB
- Bit depth: 8-bit
- Gamma: 2.4 / 12.92
- Auto-brightness: disabled
- White balance: camera

## Requirements

- Python 3.8 – 3.11
- rawpy (MIT License)
- Pillow (HPND License)

## Installation

```bash
pip install rawpy pillow
```

## Usage

```bash
python convert.py
```

All .cr2 files in the current folder and its subfolders will be automatically converted to JPG.

## Output

- JPG files are saved in the same folder as the CR2 files
- Filenames are preserved: `photo.cr2` → `photo.jpg`

## License

MIT License  
Copyright (c) 2025 codepec
