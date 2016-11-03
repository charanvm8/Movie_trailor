# Movie Trailer

The application will display a movie list(my personal list). You can clink on the image to play the trailer of the movie.

### Getting Started:

You can download the zip file and extract it to get access to the files.

### Prerequisities:

Since it is written in python you need python to be installed on the system.

### Installation Instructions:

Windows

Python and IDLE are not installed by default.

Browse to http://www.python.org/download.
Look for the Windows downloads, choose the one appropriate for your architecture (32-bit or 64-bit). At the time of writing, the choices are:
32-bit: Python 2.7.3 Windows Installer
64-bit: Python 2.7.3 Windows X86-64 Installer
If you don't know the system architecture, try running winmsd.exe (in Windows XP) or msinfo32.exe (in Windows 7). Look at System Type and/or Processor. It will look this this for 32-bit, or this for 64.
Run the installer and click through the prompts. Default options are usually just fine. This installs IDLE, too, by default.
IDLE (Python GUI) and Python (command line) should now by in your program menu, under Python 2.7, and Python will be associated with .py files. However they're going to need to know about the files we create during the workshop. This is easiest if we start IDLE from the WORKSHOP folder itself. Let's create a Windows script, idle.bat that does that:

Browse to your WORKSHOP directory.
Right-click in the empty space, choose New -> Text Document, name it idle.bat (accept the warning about file extensions).
Edit the file by right-clicking and choosing Edit.
Enter the single line:
C:\Python27\Lib\idlelib\idle.bat
Close the file.
You should now be able to double-click idle.bat to open IDLE.

Mac

Python is installed by default, but IDLE is not (and Python is likely a little old). Follow these instructions for a Mac binary install, or install from source, using the instructions further down the page.

Browse to http://www.python.org/download.
Look for the Mac download, choose the one appropriate for your architecture (32-bit or 64-bit) and OS X version. If you don't know the system architecture, try running arch or uname -m in Terminal.app. At the time of writing, the choices are:
32-bit for Mac OS X 10.3 through 10.6: Python 2.7.3 Mac OS X 32-bit i386/PPC Installer
32-bit or 64-bit OS X 10.6           : Python 2.7.3 Mac OS X 64-bit/32-bit x86-64/i386 Installer
Run the installer and click through the prompts. Default options are usually just fine. This installs IDLE, too, by default.
We're going to want to launch IDLE from within the WORKSHOP directory. This should work by default. Open up Terminal.app from the Applications menu, and type:

cd WORKSHOP
Where WORKSHOP is replaced by the directory you chose to use for the workshop. Now type:

idle &
and hit ENTER to launch IDLE.

Linux

Python is installed by default, but sometimes IDLE is not. Either install IDLE using your distro's package manager, e.g. apt-get install idle (Ubuntu/Debian/etc.), yum install python26-tools (RHEL/CentOS/etc.), USE=tk emerge -avn python (Gentoo), etc., or install new version of Python from source (which will include IDLE).

Launching IDLE from the WORKSHOP directory will be the same as for the Mac case above (just use your favorite terminal instead of Terminal.app).


Running the Application:

Run the movie_list.py file in the idle for the application to get lauched at localserver. You can see a html page showing the context.

### Built With:

HTML,CSS,JQuery,Python,JavaScript

### Developed by:
Charan Vardhan M
