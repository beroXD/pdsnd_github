import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWould you like to see data for New York City, Chicago or Washington?\n')
        city = city.lower()
        if city not in ('new york city', 'chicago', 'washington'):
            print('Sorry, invalid input. Try again.')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month would you like to filter by? January, February, March, April, May, June or enter \'all\' to show data for all months\n')
        month = month.lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('Sorry, invalid input. Try again.')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day would you like to filter by? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or enter \'all\' to show data for all days.\n')
        day = day.lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print('Sorry, invalid input. Try again.')
            continue
        else:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # TO DO: load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # TO DO: convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # TO DO: filter by month if applicable
    if month != 'all':
        # TO DO: use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # TO DO: filter by month to create the new dataframe
        df = df[df['month'] == month]

    # TO DO: filter by day of week if applicable
    if day != 'all':
        # TO DO: filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The Most Common Month is: ', common_month, '\n')

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The Most Common Day is: ', common_day, '\n')

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('The Most Common Start Hour is: ', common_start_hour, '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax() # idxmax() - Return index of first occurrence of maximum over requested axis.
    print('The Most Commonly Used Start Station is: ', start_station, '\n')

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('The Most Commonly Used End Station is: ', end_station, '\n')

    # TO DO: display most frequent combination of start station and end station trip
    # A groupby operation involves some combination of splitting the object, applying a function,
    # and combining the results. This can be used to group large amounts of data and compute operations on these groups.
    combination = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).head(1)
    print('\nThe Most Commonly Used Combination of Start and End Station trip is:\n',  combination, '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The Total travel time is: ', total_time, '\n')

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The Mean travel time is: ', mean_time, '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nUser Types:\n', user_types)

    # TO DO: Display counts of gender
    try:
        gender_types = df['Gender'].value_counts()
        print('\nGender Types:\n', gender_types)
    except KeyError: # KeyError exception is what is raised when you try to access a key that isn’t in a dictionary (dict).
        print('\nNo data, gender is unknown.\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    #Earliest year of birth
    try:
        earliest_year = df['Birth Year'].min().astype(int)
        print('\nEarliest Year of Birth is: ', earliest_year, '\n')
    except KeyError:
        print('\nNo data, year is unknown.\n')

    #Recent year of birth
    try:
        recent_year = df['Birth Year'].max().astype(int)
        print('\nMost Recent Year of Birth is: ', recent_year, '\n')
    except KeyError:
        print('\nNo data, year is unknown.\n')

    #Common year of birth
    try:
        common_year = df['Birth Year'].value_counts().idxmax().astype(int) # idxmax() - Return index of first occurrence of maximum over requested axis.
        print('\nMost Common Year of Birth is: ', common_year, '\n')
    except KeyError:
        print('\nNo data, year is unknown.\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # TO DO: Display 5 lines of raw data
def display_data(df):
    raw_data = input('\nWould you like to see the raw data? Enter yes or no.\n')
    i=5
    while raw_data.lower() == 'yes':
        print(df.iloc[:i])
        raw_data = input('\nWould you like to see five more rows of data? Enter yes or no.\n')
        i *= 2

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
