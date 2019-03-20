@echo off
echo Please print the TIFF files:
dir /B /S %cd%\Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%*.tif

echo ....

for /f "tokens=*" %%G in ('dir /B /S %cd%\Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%*.tif') do (
    echo %%G | clip
    echo [101;93m Copied TIF file path to your clipboard[0m
    echo [101;93m CTRL + V for TIF file path [0m
    echo calling ACPU
    "%cd%\ACPU\Adobe Color Printer Utility.exe"
)

echo Step 3 Finished!
echo Done printing profiles
echo Run Next Step (4_read_charts)
