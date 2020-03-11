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
        city = input('Plaease input chicago, new york city or washington:').lower()
        if city in CITY_DATA:
            break
        else:
            print('Sorry, we don\'t have the bikeshare data of this city.')

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january','february','march','april','may','june']
    while True:
        month = input('Please input the month that you want to explore:').lower()
        if month in months:
            break
        else:
            print('Sorry, we don\'t have the bikeshare data of this month.')
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        day = input('Please input the day that you want to explore:').lower()
        if day in days:
            break
        else:
            print('Sorry, we don\'t have the bikeshare data of this day.')
    

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
    
    df['day'] = df['Start Time'].dt.weekday_name.str.lower()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The Most common month: ',df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('The Most common day: ',df['day'].mode()[0])


    # TO DO: display the most common start hour
    print('The Most common hour: ',df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station: ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most commonly used end station: ',df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    df['Station Trip'] = df['Start Station']+' ot '+df['End Station']
    print('The most frequent combination of start station and end station trip:\n',df['Station Trip'].mode()[0])
              

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    df['Travel time'] = df['End Time'] - df['Start Time']
    
    # TO DO: display total travel time
    print('The total travel time: ',df['Travel time'].sum())

    # TO DO: display mean travel time
    print('The mean travel time: ',df['Travel time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of user types:\n',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('The counts of gender:\n',df['Gender'].value_counts())
    except Exception as e:
        print(e)

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        #print('The counts of gender: ',df['Birth Year'].value_counts())
        print('The earliest year of birth: ',df['Birth Year'].min())
        print('The most recent year of birth: ',df['Birth Year'].max())
        print('The most common year of birth: ',df['Birth Year'].mode()[0])
    except Exception as e:
        print(e)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
