@echo off
set ReadModeDefaultValue=1
set ReadMode=
set ContinueReadingDefaultValue=Y
set ContinueReading=

set /p ReadMode=Read Mode? Strip (1) or Patch by Patch (2)? (Default: 1-Strip)
if "%ReadMode%"=="" set ReadMode=%ReadModeDefaultValue%

if exist Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%\%ProfileName%.ti3 (
    set /p ContinueReading=Previous Chart exists! Continue Reading? (%ContinueReadingDefaultValue%^)
) else (
    set ContinueReading=N
)
if "%ContinueReading%"=="" set ContinueReading=%ContinueReadingDefaultValue%

if "%ReadMode%"=="1" (
    if "%ContinueReading%"=="Y" (
        chartread -v -H -T0.4 -r Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%\%ProfileName%
    ) else (
        chartread -v -H -T0.4 Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%\%ProfileName%
    )
) else (
    if "%ContinueReading%"=="Y" (
        chartread -v -H -T0.4 -p -P -r Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%\%ProfileName%
    ) else (
        chartread -v -H -T0.4 -p -P Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%\%ProfileName%
    )
)

echo Step 4 Finished!
echo Run Next Step (5_generate_profile)