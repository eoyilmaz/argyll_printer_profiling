@echo off
set READ_MODE_DEFAULT_VALUE=1
set READ_MODE=
set CONTINUE_READING_DEFAULT_VALUE=Y
set CONTINUE_READING=

set /p READ_MODE=Read Mode? Strip (1) or Patch by Patch (2)? (Default: 1-Strip)
if "%READ_MODE%"=="" set READ_MODE=%READ_MODE_DEFAULT_VALUE%

if exist Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%.ti3 (
    set /p CONTINUE_READING=Previous Chart exists! Continue Reading? (%CONTINUE_READING_DEFAULT_VALUE%)
) else (
    set CONTINUE_READING=N
)


if "%READ_MODE%"=="1" (
    if "%CONTINUE_READING%"=="Y" (
        chartread -v -H -T0.4 -r Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%
    ) else (
        chartread -v -H -T0.4 Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%
    )
) else (
    if "%CONTINUE_READING%"=="Y" (
        chartread -v -H -T0.4 -p -P -r Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%
    ) else (
        chartread -v -H -T0.4 -p -P Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%
    )
)

echo Step 4 Finished!
echo Run Next Step (5_generate_profile)