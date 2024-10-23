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

## Part 2
_"Identify the sensitivity of the histogram query grouped by age and music taste."_
We touched upon this in class, but the sensitivity of the histogram grouped by age and music taste is **1**. Since each user's datapoint in a count operation has a value of 1, any neighboring table's values can be separated by at most 1 across all the rows. In general, any count operation has a sensitivity of 1, as removing a user can only ever change the count by 1.

## Question 6
_"What happens when the privacy parameter grows larger or smaller? How does that affect privacy?"_

When I run dp.py for different values of epsilon, it becomes clear that a smaller epsilon causes **greater privacy but less statistical significance**, and a larger epsilon makes values closer to the original but consequently less private. Starting with 0.01, the numbers were as good as random with how high the variability was on this distribution. In fact, most of the values produced seemed to be unhelpful ones until approx. `epsilon=5`. I ran `epsilon=10` a couple of times and saw no change to the values, which suggested that the degree of variability is miniscule.

One thought I had is about the fact that our noised values are taken with any factoring in of the actual count of values. Since the number of datapoints is so small, it should not be the case that we apply similar noising to this dataset as we would to thousands of datapoints.

## Question 7
_"Look at the plot generated with privacy parameter epsilon = 0.5. What is the most likely value? What is the expected (i.e., average) value? How do they relate to the actual value (i.e., the query excuted without any noise via client.py)? How does the plot change for different values of the privacy parameter?"_

Here is the plot for `epsilon=0.5`:
![Plot for epsilon=0.5](dp-plot-0.5.png)
I altered the code a bit to double check which the most common value is. As we expect, it is the **original value of the first row, 1**. This is expected, because the laplace distribution the noise is sampled from is centered at 0, which means that the added noise should most commonly be 0. In a couple of times that I ran this code, the most common was 0 and not 1. This is probably because of the fact that we are sampling from only 150 iterations, plus the impact of rounding on the shape of the laplace distribution.

I also modified the code to check for the average value. It seems like the average value is a little more than one: __1.307__. As we increase the number of iterations, I think that this number would get closer to 1, since the original value of that row is 1.

These are linked to the actual value, since with noise sampled from a laplace distribution, their values will likely converge to the actual value as we increase the number of iterations.

If we compare this plot to that of smaller epsilons, the variability that we discussed in the previous question becomes even more obvious. For The most frequent values can become further from the center and the frequency of the frequent values becomes less with respect to the number of iterations. This makes sense, since there is less frequency at the center of a laplace distribution with a smaller epsilon.

And if we compare this to a much higher value, we notice that the variability is extremely small in the higher values. More than 98% of the values for `epsilon=10` were the actual value, 1. Because of how we round the data and because of the number of observations we take, it seems like the laplace distribution can be most clearly seen around `epsilon=0.5`.

## Part 3
_"Can you deduce with high certainity Kinan's programming experience level? What if you run the query two, three, or more times?"_

When I ran this query a couple of times, I saw a variety of different values for each row. A lot of the times, the numbers just felt random, with people programming for longer being younger on average (which is pretty unlikely). I did notice that the "more than 10 years" category was seemingly centered around an average age of 29 or 30, but it is definitely not a sure conclusion I had.

## Question 8
_"Run the composition attack against the average age grouped by programming experience. What can you deduce from the exposed averages about Kinan's programming experience level? How confident are you in what you have deduced? Are there scenarios where they might be wrong?"_

Here's what we get from the denoised query:

| programming | AVG(age) |
| -------- | ------- |
| 0-3 Years | 23.03124029692182 |
| 3-5 Years | 21.934642494063223 |
| 5-8 Years | 20.814831984071485 |
| 8-10 Years | 27.722446665005332 |
| More than 10 Years | 26.33157752408725 |

Since Kinan is a PhD in computer science, they definitely cannot have programmed for less than 5 years. Also, given how small the average ages are for programming experiences of 0-3, 3-5, and 5-8 years, it is highly unlikely that Kinan falls under any of these categories. This leaves the chance that Kinan has either programmed for 8-10 years or more than 10 years, but it is hard to tell which category he falls under without getting more of an idea about the count of this data, since each data point has a huge impact for small counts.

Even with this deduction, there is a decent chance that I am wrong. Without the counts, it is hard to tell the impact of Kinan being a part of the grouping to the average of the rest of the observations. Plus, we are making some assumptions to reach our conclusion. Maybe Kinan made it here without writing a single line of code until very recently...

## Question 9
_"Reuse your composition attack from question 8 to compute the exact non-noised counts per programming experience level. Deduce Kinan's programming experience level, with high confidence, by looking at both the exposed counts and the previously exposed averages. Now summarize everything you've learned about Kinan!"_

Let's round the counts, and we get the following potential actual values for each age group:

| programming | AVG(age) | COUNT |
| -------- | ------- | ------- |
| 0-3 Years | 23.03124029692182 | 3 |
| 3-5 Years | 21.934642494063223 | 8 |
| 5-8 Years | 20.814831984071485 | 4 |
| 8-10 Years | 27.722446665005332 | 1 |
| More than 10 Years | 26.33157752408725 | 2 |

Since Kinan is a faculty in the department, we can assume that they have to have programmed for at least five years. Then, with the counts we have, we can deduce the answer with high confidence:
- For Kinan (age 30) to have programmed for 5-8 years, the other people in this category would have to be, on average, less than 18 years old. Given our datapoints, this is not something that could really end up happening.
- If there is one individual who has programmed for 8-10 years, it cannot be Kinan, since they are not close to being 27 or 28.
This leaves the last (and most reasonable) category. So, we can say with high confidence that Kinan has programmed for **More than 10 years**!

To summarize, here is everything we have learned about Kinan through this assignment:
- **Kinan's favorite genre of music is metal**
- **Kinan is 30 years old**
- **Kinan has programmed for more than 10 years**
- **Kinan's favorite color is black**
- **Kinan's favorite sport is soccer**

## Question 10
_"Does the class you implemented suffice to truly enforce that a dataset is never used beyond a certain privacy budget? Can developers intentionally or unintentionally over-use the dataset beyond the privacy budget? At a very high level, how would you design a different privacy budget enforcment mechanism that does not suffer these drawbacks?"_

Hello
