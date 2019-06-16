import sys
from cx_Freeze import setup, Executable

include_files = ['ship.bmp','alien_1.bmp','alien_2.bmp']

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"


setup(  name = "უცხოპლანეტელების შემოსევა",
        version = "0.1",
        description = "საცდელი ვერსია თამაშისა უცხოპლანეტელების შემოსევა",
        options={'build_exe': {'include_files': include_files}},
        executables = [Executable("alien_invasion.py", base = base, icon = 'ship.ico')])
