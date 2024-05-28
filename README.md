# ASCIIscape
<div><img src="https://i.imgur.com/eMJS0Da.png" alt="asciiscape"></div>
<div><a href="https://pypi.org/project/asciiscape/"><img src="https://camo.githubusercontent.com/340246e46c5aa50acde0582093d8650c201d5c3ff31432a547ea625f700bad6d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d507950692d626c75652e7376673f6c6f676f3d70797069266c6162656c436f6c6f723d353535353535267374796c653d666f722d7468652d6261646765" alt="pypi icon"></a></div>

**ASCIIscape** is a simple Python CLI for converting images into ASCII that was made for CS50's final project.<br>
You can intall by running ```pip install asciiscape``` from your terminal.

## Usage

To run ASCIIscape type ```python -m asciiscape``` in your terminal of choice.<br>

Then provide the **PATH** of the **IMAGE** you want to convert.
<div><img src="https://i.imgur.com/9UYqcOK.png" alt="path usage" width="400"></div>
<p></p>

### Options
#### Style:
**COLOR** or **GRAYSCALE**: sets the resulting ASCII image to be printed either with color or in black and white, respectively.<br>
#### Charset:
**SMALL** or **BIG** or **BRAILLE**: sets the resulting ASCII image to be printed with a small charset (10 levels of brightness), a big charset (91 levels of 
                                       brightness) or a braille charset. 
#### If Braille Was Chosen:
**DITHER** and **THRESHOLD**: sets if the original image is to be dithered and the brightness threshold that the pixels are going to be compared against.
<div><img src="https://i.imgur.com/T9b08dS.png" alt="path usage" width="400"></div>
<p></p>

Choose your options and get your image converted to ASCII !

### Example

<div align="center"><img src="https://i.imgur.com/gh7CwD4.jpeg", alt="original", width="280" height="280"><img src="https://i.imgur.com/9HrFodC.png", alt="small charset", width="300" height="300"><img src="https://i.imgur.com/4wdDgVD.png", alt="braille charset", width="300" height="300"></div>
<p align="center">From left to right - Original, Small Charset, Braille Charset</p>


## Documentation

#### Source code

The code is divided into 3 separate files **"\_\_main\_\_.py"**, **"console.py"** and **"imgUtils.py"**:<br>

--->**"\_\_main\_\_.py""**  is mainly responsible for calling all of the functions from the other two functions, it's also the file that is run when the user types the command to start the application into the terminal.

--->**"console.py"** contains the functions that print text into the terminal and prompt the user for input, including the title, options, and ASCII image.

--->**"imgUtils.py"** contains all of the functions that relate to the processing of the images and arrays, including: loading and resizing images, converting an image to array of pixels, iterating through array of pixel, converting pixels to ASCII chars and dithering.

Roughly, the step by step, of how the program works is by taking the path of a image provided by the user and getting the conversion options, loading it with Pillow, resizing it to fit the terminal window, converting to a numpy array, where each element represents a pixel of the image, iterating through this array and converting each pixel into a ASCII character, which gets put into its own numpy array, then printing the ASCII character array with rich using the parameters chosen by the user.

The libraries <a href="https://github.com/python-pillow/Pillow">Pillow</a>, <a href="https://github.com/numpy/numpy">numpy</a> and <a href="https://github.com/Textualize/rich">rich</a> were used throught the entirety of the project. Pillow for the image loading and manipulation, numpy for working with arrays and rich for interaction with the terminal, without these libraries this project would not have been possible, so a massive thanks to all of them.

#### Package

This project is a Python package made with <a href="https://github.com/python-poetry/poetry">Poetry</a>, as such it has the main package folder "asciiscape", which contains the Python source code and the "\_\_init\_\_.py" file which defines the package. It also has the "pyproject.toml" file, which contains three tables, one that contains metadata about the package, another with the package dependencies and the last one with the Poetry dependencies.
