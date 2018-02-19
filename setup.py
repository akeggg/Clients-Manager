from cx_Freeze import setup, Executable
import os
import sys
import sqlite3 as lite

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python35\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python35\tcl\tk8.6'


build_exe_options = {"packages": [
  'os','sys','sqlite3'], 'include_files': [os.path.join(sys.base_prefix, 'Lib\site-packages\PyQt5\plugins\sqldrivers', 'qsqlite.dll'), 'main.py','util.py','data.db']}

setup(
    name = "Eclients",
    version = "0.1",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py")]
)
