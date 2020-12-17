# A tutorial of GNUD 
(ACL 2020 paper “Graph Neural News Recommendation with Unsupervised Preference Disentanglement”)

This is a tutorial guide for running the source code of GNUD. 

What we do for this project:
1. We add descriptions of the dataset structure.
2. We add guide on how to run the experiment, including the environment and the command line each step.
3. We add the comments of the functions in all the ``.py``files.
4. We update a new K regularizer different from the original paper. 
5. We add a test experiment code. 
6. We try to add new MIND dataset to apply to this personalised news recommendations. We try to extract the ``user_news`` and ``news_user`` features in order to consistent with the original data. However, the authors only give the processed data. As a result, we could not figure out how they extract from the raw data.

## Dataset:
There are totally 5 data files. 

1. ``train_news_user.json``  and ``test_news_user.json``: traning and test data for all the news and users. Dictionary. key is the ``newsID``, value is all the userID. For example, news 1 includes user 1,2,3,4.
2. ``train_user_news.txt`` and ``test_user_news.txt`` :training and test data for the clicking news data for each user. For example, user 1 clicks news 2,3,4.
3. ``news_entity``: A 40-dimension vector with 0 padding.
4. ``topic_news.txt``: Total topics for all the news. 
5. ``data.npz``: raw data. The size is too large. You could find it at the following link: 


## Experiment Environment
Python 3 and TensorFlow v1.14.

Note: Do not use the TensorFlow which is higher than v2.0. 
Due to the CUDA version, we run it on CPU and the time expenses is about 7mins each time.

If want to have experiment on GPU: Please make sure the CUDA version is higher than v1.14.


## Update the K regularizer
In the original paper, the authors use the regularizer. In our new project, we add a new K regularizer. The formula is calculated as follows. The update version of new regularizer can be found in ``model.py``.





## Adding New MIND Dataset
Data Desciption:https://github.com/msnews/msnews.github.io/blob/master/assets/doc/introduction.md 

MIND-Small Download: https://msnews.github.io/
