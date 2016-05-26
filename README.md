#UgTabs
======

Automatically selects and displays best tabs/chords available for a song from ultimate-guitar.com based on the user ratings on your default browser. Gives you the option to display the tabs in the console as well as save the file to an external text file. If the artist and song are not given as arguments the currently playing song is taken from Rhythmbox.

Dependencies
------------

- lxml
- bs4(BeautifulSoup 4)

Optional:

- rhythmbox-client to get the currently playing song from Rhythmbox

Installation
------------

Follow the usual Python paradigm

    sudo python setup.py install

or just run it directly

    ./ugtabs

Usage
-----

See the help output

    ugtabs --help
    or
    ugtabs -h

`ugtabs`, get the currently playing song from 
Rhythmbox if possible, then fetch its tabs/chords from ultimate-guitar and output 
them to your browser. The output mode can be changed with various optional arguments `-c` `-s` . The song title can be given as `ugtabs Hail to the king` or `ugtabs paranoid -c -n 3` ;the latter one displays 3 best tabs on your stdout. 

By default, ugtabs may select either tab or chords based upon the rating but you can force ugtabs to display only the tabs or chords by using `-o or --chords` or `-t` or `--tabs` arguments.
Example:

    ugtabs hey jude -c
    ugtabs voodoo child -t -n 2 -c

Author
------

Satkar Dhakal <satkar@satkardhakal.com.np>

Download
--------

- [From Github](http://github.com/satcar77/ugtabs)
