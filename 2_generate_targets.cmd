@echo off
mkdir Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%

set /a GrayPatchCount=%NumberOfPages% * 16


if "%PreconditionProfilePath%" == "" (
    targen -v -d2 -G -g%GrayPatchCount% -f%PatchCount% Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%\%ProfileName%
) else (
    targen -v -d2 -G -g%GrayPatchCount% -f%PatchCount% -c %PreconditionProfilePath% Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%\%ProfileName%
)

if "%UseHighDensityMode%"=="True" (
    rem use i1 pro as the device to print but later use ColorMunki Photo to read
    printtarg -v -ii1 -h -R1 -T300 -M2 -L -P -p %PaperSize% Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%\%ProfileName%
) else (
    rem use ColorMunki Photo as the device
    printtarg -v -iCM -h -R1 -T300 -M2 -L -P -p %PaperSize% Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%\%ProfileName%
)

echo Step 2 Finished!
echo Run Next Step (3_print_charts)