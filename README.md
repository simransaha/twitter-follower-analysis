# twitter-follower-analysis

## data_scraping.ipynb :
Contains the code used to retrieve information from Twitter accounts and save them in a sqlite database.

## creating_df.ipynb :
To create pandas dataframe containing cleaned data (required attributes) and export it as a prelimenary csv file which has also been uploaded in this repository(my_friends.csv).

## model_v1.ipynb :
Contains the classification model: including pre-processing, sampling and comparison between models.

## testModel.py :
Naive code to test performance of model against a random selection of accounts. Text files output2.txt and output3.txt contains the list of accounts followed using each method at the time of testing over a period of 1 day. More details in testModel.py

## Complete method and literature regarding how the retrieving of Twitter Follower data was done to be uploaded soon

## Regarding the use of NLP to improve the model :
NLP was NOT incorporated due to the following reasons:
1) Model is already using optimum importance features. 
2) Adding NLP will significantly increase the complexity and not improve performance.
