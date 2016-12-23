---
layout: post
title: 'Contributing to open source for the first time'
date: 2015-12-25
tags: ["Development", "Experiences"]
---

Over the summer – my last one before starting university – I was looking for a project to get into. I had a Github account, and I’d worked on a bunch of small personal projects before, but never had I contributed to someone else’s work. It just seemed too hard; how could I contribute anything of value to a project I didn’t create?

That same summer, I also rediscovered my interest in Google Chrome browser extensions. I spend a lot of time in the browser, and thought it’d be cool to develop an extension of my own, something to “itch my own scratch”. I found it even cooler when I realized you could just whip ’em up with good ol’ HTML/CSS/JavaScript. So hey, why not just contribute to a Chrome extension project somewhere?

> If you’re interesting in developing your own Chrome extensions (they’re really cool), I’d simply head over to [https://developer.chrome.com/extensions/getstarted](https://developer.chrome.com/extensions/getstarted) and hack away!

 

One of my favorite Chrome extensions is [Awesome Screenshot](https://chrome.google.com/webstore/detail/awesome-screenshot-minus/bnophbnknjcjnbadhhkciahanapffepm?hl=en), a handy tool for, as you guessed it, taking screenshots. I take a bunch of screenshots when browsing the web; sometimes it’s for amusement and sharing, other times to explain a problem better, since a picture tells a thousand words. I was using Awesome Screenshot, and realized there was no easy way to save screenshots to Google Drive, the cloud platform of choice for me. A quick Google search pulled up the extensive Drive API, and I realized I could probably just hack this together myself. Here goes.

 

After an hour or two, I had a working product, but one that didn’t fit my needs. The biggest issue, for me, was folder navigation – say I wanted to save a screenshot in the “Screenshots” folder nested inside the “My Drive” folder; how would I do that? It became a bit of a debacle in terms of both UI and logic to implement; eventually, I got things working, and looking back on it, realized I basically just implemented the idea of a file path. If only I’d realized the problem I was dealing with had only been solved. Regardless, after bit of a polishing, I had a hacked together feature *I was**proud of*.

 

<div class="wp-caption aligncenter" id="attachment_51" style="width: 710px">![Eureka - I can traverse the file hierarchy! ](http://joshkayani.me/wp-content/uploads/2015/12/screenshot2-1024x499.png)Eureka – I can traverse the file hierarchy!

</div> 

Remember how I wanted to have something to put on Github? Well it turns out, Awesome Screenshot was hosted on there, and the developer was happily accepting contributions. So, I downloaded the Github client for Windows, read up on the general rules/guidelines to requesting a pull request, and tried my luck. I’m happy to say that after a revision or two (mainly code style), my first pull request was accepted. I’d done it – I contributed to open source, all from scratching my own itch!

 
