import sys

rootDir= "D:\\myScript\\maya"


if rootDir not in sys.path:
    sys.path.append(rootDir)


if 'tempPivot.tempPivot_main' in sys.modules:
    print("deldeted Modules")
    del sys.modules['tempPivot.tempPivot_main']
    
import tempPivot.tempPivot_main as tempPivot_main

tempPivot_main.run()
