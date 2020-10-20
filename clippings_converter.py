print("starting script")

excerpts = []

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
    
for excerpt in excerpts:
    print("\"" + excerpt["excerpt"] + "\"")
    print("-- Page " + excerpt["page"] + ", " + excerpt["title_author"] + "\n")
