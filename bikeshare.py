import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Bikeshare Python Project')
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'washington', 'new york']
    city = input('What city would you like to analyze? (Chicago, New York, Washington) ').lower().strip()
    while True:
        if city not in cities:
            city = input('That is not a valid input please enter Chicago, New York or Washington: ').lower().strip()
        else:
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Which month would you like to analyze? (All, January, February, March, April, May or June) ').lower().strip()
    while True:
        if month not in months:
            month = input('That is not a valid month input please enter All, January, February, March, April, May or June: ').lower().strip()
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day = input('Which day would you like to analyze? (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday) ').lower().strip()
    while True:
        if day not in days:
            day = input('That is not a valid day input please enter All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday: ').lower().strip()
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    if month == 'all':
        df['month'] = df['Start Time'].dt.month
        popular_month = df['month'].mode()[0]
        print('Most Common Month:', popular_month)

    # TO DO: display the most common day of week
    if day == 'all':
        df['weekday'] = df['Start Time'].dt.day_name()
        popular_weekday = df['weekday'].mode()[0]
        print('Most Common Day of Week:', popular_weekday)
        
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Common End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # combining Start Staion and End Staion columns
    df['Stations'] = df['Start Station'] + ' and ' + df['End Station']
    popular_stations = df['Stations'].mode()[0]
    print('Most Frequent Combination of Start and End Station Trips Are:', popular_stations)
    df.pop('Stations')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def sec_to_days(total_seconds):
    """Converts seconds to days, hours, minutes and seconds."""
    
    days = total_seconds/(24*60*60)
    hours = (days-int(days))*24
    minutes = (hours-int(hours))*60
    seconds = (minutes-int(minutes))*60
    
    return days, hours, minutes, seconds
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    days, hours, minutes, seconds = sec_to_days(total_travel_time)
    print('Total Travel Time is: {}days {}h {}m {}s'.format(int(days), int(hours), int(minutes), int(seconds)))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    days, hours, minutes, seconds = sec_to_days(mean_travel_time)
    print('Average Travel Time is: {}days {}h {}m {}s'.format(int(days), int(hours), int(minutes), int(seconds)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('User Types Count:')
    print(user_type_count)

    # TO DO: Display counts of gender
    if city != 'washington':
        gender_count = df['Gender'].value_counts()
        print('\nGender Count:')
        print(gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        youngest_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('\nEarliest Year:\n{}\n\nMost Recent Year:\n{}\n\nMost Common Year of Birth:\n{}'.format(earliest_year, youngest_year, common_year))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def individual_trip_data(df):
    """ 
    Asks user whether they would like to see individual trip data.
    
    Displays each individual trip data of data frame 5 rows at a time.
    """
    count1 = 0
    count2 = 5
    while True:
        quest = input('Would You Like To See Individual Trip Data? enter \'yes\' or \'no\': ')
        if quest.lower().strip() == 'yes':
            for x in range(count1, count2):
                print(df.iloc[x], '\n')
            count1 += 5
            count2 += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        individual_trip_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower().strip() != 'yes':
            print('Ending Program...')
            break
        else:
            print('Restarting Program...\n')
                                       
                 
if __name__ == "__main__":
	main()
