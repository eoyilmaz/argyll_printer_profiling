@echo off
profcheck -k -v2 Outputs/%PRINTERBRAND%_%PRINTERMODEL%/%PROFILEDATE%/%PROFILENAME%.ti3 Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%.icm

echo Step 6 Finished!
echo Run Next Step (7_install_profile)