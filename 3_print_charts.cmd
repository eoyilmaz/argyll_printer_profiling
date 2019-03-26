@echo off

set DRY_CREEK_PHOTO_PROFILE_PRINTER="C:\Program Files (x86)\Dry Creek Photo\Profile Target Printer\DCP Profile Target Printer.exe"
set ADOBE_COLOR_PRINTER_UTILITY="%cd%\ACPU\Adobe Color Printer Utility.exe"



echo Please print the TIFF files:
dir /B /S %cd%\Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%*.tif

echo ....

rem Check if Dry Creek Photo Profile Target Printer is installed
if exist %DRY_CREEK_PHOTO_PROFILE_PRINTER% (
    for /f "tokens=*" %%G in ('dir /B /S %cd%\Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%*.tif') do (
        echo %%G | clip
        echo [101;93m Copied TIF file path to your clipboard[0m
        echo [101;93m CTRL + V for TIF file path [0m
        echo calling Dry Creek Photo Profile Printer
        %DRY_CREEK_PHOTO_PROFILE_PRINTER%
    )
) else (
    for /f "tokens=*" %%G in ('dir /B /S %cd%\Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%*.tif') do (
        echo %%G | clip
        echo [101;93m Copied TIF file path to your clipboard[0m
        echo [101;93m CTRL + V for TIF file path [0m
        echo calling ACPU
        %ADOBE_COLOR_PRINTER_UTILITY%
    )
)


echo Step 3 Finished!
echo Done printing profiles
echo Run Next Step (4_read_charts)
