@echo off
rem targen -v -d2 -c <preconditioning.icc> -G -g32 -f840 <name>

IF "%PAPERSIZE%"=="A4" set PATCHCOUNT=420
IF "%PAPERSIZE%"=="A3" set PATCHCOUNT=460

mkdir Outputs\%PRINTERBRAND%_%PRINTERMODEL%

targen -v -d2 -G -g32 -f%PATCHCOUNT% Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILENAME%
printtarg -v -iCM -h -R1 -T300 -p %PAPERSIZE% Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILENAME%

echo Step 2 Finished!
echo Please print %PAPERSIZE% Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILENAME%*.tif
echo Run Next Step (3_chartread)