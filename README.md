# Digital Cane

We all use internet on a daily basis and we've all encountered one common, annoying thing: CAPTCHA. 
That's the thing which verifies whether the person requesting some web content, is a human or not. 
While it's not that difficult for us normal users, it is quite a challenge for the visually impaired. 
The visually challenged people use computers and browse internet, with the use of text-to-speech softwares.
You might think audio CAPTCHAs solve the problem, but they don't. They just make things worse.

So, what do they do? How can a blind person using the internet prove he's not a robot? This project is an attempt at solving the respective problem. This was a team project, presented at **Smart India Hackathon (SIH)** 2020.

## Our approach

![CAPTCHA page](Md-images/main screen.png)

Assuming that the concerned person is using a text-to-speech software:

* Instead of the typical CAPTCHA page, he/she will be redirected to our page (think of it like a service), which simply consists of some text and one form entry.
* The user will be provided with a simple question, that any person will generally know and such that, the answer is always a number. Eg.: 'How many sides does a square have?', answer is **4**.
* Now the user has to remember the answer and consider it as some position. In the above eg. case, he/she will have to remember **'4'** as **'some position'**.
* Then a list of, random and easy-to-spell, english words will be generated(usually 7 words). Now the user has to figure out that word, that exists at the **'position'** they previously had to remember.
* Say, for e.g, the words : "car, hand, mouse, phone, chair, pad, fan" are generated. The **'answer'** we had to remember was the number **'4'**. 
* Then we figure out, among the generated words, what word existed at the postion we remember as an answer. In the above case, it's the word **'phone'**, as it's at the **4th** position.
* Then this word is entered in the form and the user will click 'submit'. If it all checks out, then they've **passed** the CAPTCHA test. Then they're redirected to the site they wanted to visit in the first place.

Ok so that was a lot to follow. If you're still unclear, check this out: 

Keep in mind that this is purely a creation of students and we don't claim that this will work perfectly, lol. I know there's a lots of gaps in this idea and many assumptions are made as well. After presenting this in **SIH**, we were criticized of many loop holes , such as "How can you be sure that 'bots' cannot crack it?", 
"How does this solve the problem of CAPTCHA?" and the best: "Do you really think this is a problem? Only a tiny percentage of people are blind and that too, those who use internet. *Are you sure this problem is even worth solving?*". 
I mean, we took this problem statement from the SIH page, so this does definitely exist, just that we don't know on what scale. 

Anyways SIH was fun and, me and my team could learn a bit at least, if not win the competition. And I thougth it'd be better if I put it on GitHub, and in that way its not a complete waste :P 

For some reason, if you want to contribute:
* Clone/Download this repo.
* Only dependency is [flask](https://flask.palletsprojects.com/en/1.1.x/), so make sure you have that installed.
* Start developing! 



