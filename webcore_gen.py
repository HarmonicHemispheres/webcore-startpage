#!/usr/bin/env python3

#   Author: Robby Boney
#   Version: 0.1.0 alpha

# ============================================================
# ============================================================
# ====================== USER VARIABLES ======================

# ===== Layout Options =====
title = "WebCore"
background_color = "#003333"
fastlink_color = "#008080"
fastlink_padding = "0px"

# === Title Font Options ===
font = ""
font_color = "#003333"
font_size = "15px"
font_bar_margin = "0px"

# === Link Image Options ===

img_size = "85px"
hover_speed = "0.2s"
hover_animation_dist = "5px"       # recommended range is 0px - 50px, but 0px is safest
hover_strength = "0.3"              # range is 0 - 1

# ===== Web Terminal & Search Options =====

term_bg_color = "#4dffff"
term_font_color = "#001a1a"

# ============================================================
# ============================================================
# ============================================================

data = open("data.txt", "r").read().splitlines()
output = open("output.html", "w+")


if (font != ""):
    font_tag = """
            @font-face{
                font-family: """+ font.split(".")[0] +""";
                src: url("""+ font +""");
            }
    """
    font = font.split(".")[0]
else:
    font_tag = ""
    font = 'arial'
mainfile = '''<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"> 
        <title>WebCore StartPage</title>
    <style>
            '''+ font_tag +'''
            body{
                background-color: ''' + background_color + ''';
            }
            .container:hover .overlay {
                opacity: '''+ hover_strength +''';     
                margin-left: '''+ hover_animation_dist +''';
                margin-right: '''+ hover_animation_dist +''';
            }
            .overlay {
                opacity: 1;
                transition: '''+ hover_speed +''' ease;
            }   
            #main{
                background-color: ''' + fastlink_color + ''';
                margin-left: auto;
                margin-right: auto;
                width: 80%;
            }
            #gsearch{
                height: 30px;
                font-size: 15px;
                text-align: center;
                width: 90%;
            }
            #webterm{
                height: 30px;
                font-size: 15px;
                text-align: center;
                width: 90%;
            }
            #fast_links{
                background-color: ''' + fastlink_color + ''';
                display: inline-block;
                margin: 10px;
                padding-left: '''+ fastlink_padding +''';
                padding-right: '''+ fastlink_padding +''';
            }
            #links{
                display: inline-block;
            }
            #colpic{
                width: 500px;
                height: 500px;
            }
            #caleandar{
                background-color: ''' + fastlink_color + ''';
                color: #111111;
                padding: 10px;
                border: solid black 5px;
            }
            input[type=text] {
                background-color: '''+ term_bg_color +''';
                color: '''+ term_font_color +''';
                border: none;
            }
            img{
                vertical-align: bottom;
                
            }
            #titles{
                font-family: '''+ font +''';
                color: '''+ font_color +''';
                font-size: '''+ font_size +''';
                letter-spacing: 1px;
                margin-top: '''+ font_bar_margin +''';
                margin-bottom: '''+ font_bar_margin +''';
            }
    </style>
    <link rel="stylesheet" href="css/theme2.css"/>

    </head>
    <body>
        <script type="text/javascript" src="js/checks.js"></script>
        <br><br><br><br>
        <div id="main" align="center">
            <br><br>
            <form method="get" action="https://www.google.com/search">
                <input id="gsearch" type="text" name="q" size="90%" value="" placeholder="search google" />
            </form>
            <br>
            <form action="#" onsubmit='launchTerm(document.getElementById("webterm"))'>
                <input id="webterm" type="text" size="90%" value="" placeholder="web terminal (type help)" />
            </form>
            <br><br>
        </div>
        <br>
        <center>
        <div id="help" style="background-color: '''+ fastlink_color +'''; display: none;" >
            <table cellspacing=10px style="border-spacing: 50px 0;" >
                <tr> <th>Command</th> <th>Function</th></tr>
                <tr> <td>help</td> <td>toggles this help box</td></tr>
                <tr> <td>color</td> <td>toggles w3schools color picker</td></tr>
                <tr> <td>cal</td> <td>toggles to a calendar </td></tr>
            </table>
        </div>
        <div id="links">
            <div id="colpic" style="display: none;">
                <iframe id="colpic" src="https://www.w3schools.com/colors/colors_picker.asp"></iframe>
            </div>

            <div id="caleandar" style="display: none;">

            </div>

            <script type="text/javascript" src="js/caleandar.js"></script>
            <script type="text/javascript" src="js/basic.js"></script>'''


output.write(mainfile)
categories = []
old =""
data.sort()

for i in range(len(data)):
    if (old == ""):
        old = data[i].split()[0]
        tags = '            <div id="fast_links">\n'
        output.write(tags + "              <p id='titles'>" + data[i].split()[0] + "</p>\n                 <!--")

    elif (data[i].split()[0] != old):
        old = data[i].split()[0]
        tags = """                 -->
            </div>
            <div id="fast_links">
        """   
        output.write(tags + "      <p id='titles'>" + data[i].split()[0] + "</p>\n                 <!--")
    output.write('                 --><a class="container" href="'+data[i].split()[1]+'"><img class="overlay" src="'+ data[i].split()[2] +'" width="'+img_size+'" height="'+img_size+'"></img></a><!--')

end = """                 -->
            </div>
            </center>
            <br><br><br>
        </body>
</html> 
"""

output.write(end)
output.close()
