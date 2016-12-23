from datetime import datetime
import json

json_data = open("wordpress-export.json").read()
data = json.loads(json_data)

for elm in data ['data'] ['posts']:
    
    # Parse JSON to get date and post title
    dateString = datetime.strptime(elm ['updated_at'], "%a, %d %b %Y %X %z")
    dateString = dateString.strftime("%Y-%m-%d")
    title = elm ['title']
    fName = dateString + "-" + title.lower().replace(" ", "-").replace(":", "") + ".markdown"
    print("Processing: " + fName)
    
    # Open file
    f = open("_posts/" + fName, "w")
    
    # Write front-matter
    f.write("---\nlayout: post\ntitle: '" + title + "'\ndate: " + dateString + "\n---\n")
    
    # Write post contents
    f.write(elm ['markdown'].replace("\u00c2", ""))
    
    # Close file
    f.close()