@echo off

rem Set default values
set PRINTERBRAND_DEFAULT_VALUE=Canon
set PRINTERMODEL_DEFAULT_VALUE=iX6800_Series
set PAPERBRAND_DEFAULT_VALUE=Kodak
set PAPERMODEL_DEFAULT_VALUE=UPPP
set PAPERFINISH_DEFAULT_VALUE=Glossy
set PAPERSIZE_DEFAULT_VALUE=A4
set INK_BRAND_DEFAULT_VALUE=Canon
set USE_HIGH_DENSITY_MODE_DEFAULT_VALUE=True
set NUMBER_OF_PAGES_DEFAULT_VALUE=1
set PER_PAGE_PATCH_COUNT_DEFAULT_VALUE=

rem =================================================
rem If the USE_HIGH_DENSITY_MODE_DEFAULT_VALUE is set
rem to True the system uses the i1pro patch pattern
rem which is much denser than the Color munki one.
rem
rem If USE_HIGH_DENSITY_MODE_DEFAULT_VALUE is set
rem anything other than True, then the system will use
rem two A4 pages or one A3 page and will set the:
rem
rem PATCH_COUNT_A4_DEFAULT_VALUE=420
rem PATCH_COUNT_A3_DEFAULT_VALUE=460
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
set PRINTERBRAND=
set PRINTERMODEL=
set PAPERBRAND=
set PAPERMODEL=
set PAPERFINISH=
set PAPERSIZE=
set INK_BRAND=
set PRECONDITION_PROFILE_PATH=
set PATCH_COUNT=
set USE_HIGH_DENSITY_MODE=
set COPYRIGHT=

rem Request user values
set /p PRINTERBRAND=Printer Brand? (%PRINTERBRAND_DEFAULT_VALUE%)
if "%PINTERBRAND%"=="" set PRINTERBRAND=%PRINTERBRAND_DEFAULT_VALUE%

set /p PRINTERMODEL=Printer Model? (%PRINTERMODEL_DEFAULT_VALUE%)
if "%PRINTERMODEL%"=="" set PRINTERMODEL=%PRINTERMODEL_DEFAULT_VALUE%

set /p PAPERBRAND=Paper Brand? (%PAPERBRAND_DEFAULT_VALUE%)
if "%PAPERBRAND%"=="" set PAPERBRAND=%PAPERBRAND_DEFAULT_VALUE%

set /p PAPERMODEL=Paper Model? (%PAPERMODEL_DEFAULT_VALUE%)
if "%PAPERMODEL%"=="" set PAPERMODEL=%PAPERMODEL_DEFAULT_VALUE%

set /p PAPERFINISH=Paper Finish? (%PAPERFINISH_DEFAULT_VALUE%)
if "%PAPERFINISH%"=="" set PAPERFINISH=%PAPERFINISH_DEFAULT_VALUE%

set /p PAPERSIZE=Paper Size? (%PAPERSIZE_DEFAULT_VALUE%)
if "%PAPERSIZE%"=="" set PAPERSIZE=%PAPERSIZE_DEFAULT_VALUE%

set /p INK_BRAND=Ink Brand? (%INK_BRAND_DEFAULT_VALUE%)
if "%INK_BRAND%"=="" set INK_BRAND=%INK_BRAND_DEFAULT_VALUE%

set /p USE_HIGH_DENSITY_MODE=Use High Density Mode? (%USE_HIGH_DENSITY_MODE_DEFAULT_VALUE%)
if "%USE_HIGH_DENSITY_MODE%"=="" set USE_HIGH_DENSITY_MODE=%USE_HIGH_DENSITY_MODE_DEFAULT_VALUE%

set /p NUMBER_OF_PAGES=Number of pages to be used in profiling? (%NUMBER_OF_PAGES_DEFAULT_VALUE%)
if "%NUMBER_OF_PAGES%"=="" set NUMBER_OF_PAGES=%NUMBER_OF_PAGES_DEFAULT_VALUE%

if "%USE_HIGH_DENSITY_MODE%"=="True" (
    set PER_PAGE_PATCH_COUNT_A4_DEFAULT_VALUE=600
    set PER_PAGE_PATCH_COUNT_A3_DEFAULT_VALUE=1260
) else (
    set PER_PAGE_PATCH_COUNT_A4_DEFAULT_VALUE=210
    set PER_PAGE_PATCH_COUNT_A3_DEFAULT_VALUE=460
)

if "%PAPERSIZE%"=="A4" set PER_PAGE_PATCH_COUNT_DEFAULT_VALUE=%PER_PAGE_PATCH_COUNT_A4_DEFAULT_VALUE%
if "%PAPERSIZE%"=="A3" set PER_PAGE_PATCH_COUNT_DEFAULT_VALUE=%PER_PAGE_PATCH_COUNT_A3_DEFAULT_VALUE%
if "%PATCH_COUNT%"=="" set /a PATCH_COUNT=%NUMBER_OF_PAGES% * %PER_PAGE_PATCH_COUNT_DEFAULT_VALUE%

set /p PRECONDITION_PROFILE_PATH=Pre-conditioning Profile Path? ()

set /p COPYRIGHT=Copyright Info?


rem get date time string
for /f "tokens=1-3 delims=/. " %%a in ('date /t') do (set PROFILEDATE=%%c%%b%%a)
for /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set PROFILETIME=%%a%%b)

rem prepare profile name
set PROFILENAME=%PRINTERBRAND%_%PRINTERMODEL%_%PAPERBRAND%_%PAPERMODEL%_%PAPERFINISH%_%PAPERSIZE%_%INK_BRAND%_%PROFILEDATE%_%PROFILETIME%

rem inform user
echo Profile name is: %PROFILENAME%

echo Step 1 Finished!
echo Run Next Step (2_generate_targets)