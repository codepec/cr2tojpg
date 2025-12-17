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

- Python 3.8 – 3.12 (tested with Python 3.12)
- rawpy (MIT License)
- Pillow (HPND License)

⚠️ Note for Windows users:
  Installing rawpy via the standard CMD may not work if multiple
  Python environments exist. It is recommended to use VS Code
  or another IDE with the correct Python environment selected.

## Installation

```bash
pip install rawpy pillow
```

## Usage

```bash
python convert.py
```

The script will automatically traverse all subfolders, converting
each .cr2 file to a .jpg while preserving the original folder structure.

## OUTPUT

- Converted JPG files are saved in the **same folder** as the source CR2 files
- Original filenames are preserved:
  photo.cr2 -> photo.jpg
- Subfolder hierarchy is maintained exactly as in the input directory

## EXAMPLE FOLDER TREE

Input directory before conversion:

project/
├── event1/
│   ├── img001.cr2
│   └── img002.cr2
├── event2/
│   ├── subeventA/
│   │   └── photoA.cr2
│   └── subeventB/
│       └── photoB.cr2
└── misc/
    └── test.cr2

Output after conversion:

project/
├── event1/
│   ├── img001.cr2
│   └── img001.jpg
│   ├── img002.cr2
│   └── img002.jpg
├── event2/
│   ├── subeventA/
│   │   ├── photoA.cr2
│   │   └── photoA.jpg
│   └── subeventB/
│       ├── photoB.cr2
│       └── photoB.jpg
└── misc/
    ├── test.cr2
    └── test.jpg

## LICENSE

MIT License
Copyright (c) 2025 codepec

