import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {
    "build_exe": "C:/Users/colto/Documents/Github/bepto-engine/sandbox/build",
    "optimize": 2,
    "includes" : ["OpenGL.platform.win32"],
    "packages": ["bengine"],
    "excludes": ["tkinter"]
   }

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Sandbox",
    version = "0.1",
    description = "Sandbox in Bengine",
    options = {"build_exe": build_exe_options},
    executables = [Executable("C:/Users/colto/Documents/Github/bepto-engine/sandbox/src/main.py", base=base)]
)