## 0x16. API advanced

[Image Link](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/314/WIxXad8.png)

### Tasks

#### 0. How many subs?

Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

**Requirements:**
- Prototype: `def number_of_subscribers(subreddit)`
- If not a valid subreddit, return 0.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

#### 1. Top Ten

Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

**Requirements:**
- Prototype: `def top_ten(subreddit)`
- If not a valid subreddit, print None.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

#### 3. Count it!

Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).

**Requirements:**
- Prototype: `def count_words(subreddit, word_list)`
- Note: You may change the prototype, but it must be able to be called with just a subreddit supplied and a list of keywords. AKA you can add a counter or anything else, but the function must work without supplying a starting value in the main.
- If word_list contains the same word (case-insensitive), the final count should be the sum of each duplicate (example below with java)
- Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically (ascending, from A to Z). Words with no matches should be skipped and not printed. Words must be printed in lowercase.
- Results are based on the number of times a keyword appears, not titles it appears in. java java java counts as 3 separate occurrences of java.
- To make life easier, java. or java! or java_ should not count as java
- If no posts match or the subreddit is invalid, print nothing.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are NOT following redirects.

