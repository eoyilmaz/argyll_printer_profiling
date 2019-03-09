@echo off
colprof -v -qh -r1.0 -S AdobeRGB.icc -cmt -dpp -D"%PROFILENAME%" Outputs\%PRINTERBRAND%_%PRINTERMODEL%\%PROFILENAME%

echo Step 5 Finished!
echo Run Next Step (6_profile_check)