@echo off
rem targen -v -d2 -c <preconditioning.icc> -G -g32 -f840 <name>

IF "%PAPERSIZE%"=="A4" set PATCHCOUNT=420
IF "%PAPERSIZE%"=="A3" set PATCHCOUNT=460

mkdir Outputs\%PRINTERBRAND%_%PRINTERMODEL%

IF "%PRECONDITION_PROFILE_PATH%" == "" (
    targen -v -d2 -G -g16 -f%PATCHCOUNT% Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILENAME%
) ELSE (
    targen -v -d2 -G -g16 -f%PATCHCOUNT% -c %PRECONDITION_PROFILE_PATH% Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILENAME%
)

printtarg -v -iCM -h -R1 -T300 -M6 -L -P -p %PAPERSIZE% Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILENAME%

echo Step 2 Finished!
echo Run Next Step (3_print_charts)