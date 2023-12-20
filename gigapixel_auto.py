from gigapixel import Gigapixel, Scale, Mode, OutputFormat
from pathlib import Path
from gigapixel import Scale, Mode, OutputFormat
import time


# Path to Gigapixel executable file.
exe_path = Path('C:\Program Files\Topaz Labs LLC\Topaz Gigapixel AI\Topaz Gigapixel AI.exe')


# Output file suffix. (e.g. pic.jpg -> pic-gigapixel.jpg)
# You should set same value inside Gigapixel (File -> Preferences -> Default filename suffix).
output_suffix = '-gigapixel'

# Create Gigapixel instance.
app = Gigapixel(exe_path, output_suffix)

time.sleep(10)
# Process image.
image = Path('image.png')
output_path = app.process(image, scale=Scale.X4, mode=Mode.ART_AND_CG, delete_from_history=True)

# Print output path.
print(output_path)
