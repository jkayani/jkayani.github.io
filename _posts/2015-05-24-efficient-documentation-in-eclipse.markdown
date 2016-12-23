---
layout: post
title: 'Efficient documentation in Eclipse'
date: 2015-05-24
---

Many Java developers, budding and veteran, use the Eclipse IDE – heck, I even used it in my AP Computer Science class in high school (even though it was technically taught with the BlueJ IDE). In the course, we were required to have documentation on the top of any Java classes we wrote in the following format:

```
<br></br>
Name```

Date

Assignment Name

Description

Difficulties

What was learned


 From looking at this, this seems like something that can be largely automated, right? The user’s name is probably stored somewhere, the date can be retrieved from the computer, and the assignment name is probably similar to the Eclipse project name – and that’s exactly what I did.

Eclipse offers a feature called “Code Templates”, which essentially allow you to create a template for any code and comments in your source. Template variables, such as the date or project name, can be accessed in this format: `${variableName}`.

So, all I had to do was edit the comment templates for files (accessed from Preferences > Java > Code Style > Code Templates), inserting `${name}`, `${date}`, and `${project_name}` variables in my comments, along with the text, giving me an easy “form” to fill out on the top of each new source file I created.

You might find it useful to insert a TODO at the top of your source files for remembering documentation tasks like descriptions for classes, etc.
