import os
import subprocess
import sys

def upscale_image(input_file, output_file, scale_factor):
    # Set the path to the Topaz Gigapixel AI CLI executable
    gigapixel_cli_path = "C:/Program Files/Topaz Labs LLC/Topaz Gigapixel AI/gigapixel-cli.exe"  # Windows
    # gigapixel_cli_path = "/path/to/gigapixel-cli"  # macOS or Linux

    if not os.path.exists(gigapixel_cli_path):
        print("Gigapixel CLI not found. Check the path.")
        sys.exit(1)

    command = [
        gigapixel_cli_path,
        "-i", input_file,
        "-o", output_file,
        "-s", str(scale_factor)
    ]

    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode("utf-8"))
    except subprocess.CalledProcessError as error:
        print(f"Upscaling failed with error: {error}")
        print(error.stderr.decode("utf-8"))

if __name__ == "__main__":
    input_image = "path/to/your/input/image.jpg"
    output_image = "path/to/your/output/image.jpg"
    scale = 2  # Set the desired upscale factor (e.g., 2 for 2x upscale)

    upscale_image(input_image, output_image, scale)




Windows

Open command prompt or terminal
Type in: cd “C:\Program Files\Topaz Labs LLC\Topaz Photo AI”
Type in: tpai.exe --help
Hit enter to see options