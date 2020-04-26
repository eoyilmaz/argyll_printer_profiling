@echo off
profcheck -k -v2 Outputs/%PrinterBrand%_%PrinterModel%/%ProfileDate%/%ProfileName%.ti3 Outputs\%PrinterBrand%_%PrinterModel%\%ProfileDate%\%ProfileName%.icm

echo Step 6 Finished!
echo Run Next Step (7_install_profile)