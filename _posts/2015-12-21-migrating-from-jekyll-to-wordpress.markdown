---
layout: post
title: 'Migrating from Jekyll to WordPress'
date: 2015-12-21
tags: ["Development"]
---

So recently, I decided to resurrect my blog. It was built on top of a tool called Jekyll, which is a static website generator, written in Ruby. It essentially worked like WordPress (with its own famous “loop”), with page/post templates written in HTML and Liquid (a templating engine), and pages/posts themselves written in Markdown. You’d simply run a build command, and Jekyll would spit out a full website, ready for upload to a server.

It worked great for the short period I was into blogging. The downsides were that I could only blog from the computer I had Jekyll completely setup on, and it required a Linux environment to work painlessly (Windows just didn’t work for me). When I decided to pick up blogging for me, I wanted to be able to blog from any computer, preferably through a web interface. Given that I had the most experience with WordPress, I figured I’d try switching over.

Man – it was **easy**! For the most part, anytime I saw a Liquid tag that meant something for Jekyll (something like `{{ page.title }}`, I’d just replace it with the WordPress/PHP equivalent. Once all my templates were encapsulated in PHP tags, and all the files were renamed so that WordPress would recognize them, I was 90% done. Just the typical bugs to be ironed out, is all.

It certainly helped that I was migrating from Jekyll to WordPress – had it been the reverse, and I was reliant on widgets and plugins, I’d probably be stuck pretty early on.
