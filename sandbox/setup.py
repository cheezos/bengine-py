import sys, os
from cx_Freeze import setup, Executable

build_exe_options = {
    "build_exe": f"{os.path.dirname(os.path.abspath(__file__))}/build",
    "optimize": 1,
    "include_files": [f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/bengine/bengine/resources/"],
    "includes" : ["pyrr", "numpy", "OpenGL.platform.win32"],
    "packages": ["os", "numpy", "pyrr", "OpenGL", "glfw", "bengine"],
    "excludes": ["tkinter"]
   }

base = None

# Uncomment below to disable the console

# if sys.platform == "win32":
#     base = "Win32GUI"

setup(
    name = "Sandbox",
    version = "0.1",
    description = "Sandbox in Bengine",
    options = {"build_exe": build_exe_options},
    executables = [Executable(f"{os.path.dirname(os.path.abspath(__file__))}/src/sandbox.py", base=base)]
)