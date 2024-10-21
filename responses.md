# CSCI2390 Assignment 3: Differential Privacy

## Question 1
_"Look at the result of this count query. Note that it does not include any name, email, or other personally identifiable information. What can you nevertheless learn about Kinan's musical tastes? What possible genres might they have chosen? Alternatively, what genres is it impossible for them to have chosen?"_

When we use the API to count the data grouped by music and age, we get a pretty large number of entries for ages like 20 and 21 but very few for ages close to 30. Given the very basic knowledge I have of Kinan's occupation, I am able to rule out a good number of entries. They are very likely to be older than 24, which suggests that they can either be 27, 29, or 30 based on the data (more likely the oldest as the prof.)
This means that Kinan is likely to listen to one of pop, rock, or **metal** — most likely the latter. This also means that they surely didn't choose hip-hop, house, or country, since only people 22 or younger chose any of these genres.

## Question 2
_"Look Kinan up online and try to find information about their musical taste. You can start by Googling Kinan Bab and checking the first few pages of results. Prioritize results from online services where musical taste may be relevant. What did you find out about Kinan? Are your findings consistent with Question 1? Combine the two together to learn Kinan's exact age."_

I scrolled through and found Kinan on a bunch of different platforms: their personal website, twitter, LinkedIn, youtube, and so on. In most, __they directly reference their passion for metal__. On Twitter, they repost clips of metal performances. On Youtube, they have playlists of videos for metal. It seems like my initial thought—that Kinan might have picked metal–is accurate. Since there are only two people who selected metal in the dataset, one of whom is only 21 years old, the other must be Kinan. This means that **Kinan is 30 years old!**

### Question 3
_"Identify Kinan's favorite color. What is it? How easy or obvious is this to do, and why?"_

Now that we know Kinan's age, it is very straightforward to find their favorite color, since there seems to be only one individual with that age. So, finding their favorite color is as simple as looking at the only row entry corresponding to their age. Kinan's favorite color is **black**.

## Question 4
_"What information can you learn about Kinan's favorite sport from the above query?"_

Since Kinan is in the "25 or more" agegroup, they can either have indicated a favorite of basketball or soccer. So they definitely did not indicate American football or baseball!

## Question 5
_"Combine what you learn from both datasets to learn more information about Kinan's favorite sport. What is Kinan's favorite sport?"_

Since Kinan's data did not change from last year and nor did their age group (if they are 30 this year they were 29 last year), we can be sure that Kinan indicated one of American Football, Soccer, or E-Sports last year. If we compare these with the options for this year–soccer and basketball–we can conclude with surety that Kinan's favorite sport is **soccer**!

