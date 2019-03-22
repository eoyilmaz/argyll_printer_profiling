@echo off
mkdir Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%

if "%PRECONDITION_PROFILE_PATH%" == "" (
    targen -v -d2 -G -g16 -f%PATCH_COUNT% Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%
) else (
    targen -v -d2 -G -g16 -f%PATCH_COUNT% -c %PRECONDITION_PROFILE_PATH% Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%
)

if "%USE_HIGH_DENSITY_MODE%"=="True" (
    rem use i1 pro as the device to print but later use ColorMunki Photo to read
    printtarg -v -ii1 -h -R1 -T300 -M2 -L -P -p %PAPERSIZE% Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%
) else (
    rem use ColorMunki Photo as the device
    printtarg -v -iCM -h -R1 -T300 -M2 -L -P -p %PAPERSIZE% Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%
)

echo Step 2 Finished!
echo Run Next Step (3_print_charts)