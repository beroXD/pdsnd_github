## 19th Nov'20

# PDSND-P2-Explore-US-Bikeshare-Data
Udacity Programming for Data Science Nanodegree Program - Project II

## Overview
In this project, Python is used to explore data related to bike share systems for three major cities in the United States —Chicago, New York City, and Washington.

## What Software Do I Need?
To complete this project, the following software requirements apply:

* Python 3, NumPy, and pandas installed using Anaconda.
* A text editor, like Sublime or Atom.
* A terminal application (Terminal on Mac and Linux or Cygwin on Windows).

## **Installation links for softwares:**
* [Git for windows - for terminal application using Git Bash](https://gitforwindows.org/)
* [Python using Anaconda (latest version for windows)](https://www.anaconda.com/distribution/)
* [Atom Code Editor (for windows)](https://atom.io/)

## **Code explained in Detail:**
### **How the program works:**
The code developed takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions will change! There are four questions that will change the answers:

* Would you like to see data for _Chicago_, _New York_, or _Washington_?
* Would you like to filter the data by month, day, or not at all?
* (If they chose month) Which month - _January_, _February_, _March_, _April_, _May_, or _June_?
* (If they chose day) Which day - _Monday_, _Tuesday_, _Wednesday_, _Thursday_, _Friday_, _Saturday_, or _Sunday_?

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

## The Datasets:
The data is provided by Motivate, a bike share system provider for many major cities in the United States, to uncover bike share usage patterns. You will compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

* Start Time (e.g., 2017-01-01 00:07:57)
* End Time (e.g., 2017-01-01 00:20:53)
* Trip Duration (in seconds - e.g., 776)
* Start Station (e.g., Broadway & Barry Ave)
* End Station (e.g., Sedgwick St & North Ave)
* User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

* Gender
* Birth Year

## Statistics Computed:
Using python is was able to compute a variety of descriptive statistics.

### 1 Popular times of travel (i.e., occurs most often in the start time)

* most common month
* most common day of week
* most common hour of day

### 2 Popular stations and trip

* most common start station
* most common end station
* most common trip from start to end (i.e., most frequent combination of start station and end station)

### 3 Trip duration

* total travel time
* average travel time

### 4 User info

* counts of each user type
* counts of each gender (only available for NYC and Chicago)
* earliest, most recent, most common year of birth (only available for NYC and Chicago)

## **Credits:**
* Richard Kalehoff (Udacity mentor)
    - [https://github.com/richardkalehoff](https://github.com/richardkalehoff)
    - [https://twitter.com/richardkalehoff](https://twitter.com/richardkalehoff)

* Juno Lee (Udacity Mentor)
    - [https://github.com/junolee](https://github.com/junolee)
    - [https://www.linkedin.com/in/junoleelj](https://www.linkedin.com/in/junoleelj)
    
* The data for all 3 cities that is used in this project can be accessed through the link mentioned below :
    - [City Data](https://zips.udacity-data.com/ee7d089a-4a92-4e5d-96d2-bb256fae28e9/565645/1544291225726/Explore+US+Bikeshare+Data+Subtitles.zip)

* The link for commit message style reference for this project is given below :
    - [Udacity Git Commit Message Style Guide](https://udacity.github.io/git-styleguide/)