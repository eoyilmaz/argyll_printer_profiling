@echo off

rem Set default values
if "%PrinterBrand%" == "" (
    set PrinterBrandDefaultValue=Canon
) else (
    set PrinterBrandDefaultValue=%PrinterBrand%
)

if "%PrinterModel%" == "" (
    set PrinterModelDefaultValue=iX6850
) else (
    set PrinterModelDefaultValue=%PrinterModel%
)

if "%PaperBrand%" == "" (
    set PaperBrandDefaultValue=Kodak
) else (
    set PaperBrandDefaultValue=%PaperBrand%
)

if "%PaperModel%" == "" (
    set PaperModelDefaultValue=UPPP
) else (
    set PaperModelDefaultValue=%PaperModel%
)

if "%PaperFinish%" == "" (
    set PaperFinishDefaultValue=Glossy
) else (
    set PaperFinishDefaultValue=%PaperFinish%
)

if "%PaperSize%" == "" (
    set PaperSizeDefaultValue=A4
) else (
    set PaperSizeDefaultValue=%PaperSize%
)

if "%InkBrand%" == "" (
    set InkBrandDefaultValue=Canon
) else (
    set InkBrandDefaultValue=%InkBrand%
)

if "%UseHighDensityMode%" == "" (
    set UseHighDensityModeDefaultValue=True
) else (
    set UseHighDensityModeDefaultValue=%UseHighDensityMode%
)

if "%NumberOfPages%" == "" (
    set NumberOfPagesDefaultValue=1
) else (
    set NumberOfPagesDefaultValue=%NumberOfPages%
)

if "%PerPagePatchCount%" == "" (
    set PerPagePatchCountDefaultValue=
) else (
    set PerPagePatchCountDefaultValue=%PerPagePatchCount%
)

if "%Copyright%" == "" (
    set CopyrightDefaultValue=
) else (
    set CopyrightDefaultValue=%Copyright%
)


rem =================================================
rem If the UseHighDensityModeDefaultValue is set
rem to True the system uses the i1pro patch pattern
rem which is much denser than the Color munki one.
rem
rem If UseHighDensityModeDefaultValue is set
rem anything other than True, then the system will use
rem two A4 pages or one A3 page and will set the:
rem
rem PatchCountA4DefaultValue=420
rem PatchCountA3DefaultValue=460
rem
rem by setting the device to i1pro and the margins to 2 mm
rem it is possible to print
rem 600 (25x24) 8x10 mm patches for A4 and
rem 1260 (36x35) 8x10 mm patches for A3
rem on a single page
rem 
rem what I want to achive here is to use the minimum
rem amount of paper for profiling and still have an
rem excellent result
rem =================================================


rem Erase previous values
set PrinterBrand=
set PrinterModel=
set PaperBrand=
set PaperModel=
set PaperFinish=
set PaperSize=
set InkBrand=
set PreconditionProfilePath=
set NumberOfPages=
set PatchCount=
set UseHighDensityMode=
set Copyright=

rem Request user values
set /p PrinterBrand=Printer Brand? (%PrinterBrandDefaultValue%)
if "%PrinterBrand%"=="" set PrinterBrand=%PrinterBrandDefaultValue%

set /p PrinterModel=Printer Model? (%PrinterModelDefaultValue%)
if "%PrinterModel%"=="" set PrinterModel=%PrinterModelDefaultValue%

set /p PaperBrand=Paper Brand? (%PaperBrandDefaultValue%)
if "%PaperBrand%"=="" set PaperBrand=%PaperBrandDefaultValue%

set /p PaperModel=Paper Model? (%PaperModelDefaultValue%)
if "%PaperModel%"=="" set PaperModel=%PaperModelDefaultValue%

set /p PaperFinish=Paper Finish? (%PaperFinishDefaultValue%)
if "%PaperFinish%"=="" set PaperFinish=%PaperFinishDefaultValue%

set /p PaperSize=Paper Size? (%PaperSizeDefaultValue%)
if "%PaperSize%"=="" set PaperSize=%PaperSizeDefaultValue%

set /p InkBrand=Ink Brand? (%InkBrandDefaultValue%)
if "%InkBrand%"=="" set InkBrand=%InkBrandDefaultValue%

set /p UseHighDensityMode=Use High Density Mode? (%UseHighDensityModeDefaultValue%)
if "%UseHighDensityMode%"=="" set UseHighDensityMode=%UseHighDensityModeDefaultValue%

set /p NumberOfPages=Number of pages to be used in profiling? (%NumberOfPagesDefaultValue%)
if "%NumberOfPages%"=="" set NumberOfPages=%NumberOfPagesDefaultValue%

if "%UseHighDensityMode%"=="True" (
    set PerPagePatchCountA4DefaultValue=600
    set PerPagePatchCountA3DefaultValue=1260
) else (
    set PerPagePatchCountA4DefaultValue=210
    set PerPagePatchCountA3DefaultValue=460
)

if "%PaperSize%"=="A4" set PerPagePatchCountDefaultValue=%PerPagePatchCountA4DefaultValue%
if "%PaperSize%"=="A3" set PerPagePatchCountDefaultValue=%PerPagePatchCountA3DefaultValue%
if "%PatchCount%"=="" set /a PatchCount=%NumberOfPages% * %PerPagePatchCountDefaultValue%

set /p PreconditionProfilePath=Pre-conditioning Profile Path? ()

set /p Copyright=Copyright Info? (%CopyrightDefaultValue%)
if "%Copyright%"=="" set Copyright=%CopyrightDefaultValue%


rem get date time string
for /f "tokens=1-3 delims=/. " %%a in ('date /t') do (set ProfileDate=%%c%%b%%a)
for /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set ProfileTime=%%a%%b)

rem prepare profile name
set ProfileName=%PrinterBrand%_%PrinterModel%_%PaperBrand%_%PaperModel%_%PaperFinish%_%PaperSize%_%InkBrand%_%ProfileDate%_%ProfileTime%

rem inform user
echo Profile name is: %ProfileName%

echo Step 1 Finished!
echo Run Next Step (2_generate_targets)