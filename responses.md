# CSCI2390 Assignment 3: Differential Privacy

## Question 1
_"Look at the result of this count query. Note that it does not include any name, email, or other personally identifiable information. What can you nevertheless learn about Kinan's musical tastes? What possible genres might they have chosen? Alternatively, what genres is it impossible for them to have chosen?"_

When we use the API to count the data grouped by music and age, we get a pretty large number of entries for ages like 20 and 21 but very few for ages close to 30. Given the very basic knowledge I have of Kinan's occupation, I am able to rule out a good number of entries. They are very likely to be older than 24, which suggests that they can either be 27, 29, or 30 based on the data (more likely the oldest as the prof.)
This means that Kinan is likely to listen to one of pop, rock, or **metal** — most likely the latter. This also means that they surely didn't choose hip-hop, house, or country, since only people 22 or younger chose any of these genres.

## Question 2
_"Look Kinan up online and try to find information about their musical taste. You can start by Googling Kinan Bab and checking the first few pages of results. Prioritize results from online services where musical taste may be relevant. "_