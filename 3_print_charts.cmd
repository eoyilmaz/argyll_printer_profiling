@echo off

set DryCreekPhotoProfilePrinter="C:\Program Files (x86)\Dry Creek Photo\Profile Target Printer\DCP Profile Target Printer.exe"
set AdobeColorPrinterUtility="%cd%\ACPU\Adobe Color Printer Utility.exe"



echo Please print the TIFF files:
dir /B /S %cd%\Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%\%ProfileName%*.tif

echo ....

rem Check if Dry Creek Photo Profile Target Printer is installed
if exist %DryCreekPhotoProfilePrinter% (
    for /f "tokens=*" %%G in ('dir /B /S %cd%\Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%\%ProfileName%*.tif') do (
        echo %%G | clip
        echo [101;93m Copied TIF file path to your clipboard[0m
        echo [101;93m CTRL + V for TIF file path [0m
        echo calling Dry Creek Photo Profile Printer
        %DryCreekPhotoProfilePrinter%
    )
) else (
    for /f "tokens=*" %%G in ('dir /B /S %cd%\Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%\%ProfileName%*.tif') do (
        echo %%G | clip
        echo [101;93m Copied TIF file path to your clipboard[0m
        echo [101;93m CTRL + V for TIF file path [0m
        echo calling ACPU
        %AdobeColorPrinterUtility%
    )
)


echo Step 3 Finished!
echo Done printing profiles
echo Run Next Step (4_read_charts)
