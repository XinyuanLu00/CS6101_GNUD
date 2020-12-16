# This is a tutorial of GNUD (ACL 2020 paper “Graph Neural News Recommendation with Unsupervised Preference Disentanglement”)
## Dataset:
There are totally five data files. ``news_user.json`` is all the user clicking data for each news. For example, news 1 includes user 1,2,3,4.
``user_news.json`` is the browsing news data for each user. For example, user 1 browse news 2,3,4.

## How to run the experiment:

# Adding New MIND Dataset
Data Desciption:https://github.com/msnews/msnews.github.io/blob/master/assets/doc/introduction.md 

MIND-Small Download: https://msnews.github.io/

# Update in GNUD
We add a new K regularization in ``model.py``.
We also try to extract the user_news and news_user data from MIND dataset. Please see ``handleBehavior``.py
