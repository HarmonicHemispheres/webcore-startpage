# webcore-startpage
A fun and expandable Web browser Startpage Generator written in python 3.6

<br>
<br>

![webcore](https://github.com/HarmonicHemispheres/webcore-startpage/tree/master/Info/webcore-demo.png?raw=true)

# OVERVIEW
The purpose of webcore is to provide a script which can generate an easily customizable html file for you to set as your homepage on any browser. 

## USE
To use the program, minimal work is required. 

### 1) clone the repo
`% git clone https://github.com/HarmonicHemispheres/webcore-startpage.git`

### 2) add links to data.txt 
Webcore uses takes the links and images referenced in data.txt to generate html in webcore_gen.py. Every line in data.txt should follow:<br>
`category link_to_site path_to_img`<br>
this can also be seen in the data.txt file on this site. all image paths should consider the webcore project folder as the root folder.

### 3) add settings to webcore_gen.py
The Webcore generator file is what brings it all together. at the top of the script are a number of settings in the USER VARIABLES section. here we will describe the function of each parameter.
#### Layout Options

| Parameter | Description | syntax/example |
|:-----------|:-------------|:--------|
| title     | the title of the page | "title" |
| background_color | background color | "#000000" |
| fastlink_color | container background colors | "#000000" |
| fastlink_padding | space between the images and container edge | "0px" |

#### Title Font Options

| Parameter | Description | syntax/example |
|:-----------|:-------------|:--------|
| font     | path to a custom font | "fonts/Trattatello.ttf" |
| font_color | title font color | "#000000" |
| font_size | title font size | "15px" |
| font_bar_margin | vertical width of the fastlink background around the title | "0px" |

#### Link Image Options
NOTE: choosing a hover animation too high can result in the page getting freaking out, safest option is 0px of hover_animation_dist.

| Parameter | Description | syntax/example |
|:-----------|:-------------|:--------|
| img_size | size of the images for the links | "85px" | 
| hover_speed | length of hover animation | "0.2" |
| hover_animation_dist | how far the images slide during animation | "15px" |
| hover_strength | opacity of images during hover range (0-1) | "0.3" |

#### Web Terminal & Search Options
| Parameter | Description | syntax/example |
|:-----------|:-------------|:--------|
| term_bg_color | search bar and terminal bar background color | "#000000" |
| term_font_color | color of text in the terminal and search bar | "#000000" |

### 4) generate html!
Now that you have all your settings and links the way you want, all you have to do is run the webcore_gen.py. todo this open terminal.
```
% cd /path/to/webcore_gen.py
```
Once in the directory run the script
```
% ./webcore_gen.py
```
the script outputs a file called `output.html` this file must stay in the current directory or links to the resources will be messed up. Now you have a html file you can launch in your browser!

<br>
<br>

## BROWSER SETUP
Even though you have the html, the last step to make this useful is to set this html file as your browser's homepage.

### FIREFOX
1) goto: preferences -> general
2) set homepage to: path/of/your/output.html
3) additionally add the ability to goto your homepage when you make a new tab with this plugin https://www.basson.at/firefox-addons/newtabhomepage


### CHROME
1) goto: settings -> Apperance
2) click "change" under "show home button" and set link to: path/of/your/output.html

<br>
<br>

## FUTURE DIRECTIONS
This project is still in its inception and as a simple fun side project some future endevors still to be done include:

* Make this readme cleaner to read and include a section for the web terminal
* add ability to display rss feeds with a web terminal command
* clean up the webcore_gen.py by parsing out sections of the html file to seperate files
