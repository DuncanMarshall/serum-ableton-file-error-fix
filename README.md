# Serum Ableton File Error Fix
Workaround for the issue with not being able to drag files in to Serum if they are open in the Ableton playlist/browser

## Why?

A common workflow for Serum is to resample and drag files on to the oscilator as wavetables.  When using Ableton on Windows, Ableton often keeps files open, and Serum cannot access them causing a File Error.

## Install

1.  Download, and unzip to a folder.

2.  Download and unzip Microsoft's Handle utility in the same folder: https://download.sysinternals.com/files/Handle.zip

3.  Run handle.exe once and agree to the licence.

4.  Install python, clicking "Add Python to path" in the installer: https://www.python.org/downloads/windows/ 

5.  (optional) Run the "Run as Admin.reg" file, giving a "Open command window here as Administrator" right click context option to Explorer.

## Warning

This a kludge, and could very well make your system unstable, make you lose progress, or any other number of terrible things.  I've personally never had a problem, but use at your own risk.  I would save and backup frequently.

## Usage

1.  Do some work in Ableton, causing you to have a file in your browser or playlist which you want to import in to Serum as a wave table or a noise, etc.

2. As administrator, from the install directory, run the command:

`python serum-file-fix.py`

3.  All of Serum's open samples should no longer be open in the background now, and the file should have imported in to serum.  The files should still play and be visible in the playlist.

## Notes

Tested with Windows 10 and Ableton 11 Suite.  You could probably make it work with other Abletons by editing serum-file-fix.py, and changing the reference to the .exe name to whatever is relevant.
