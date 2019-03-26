@echo off
colprof -v -qh -r0.5 -S AdobeRGB.icc -cmt -dpp -D"%PROFILENAME%" -Zr Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILEDATE%\%PROFILENAME%

echo Step 5 Finished!
echo Run Next Step (6_check_profile)
