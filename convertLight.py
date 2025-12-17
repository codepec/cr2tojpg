"""
CR2 to JPG Converter (Batch)

Copyright (c) 2025 codepec

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.
Uses:
- rawpy (MIT License)
- Pillow (HPND License)
"""

import os
import rawpy
from PIL import Image
import traceback

print("Python OK")
print("rawpy version:", rawpy.__version__)

input_root = "."

for root, dirs, files in os.walk(input_root):
    print(f"📂 Folder: {root}")

    for file in files:
        if file.lower().endswith(".cr2"):
            input_path = os.path.join(root, file)
            print(f"➡️ Opening: {input_path}")

            try:
                with rawpy.imread(input_path) as raw:
                    print("   ✔ CR2 loaded")
                    rgb = raw.postprocess(
                        use_camera_wb=True,
                        use_auto_wb=False,
                        no_auto_bright=True,
                        output_color=rawpy.ColorSpace.sRGB,
                        output_bps=8,
                        bright=1.5,
                        gamma=(2.4, 12.92),
                        demosaic_algorithm=rawpy.DemosaicAlgorithm.AHD
                    )
                    print("   ✔ Postprocess OK")

                output_path = os.path.splitext(input_path)[0] + ".jpg"
                Image.fromarray(rgb).save(
                    output_path,
                    "JPEG",
                    quality=95,
                    subsampling=0
                )
                print(f"   ✔ Saved: {output_path}")

            except Exception:
                print("❌ ERROR:")
                traceback.print_exc()
