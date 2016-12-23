---
layout: post
title: "Winning at Hack NC 2016"
date: 11-05-2016
tags: [Development, Experiences]
---
Just like last year, the University of North Carolina at Chapel Hill and Major League Hacking teamed up to put on Hack NC 2016 - a 24 hour hackathon with the objective of building cool stuff, very fast. And, just like last year, I went - except this time, **we won something.**

I formed a team with two friends of mine, and immediately we started thinking about ideas from a political angle. It was a few months before the 2016 US Presidential election, arguably the most bizarre and controversial of recent history - could you really blame us? In any case, after mulling over a bunch of ideas, we discovered 3 political websites had API's that could give us potentially useful information:

* [Politifact](http://static.politifact.com/api/doc.html) - if you haven't heard of this one already, these are the people who rate politician's claims/statements based off how truthful they are. Their API allows you to retrieve, among other things, a set of statements and their corresponding "truth" ratings for any given politician in their database.
* [Open Secrets](https://www.opensecrets.org/resources/create/api_doc.php) - this is an interesting website that uses politician's FEC filings to analyze where campaign contributions are coming from; their API let's you ask how much money was contributed to any given candidate's campaign, from any particular industry, such as healthcare and national defense.
* [Five Thirty Eight](http://fivethirtyeight.com/) - this is a website that uses data-driven models to make predictions about many things, including the US political landscape; they provided an API that allowed us to ask for a given candidate's current stand in the polls.
So to put all this together, we decided to create a website that consolidated all this data in one place, to help educate American voters and let them choose their allegiances based off the facts; after all, the data doesn't lie. The site allows a user to choose a particular issue they're concerned about, and then displays information on the Republican, Democratic, and Libertarian presidential candidates; in particular, each candidate has information on:

Their current polling average, as pulled from Five Thirty Eight
Statement's they've made concerning the user-chosen issue, as well as the truthfulness of the claim, as rated by Politifact
A list of campaign contributions from industries relevant to the user-chosen issue, provided by the Open Secrets database.
It took a long time to put together, and if you'd asked us how it was coming along on Saturday afternoon (the project's were due Sunday morning), the outlook would've been quite bleak. We were running into issues trying to do everything client-side, which in retrospect, was obviously a silly choice. To remedy this, we decided to use the Django Python framework, combined with Bootstrap to make an easy, good looking UI - this made it infinitely easier to process data retrieved via the above REST API's.

We also hit a snag with the Open Secrets API, in that there was a tight limit on the number of allowed API calls - throughout the development of the site, we probably burned through 3 or 4 API keys! The even bigger problem however, was the time it took to query their database - there was a point where it took at least 1 minute for a POST request to return with data. This was fixed by doing 1 pull every few hours, a sort of "caching" solution - since it was just campaign finance information, which isn't subject to wildly fluctuate in the span a few hours, this was an acceptable solution. And of course, there was a huge performance improvement!

By the time Sunday morning came, we were pretty happy with our work - unlike last year, we managed to actually fully implement our idea! Fortunately, the judges agreed - many were very appreciative of our work, and thought it was pretty cool - we were pretty busy talking to judges for the most of the judging period. In the end, we won a $500 cash prize from Infusion, one of the many corporate sponsors at the hackathon.

All in all, I learned a lot, both in a technical and political sense - I came away $167 richer than I arrived, and with something interesting to write about. The experience was definitely the most valuable reward, and I hope it lets me pull this off again next year!

Oh right - [here's a link to the final product.](http://candidata.herokuapp.com/results/)
