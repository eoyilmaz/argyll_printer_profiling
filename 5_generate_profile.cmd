@echo off
colprof -v -qh -r0.5 -S AdobeRGB.icc -cmt -dpp -D"%ProfileName%" -Zr -C"%Copyright%" Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%\%ProfileName%

echo Step 5 Finished!
echo Run Next Step (6_check_profile)
