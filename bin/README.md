# aocsetup

**A**dvent **o**f **C**ode setup is a command line utility tool which can download the problem input and generate src and test files from a template.

The default behavior is to download the problem input of current year/day according to your system time. If you want the script to wait for the next problem release use ```-w```.

## Usage

```
usage: aocsetup.py [-h] [-s SESSION_COOKIE] [-y YEAR] [-d DAY]
                   [-st SRC_TEMPLATE] [-so SRC_OUTPUT] [-tt TEST_TEMPLATE]
                   [-to TEST_OUTPUT] [-io INPUT_OUTPUT] [-w] [-l] [-f]
                   [-cf CONFIG_FILE] [-ic] [-sc] [-sco SAVE_CONFIG_OUTPUT]

Advent of Code (AOC) utility to download problem input and setup python files
for a given day.

optional arguments:
  -h, --help            show this help message and exit
  -s SESSION_COOKIE, --session-cookie SESSION_COOKIE
                        Session cookie which is used to download problem input
  -y YEAR, --year YEAR  Download the aoc input for a given year
  -d DAY, --day DAY     Download the aoc input for a given day
  -st SRC_TEMPLATE, --src-template SRC_TEMPLATE
                        Source template file
  -so SRC_OUTPUT, --src-output SRC_OUTPUT
                        Source output file
  -tt TEST_TEMPLATE, --test-template TEST_TEMPLATE
                        Test template file
  -to TEST_OUTPUT, --test-output TEST_OUTPUT
                        Test output file
  -io INPUT_OUTPUT, --input-output INPUT_OUTPUT
                        Input output file
  -w, --wait            Wait for the next problem release
  -l, --log             Enable logging
  -f, --force           Overwrite existing files
  -cf CONFIG_FILE, --config-file CONFIG_FILE
                        Config file
  -ic, --ignore-config  Ignores any existing config files
  -sc, --save-config    Generates (default: aocsetup.conf) config file from
                        current arguments
  -sco SAVE_CONFIG_OUTPUT, --save-config-output SAVE_CONFIG_OUTPUT
                        Generated config file output
```

## Template Files

Template files you provide will be copied to the path specified with ```-so``` or ```-to``` for a src and test file respectively. Substrings ```{{day}}``` and ```{{year}}``` will be replaced with the year and day specified. 

## Config File

All arguments can also be specified in a config file. ```aocsetup.conf``` is the default config file name the script is looking for if no specific config file name was passed via ```-cf```. You can generate a config file of your current arguments with ```-sc```. 

Example:

```
{
    "session-cookie": "SESSION ID",
    "src-template": "bin/src-template.py",
    "src-output": "src/day{{day}}.py",
    "test-template": "bin/test-template.py",
    "test-output": "tests/test_day{{day}}.py",
    "input-output": "inputs/input_day{{day}}.txt"
}
```
