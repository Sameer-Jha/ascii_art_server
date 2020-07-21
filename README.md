# ASCII art server

Usage:

Simply send a get request to the domain: [***picascii.herokuapp.com***](picascii.herokuapp.com)

eg. `curl picascii.herokuapp.com`

output :

![](/home/sam/main/src/web_pro/ascii_meme_api/ss.png)

> A step further add this to alias : `alias ascii='curl picascii.herokuapp.com`
>
> or 
>
> Run this command for permanent alias : `echo "alias ascii='curl picascii.herokuapp.com'" >> ~/.bashrc`
>
> You may replace the .bashrc with rc file of your shell

A flask based app based on scraping and generation to give you random ascii art pieces.

> **[ASCII art](https://en.wikipedia.org/wiki/ASCII_art)** is a [graphic design](https://en.wikipedia.org/wiki/Graphic_design) technique that uses [computers](https://en.wikipedia.org/wiki/Computer) for presentation and consists of pictures pieced together from the 95 printable (from a total of 128) [characters](https://en.wikipedia.org/wiki/Character_(computing)) defined by the [ASCII](https://en.wikipedia.org/wiki/ASCII) Standard from 1963 and ASCII compliant character sets with proprietary  extended characters (beyond the 128 characters of standard [7-bit ASCII](https://en.wikipedia.org/wiki/7-bit_ASCII)). The term is also loosely used to refer to [text based visual art in general](https://en.wikipedia.org/wiki/ASCII_art#Other_text-based_visual_art).

An ASCII art example:

> ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⠉⠀⠀⠀⠀⠉⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
> ⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿
> ⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿
> ⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣆⠀⠀⠀⠈⣿⣿⣿⣿⣿
> ⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡏⠀⠀⠀⠀⢹⣿⣿⣿⣿
> ⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣠⣤⣤⣤⣴⣶⣾⣿⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿
> ⣿⣿⣿⣿⣧⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿
> ⣿⣿⣿⣿⣿⡄⣴⠾⠟⢛⣿⡿⠋⠙⠛⠛⢿⡟⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿
> ⣿⣿⣿⣿⣿⣿⣄⠀⣴⣿⠋⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿
> ⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣶⣶⣶⣶⣶⣶⣿⣷⣶⣦⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿
> ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿