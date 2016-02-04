# himawaripy
*Put near-realtime picture of Earth as your desktop background*

himawaripy is a Python 3 script that fetches near-realtime (10 minutes delayed)
picture of Earth as its taken by
[Himawari 8 (ひまわり8号)](https://en.wikipedia.org/wiki/Himawari_8) and sets it
as your desktop background.

Set a cronjob that runs in every 10 minutes to automatically get the
near-realtime picture of Earth.

## Supported Desktop Environments
### Tested
* OS X


## Configuration
You can configure the level of detail, by modifying the script. You can set the
global variable `level` to `4`, `8`, `16`, or `20` to increase the quality (and
thus the file size as well). Please keep in mind that it will also take more
time to download the tiles.

## Installation

This uses the system python as installed by Apple. So you need to install `Pillow` as shown below. This was a quick edit from a project I saw and I've been too lazy to see if I can pip install the pyobjC libraries into a homebrew python


    /usr/bin/easy_install Pillow

    cd ~
    git clone https://github.com/mzupan/himawaripy.git
    cd himawaripy
    
    # test whether it's working
    ./himawaripy.py
    
    # set up a cronjob
    crontab -e
    # Add the line:
    # */20 * * * * /home/USERNAME/himawaripy/himawaripy.py >/dev/null 2>&1
    
## Example
![Earth, as 2016/02/04/13:30:00 GMT](http://i.imgur.com/4XA6WaM.jpg)
    
## Attributions
Thanks to *[MichaelPote](https://github.com/MichaelPote)* for the [initial
implementation](https://gist.github.com/MichaelPote/92fa6e65eacf26219022) using
Powershell Script.

Thanks to *[Charlie Loyd](https://github.com/celoyd)* for image processing logic
([hi8-fetch.py](https://gist.github.com/celoyd/39c53f824daef7d363db)).

Obviously, thanks to the Japan Meteorological Agency for opening these pictures
to public.
