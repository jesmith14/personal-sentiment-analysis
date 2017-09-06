# personal-sentiment-analysis
Data Science project that implements sentiment analysis on your personal facebook account. By cross-examining the public timeline posts vs. the private messages, I created visualizations to discover if my private sentiment is different than my public sentiment. Then, I used a machine learning algorithm to predict what my future sentiment might be.

## Motivation:
Far too many people share their lives and personal information with Facebook as if it was a private journal instead of a corporation. A majority of people who use Facebook don't know even remotely how much data is being collected on us every single day. This projecct serves two main purposes:
1) To raise awareness for how much data is being collected on us through our social media usage.
2) To show the public that we can take control of our own data. If companies who don't even personally know us can use our data to benefit their platforms, why can't we use it to learn about ourselves?

For privacy, I have not uploaded my own messages and timeline html files. But, if you'd like to use this repo to assess your own public vs private sentiment - here's how!

### Step 1:
Clone this repo, or download the files and put them into a jupyter notebook.

### Step 2:
Download a copy of your Facebook data (this can be done through your Facebook settings)

### Step 3:
Take the timeline.htm and messages.htm files (make sure they are named exactly this too!) And run the functions in Data Collection and Cleaning to get Pandas Data Frames of your messages / posts. This is important because you can't create the visualizations unless the data has been cleaned.

### Step 4:
To get the visualizations, run the functions in the Data Exploration file. This will show you your timeline vs your messages sentiment analysis yearly, monthly, and daily.

### Step 5:
To run the machine learning algorithms on your data, run the functions in the Machine Learning file. 

This is just the beginnings of this project. Eventually, I'd like to make it more transparent and portable by creating a python package for FB sentiment analysis. If you have any questions or would like to reach out to me about my project, feel free to email me at jsmit167@calpoly.edu.
