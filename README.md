Django-CMS Parallax Plugin
==========================
A Django-CMS plugin using the [Parallax-ImageScroll jQuery plugin](https://github.com/pederan/Parallax-ImageScroll) by 
Peder Andreas Nielsen, to achieve a simple parallax effect, very similar to the one utilised by 
[Spotify](https://spotify.com/). 

Installation
------------
Install latest development version from GitHub:

    $ pip install git+https://github.com/ovidner/djangocms-parallax.git#egg=djangocms_parallax

Add ``djangocms_parallax`` to your ``INSTALLED_APPS``:

    INSTALLED_APPS = (
        ...,
        'djangocms_parallax',
    )

Migrate your database:

    ./manage.py migrate djangocms_parallax

Usage
-----
Add a Parallax plugin to a (preferably empty) placeholder and add a few ParallaxImage and ParallaxContent plugins 
inside.

You probably want to style the elements with some custom CSS. The plugin plays well with Bootstrap, see 
extras/parallax.less directory for a LESS file you can customize and import in your Bootstrap setup.

License
-------
[MIT License](http://choosealicense.com/licenses/mit/)

The included Parallax-ImageScroll and Modernizr files are covered by their respective licenses.