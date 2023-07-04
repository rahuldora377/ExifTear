import sys
import argparse
import pyexiv2


banner = """
    _______  __ __________   _______________    ____ 
   / ____/ |/ //  _/ ____/  /_  __/ ____/   |  / __ \\
  / __/  |   / / // /_       / / / __/ / /| | / /_/ /
 / /___ /   |_/ // __/      / / / /___/ ___ |/ _, _/ 
/_____//_/|_/___/_/        /_/ /_____/_/  |_/_/ |_|  
                                                    """



# ANSI escape sequence codes for different colors
COLORS = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'reset': '\033[0m'
}


# Function to colorize text
def colorize(text, color):
    color_code = COLORS.get(color.lower())
    if color_code:
        return f"{color_code}{text}{COLORS['reset']}"
    else:
        return text





parser = argparse.ArgumentParser(description="Show/Remove EXIF Data")
parser.add_argument("-p", dest="Source",help="Input File Path")
parser.add_argument("-s", dest="Show", action="store_true", help="Show EXIF Data")
parser.add_argument("-r", dest="Remove", action="store_true", help="Remove EXIF Data")
parser.add_argument("-b", dest="Banner", action="store_true", help="Show Banner")
args = parser.parse_args()


# Store Passed FilePath
filePath = args.Source


def showMetaData():
    metaData = pyexiv2.Image(filePath)
    # Read MetaData
    if len(metaData.read_exif().items()) == 0:
        print("No EXIF Data Found")
    for key, value in metaData.read_exif().items():
        f'{print(colorize(key,"cyan"),end=" : ")} {print(colorize(value,"green"))}'


def removeMetaData():
    metaData = pyexiv2.Image(filePath)
    # Remove MetaData
    metaData.clear_exif()

    # Save the modifiedImage
    metaData.close()

    colorize("EXIF Data Removed", "red")


if args.Show:
    showMetaData()

if args.Remove:
    removeMetaData()
if args.Banner:
    print(colorize(banner,'red'))