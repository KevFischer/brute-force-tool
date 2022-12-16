# Brute-Force-Tool
This project will be a python based bruteforce-tool to test security systems.

Read more in the [Wiki Section](https://github.com/KevFischer/brute-force-tool/wiki).

## How to run

## Prerequisites

### Python

First of all you need to make sure that Python is installed.

Check if python is installed by typing the following line in shell / command-prompt:

    python -V
    
or eventually:

    python3 -V
    
You should get a similar output like this:

    Python 3.10.6
    
If you don't get an output like this or an error message, you should install Python first.

You can get it [here](https://www.python.org/downloads/).

Or if you using Linux, you can simply paste following commands in your shell:

    $ sudo apt-get update
    $ sudo apt-get install python3.10

In development i'm using the following version:

    Python 3.10.6
  
To make sure everything is working fine, you should have at least the version mentioned above.

### PIP

To install python packages I'm using pip with the following version:

    pip 22.2.1 from C:\Python310\lib\site-packages\pip (python 3.10)
    
To make sure everything is working fine, you should have at least the version mentioned above.

Note: PIP can be automatically installed with python together.

### Virtual environment

I am using a [virtual environment](https://pypi.org/project/virtualenv/) (short venv) to prevent e.g. class name duplications.

To set up a venv, you need to have virtualenv installed.

You can install it by typing the following line in your prompt:

    pip install virtualenv
    
I am using the following version of virtualenv:

    virtualenv==20.16.4
    
You can check your version of virtualenv by using following command:

    pip show virtualenv

The output should look like this:

    Name: virtualenv
    Version: 20.16.4
    Summary: Virtual Python Environment builder
    Home-page: https://virtualenv.pypa.io/
    Author: Bernat Gabor
    Author-email: gaborjbernat@gmail.com
    License: MIT
    Location: c:\users\wm01114\appdata\local\programs\python\python310\lib\site-packages
    Requires: distlib, filelock, platformdirs
    Required-by:

Now, in your project directory you can create a virtual environment by typing the following line:

    python -m venv [NAME OF VENV]
    
Note: Replace [NAME OF VENV] with a name you like. I'm usually using "venv" as the name of the virtual environment for simplicity.

You can activate the virtual environment as following:

On windows:

    .\venv\Scripts\activate

Note: If your PowerShell execution policy rejects you from executing the activate.ps1, you can try the activate.bat in a Command Prompt, rather than in a PowerShell Environment.
    
On Linux:

    source \venv\bin\activate.sh
    
Now you're ready to install required packages in the environment by hitting the following line:

    pip install -r requirements.txt
    
Note: You need to be in the same directory where requirements.txt is located.

## Run the program

### Using the source code

If you match all prerequisites from above, you should be able to run the program with the following command:

In project directory:

    python main.py

There are multiple option, some of them are required. Please take in mind that required options have to be given.

|Short Option|Long Option|Parameters|Description|Required|
|---|---|---|---|---|
|-h|--help|None|List all options with it's description|No|
|-t|--target|String|Hostname or IP-address of target devicce|Yes|
|-r|--runs|Integer|Number of runs till program ends|Yes|
|-s|--system|String|Describing name of system to try the bruteforce attack. E.g. RDP|Yes|
|-o|-outfile|String|File where results should be safed in|No|
|-timeout|None|Integer|Number in seconds the program is allowed to run|No|
|-d|--delay|Float|Number of seconds the program is waiting between each attempt|No|

Taking this in mind an example execution command could look like this:

    python main.py -t TestServer -s RDP -r 100 -o Test.txt -d 0.5 -timeout 1800

### Using the released executable

Executing the program with the executable is working exactly the same as executing the source code thanks to [PyInstaller](https://pyinstaller.org/en/stable/usage.html).

You can simply run the following line:

    bruteforce.exe -t TestServer -s RDP -r 100 -o Test.txt -d 0.5 -timeout 1800
    
## Troubleshooting

Feel free to create [issues](https://github.com/KevFischer/brute-force-tool/issues) if you have troubles starting the app or setting up one of the prerequisites.

I'm looking forward to help with every issue.

## Roadmap

You can have an indepth view of planned Features, Bugfixes and more in the [issues section](https://github.com/KevFischer/brute-force-tool/issues).