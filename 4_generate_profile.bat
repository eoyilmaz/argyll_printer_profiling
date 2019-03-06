@echo off
colprof -v -qh -r1.0 -S AdobeRGB.icc -cmt -dpp -D"%PROFILENAME%" Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILENAME%

echo Step 4 Finished!
echo Run Next Step (5_profile_check)