@echo off
xcopy /Y Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILENAME%.icm C:\Windows\System32\spool\drivers\color\

echo Congrats, All Profiling Steps Are Finished!
echo To start from scratch run step 1 (1_setup_vars)