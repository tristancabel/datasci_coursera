## problem description
I choose "San Francisco crime classification" where the problem is to predict crimes category which are going to occur.
The Data given is a record of past crime. We are given a date, a crime category, a location (both coordinates and address), a description of the crime and the state of the crime(solved or not).

##analysis approach
I used a K-nearest neighboor approach to solve this problem. Given a date and location, predict the crime category most likely to occur.

I first started by looking at the data plotting crimes category against location. Then, I choose to use a K-nearest neighboor approach to solve this problem. As stated in Wikipedia, for this algorithm : "An object is classified by a majority vote of its neighbors, with the object being assigned to the class most common among its k nearest neighbors". 
In order to be able to use this algorithm, I needed to clean a bit the data. I first deleted columns that I wouldn't use : 'Descript', 'PdDistrict', 'Resolution', 'Address' . Then I added 2 new columns : 'Hour' and 'weekday' (0:Monday, .. 6: Sounday).

##first approach

I used Python language, using the libraries 'Panda', 'numpy' and 'sklearn'. I ran into some small challenges to clean the data as I was not familiar with these libraries. I also had to change the week day from string to number (Monday become 0) in order to use it in the KNN algorithm . I then needed to tune the KNN parameters a bit (number of neighbours to take into consideration). 

## initial solution analysis
In my first approach I was testing my predictions against the true result of my test dataset. However, in this dataset, there is crimes occuring at the same hour and quite close from each other. There is also some noise produced by crime occuring quite rarely. 

## revised solution approach
In my revised solution approach, I first clean the data a bit, deleting records of type "NON-CRIMINAL" and "SUSPICIOUS OCC" and I changed my comparison algorithm to check predictions against not only the exact record but crime occuring in the given hour and in a distance less than 500m from crime scene. 
