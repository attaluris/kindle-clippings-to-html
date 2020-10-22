# -*- coding: utf-8 -*-
excerpts = []

# processing step
clippings_file = open('My_Clippings.txt', 'r') 
clippings_lines = clippings_file.readlines() 

excerpt_dict = {}
for i in range(len(clippings_lines) / 5):
    excerpt_dict = {
        "title_author": clippings_lines[i * 5].rstrip(),
        "page": clippings_lines[i * 5 + 1].split('page')[1].split(' ')[1],
        "excerpt": clippings_lines[i * 5 + 3].rstrip()
    }
    
    excerpts.append(excerpt_dict)

# HTML creation step
clippings_html = open("clippings.html", "w")
pretext = "<html>\r\n    <head>\r\n        <meta charset=\"utf-8\">\r\n        <meta http-equiv=\"X-UA-Compatible\" content=\"chrome=1\">\r\n        <title>Sritej\'s clippings</title>\r\n        <link rel=\"icon\" href=\"assets/four.jpg\">\r\n        <link rel=\"stylesheet\" href=\"css/main.css\">\r\n        <script type=\"text/javascript\" src=\"js/main.js\"></script>\r\n        <meta name=\"viewport\" content=\"width=device-width\">\r\n    </head>\r\n    <body>\r\n        <div class=\"wrapper\">\r\n            <div>\r\n                <a href=\"http://www.sritej.com\">← back to site</a>\r\n            </div>\r\n            <div class=\"top\">\r\n                <h1><B>Clippings from books I\'ve read</B></h1>\r\n            </div>\r\n            <hr />\r\n            <div>\r\n   \t\t\t<input type=\"text\" id=\"myInput\" onkeyup=\"myFunction()\" placeholder=\"Search clippings...\">\r\n   \t\t\t<div style=\" overflow: scroll; height: 600px; padding: 5px; \">\r\n\t\t\t\t<ul id=\"myUL\">\r\n"
clippings_html.write(pretext)
for excerpt in excerpts:
    clipping_item = "\t\t\t\t  <li><a href=\"#\">" + "\"" + excerpt["excerpt"] + "\" -- Page " + excerpt["page"] + ", " + excerpt["title_author"] + "</a></li>\r\n"
    clippings_html.write(clipping_item)

posttext = "\t\t\t\t</ul>\r\n\t\t\t</div>\r\n        </div>\r\n    </body>\r\n</html>\r\n<script>\r\n\tfunction myFunction() {\r\n\t  // Declare variables\r\n\t  var input, filter, ul, li, a, i, txtValue;\r\n\t  input = document.getElementById(\'myInput\');\r\n\t  filter = input.value.toUpperCase();\r\n\t  ul = document.getElementById(\"myUL\");\r\n\t  li = ul.getElementsByTagName(\'li\');\r\n\r\n\t  // Loop through all list items, and hide those who don\'t match the search query\r\n\t  for (i = 0; i < li.length; i++) {\r\n\t    a = li[i].getElementsByTagName(\"a\")[0];\r\n\t    txtValue = a.textContent || a.innerText;\r\n\t    if (txtValue.toUpperCase().indexOf(filter) > -1) {\r\n\t      li[i].style.display = \"\";\r\n\t    } else {\r\n\t      li[i].style.display = \"none\";\r\n\t    }\r\n\t  }\r\n\t}\r\n</script>"
clippings_html.write(posttext)
    
clippings_html.close()
