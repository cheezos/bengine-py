import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "build_exe": "build",
    "optimize": 1,
    "include_files": ["C:/Users/colto/Documents/Github/bepto-engine/bengine/bengine/resources/"],
    "includes" : ["pyrr", "numpy", "OpenGL.platform.win32"],
    "packages": ["os", "numpy", "pyrr", "OpenGL", "glfw", "bengine"],
    "excludes": ["tkinter"]
   }

base = None

# if sys.platform == "win32":
#     base = "Win32GUI"

setup(
    name = "Sandbox",
    version = "0.1",
    description = "Sandbox in Bengine",
    options = {"build_exe": build_exe_options},
    executables = [Executable("./src/sandbox.py", base=base)]
)