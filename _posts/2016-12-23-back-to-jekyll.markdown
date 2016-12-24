---
layout:  post
title:  "Back to Jekyll"
date:  2016-12-23
tags:  [Blogging, Development]
---
Well, I've gone full circle - I switched [from Jekyll to WordPress]({{site.baseurl}}{% post_url 2015-12-21-migrating-from-jekyll-to-wordpress %}) in 2015,
and I've recently finished doing the reverse. Maybe I just love constantly switching things up, or maybe I made the switch because of the allure of
Github Pages!

Just like the original migration to WordPress, getting my very simplistic theme up and running was incredibly simple, since WordPress and Liquid operate pretty similarly. It really boiled down to replacing PHP with Liquid tags, and cutting out more WordPress cruft, and I was on my way!

The difficulty was with post content - this is because Jekyll requires posts to be formatted in Markdown, which isn't something you can easily get a bunch of WordPress posts. There are automatic WordPress to Jekyll converters, which can be used to convert your pages and posts into Markdown, but it was no good for me - they required PHP version 5.5 or higher, and with my free webhost, I was restricted to 5.2.x. So, I started looking for any generic tool that could convert already written WordPress posts into Markdown, and then I found the [Ghost export tool](https://wordpress.org/plugins/ghost/).

Ghost is an online blogging platform similar to WordPress, but rather than using rich formatted text or HTML to write your posts, you write them *in Markdown*! This was exactly what I needed, and so I quickly installed and ran the plugin - it generated a JSON file that looked a bit like this:

```
{
  "data":
    {
      "posts":  [
        {
          "id":  6,
          "title":  "About",
          "slug":  "about",
          "markdown":  "Post contents in Markdown",
          "html":  "Post contents in HTML",
          "image":  null,
          "featured":  0,
          "page":  1,
          "status": "published",
          "language": "en_US",
          "meta_title": null,
          "meta_description": null,
          "author_id": 1,
          "created_at": "Sun, 20 Dec 2015 01: 00: 43 +0000",
          "created_by": 1,
          "updated_at": "Tue, 20 Dec 2016 13: 50: 12 +0000",
          "updated_by": 1,
          "published_at": "Sun, 20 Dec 2015 01: 00: 43 +0000",
          "published_by": 1
        }
    ]
  }
}
```

Each post and page on my site had an entry in the `posts` array - a lot of the data was meaningless for me, but the key pieces were there: the title of the post, the date of publication, and the post's contents, already converted to Markdown. Looking back, it even had the `slug` attribute, which I could have used as a Jekyll `permalink`, so that each post would have a pretty URL. The one thing noticeably missing was the tags associated with each post, which seems a bit odd since each Ghost appears to support tagging posts.

Of course, extracting each post manually from the JSON would be an incredible waste of time - why not just automate it?

```python
from datetime import datetime
import json

json_data = open("wordpress-export.json").read()
data = json.loads(json_data)

for elm in data ['data'] ['posts']:

    # Get the post's date of publication
    dateString = datetime.strptime(elm ['updated_at'], "%a, %d %b %Y %X %z")
    dateString = dateString.strftime("%Y-%m-%d")
    title = elm ['title']

    # Create a properly formatted file name for Jekyll
    fName = dateString + "-" + title.lower().replace(" ", "-").replace(":", "") + ".markdown"
    print("Processing: " + fName)
    f = open("_posts/" + fName, "w")

    # Write front-matter
    f.write("---\nlayout: post\ntitle: '" + title + "'\ndate: " + dateString + "\n---\n")

    # Write post contents
    f.write(elm ['markdown'].replace("\u00c2", ""))
    f.close()
```

The only weird thing I had to do was the line where I wrote the post's contents to the file; for some reason, the JSON file had the `\u00c2` character sprinkled about randomly through the Markdown.

Once that was done, it was just a matter of polishing the end result - changing a few CSS rules here and there, and updating the templates for the [Projects]({{site.baseurl}}/projects) and [About]({{site.baseurl}}/about) pages. Connecting it with my domain was pretty painless too; with Namecheap, I had to create a new "A record" pointing to Github's servers, and the changes took effect pretty quick.

At the end of the day, my blogging workflow became greatly simplified. Now, I just have to open Atom, use `Ctrl-Shift-M` to get a Markdown preview, bang out a post, and then push it to Github. Unlike the old days with Jekyll, I don't have to FTP the produced `_site` folder; Github Pages takes care of processing the site for me. Hopefully this will encourage me to write more, more often.
