backup-rally
============

A simple python script to backup rally test sets and test cases.(Very much WIP)

Installation
------------
1. This script is tested on Python27, lesser versions will not work (pyral depends on 2.7), higher versions are untested. To check if you have python installed run:  
    ````python --version````  
If you do not have python, then grab it (tested on CPython only) from the [Python website](http://www.python.org/download/releases/2.7.3/) and run the appropriate installer
If you DO have python and pip installed already, go ahead and skip to step x.  
2. Once python is installed, you need to grab pip, which doesn't *really* boil down to one installation instruction but you'll need to grab easy_install probably and then download pip. Here are the instructions for doing it on 64-bit windows which is where it was developed (adapted from [this stackoverflow answer](http://stackoverflow.com/a/9038397/1167456)):  
	* First you need to obtain easy install (either use the curl line below or do save link as on the link below and then open a command window to the directory where you saved it):  
	    ````curl -O http://peak.telecommunity.com/dist/ez_setup.py````
	* Now run:  
	    ````python ez_setup.py````
	* After that is successful, you will need to manually update your PATH (Control panels -> system -> advanced system settings -> environment variables) to include this folder (this is the default location, change it if you installed python elsewhere):  
	    ````C:\Python27\Scripts````  
	* Then run:  
	    ````easy_install pip````
3. Once pip has been obtained and installed you'll need 3 more dependencies(requests 0.9.3, pyral and Jinja2) so run this command:  
   ````pip install requests==0.9.3 pyral Jinja2````

More information and troubleshooting steps for installing pyral can be found here:  
<http://developer.help.rallydev.com/python-toolkit-rally-rest-api> 


Set-Up
------
1. From the backup rally folder do (make a duplicate in explorer):  
    ````cp settings.cfg.template settings.cfg````
2. Open the new settings.cfg file and fill in all required information (Server, Username and Password)

Usage
-----

Usage is simple (but make sure to read this entire section):  
	````python backup-rally.py --conf=settings.cfg "iteration"````  
In place of "iteration" type a partial or full match to the name of the iteration you want to return all test cases.  
Here is an example to pull in iteration 1302 (remember that iteration is phrased 13.02 in rally!):  
	````python backup-rally.py --conf=settings.cfg 13.02````  
NOTE: You will probably have to run it a few times to get it to work, the first 1-2 times will likely give you an error message about "server not existent" or similar. It should work fine after the first couple times.

Features to be Added / Known limitations
-----
At the moment all test cases will be printed as TS#-TC#.html next on the TODO list is making it create new folders for each testset.
