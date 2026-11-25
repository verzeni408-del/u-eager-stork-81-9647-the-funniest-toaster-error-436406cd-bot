import os

# Writes one line to /output/entry.txt: the toaster's error message.
ENTRY = "ERROR 04: BREAD BURNED. I HEARD WHAT YOU CALLED ME THIS MORNING."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
