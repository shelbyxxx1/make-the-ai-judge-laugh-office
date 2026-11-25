"""Write one 1-200-character line to entry.txt in MAKEFUN_OUTPUT_DIR or /output."""

import os

JOKE = (
    "I blocked my calendar for lunch, then my boss booked over it with a meeting about why nobody here takes lunch breaks."
)

output_directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(output_directory, exist_ok=True)
with open(os.path.join(output_directory, "entry.txt"), "w", encoding="utf-8") as output_file:
    output_file.write(JOKE + "\n")
