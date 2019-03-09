@echo off
echo Please print %ch%\Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILENAME%*.tif

echo [101;93m Copied TIF file path to your clipboard[0m
echo [101;93m CTRL + V for TIF file path [0m

echo %cd%\Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILENAME%_01.tif | clip
"ACPU\Adobe Color Printer Utility.exe"

IF "%PAPERSIZE%" == "A4" (
echo %cd%\Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILENAME%_02.tif | clip
"ACPU\Adobe Color Printer Utility.exe"
)


echo Step 3 Finished!
echo Done printing profiles
echo Run Next Step (4_chartread)