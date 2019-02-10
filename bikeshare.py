import time
import pandas as pd
import numpy as np
import datetime
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    city = ''
    while city.lower() not in ['chicago','new york city','washington']:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or'
                     ' Washington?\n')
        if city.lower() == 'chicago':
            return 'chicago'
        elif city.lower() == 'new york city':
            return 'new_york_city'
        elif city.lower() == 'washington':
            return 'washington'


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
    cities = ['chicago','new york city','washington']
    months = ['All','January','Feburary','March','April','May','June']
    days_of_week = ['All','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    while True:
        city = input('Input city \n')
        if city in cities:
            print('\n')
            break


    while True:
        month = input('Input month \n')
        if month in months:
            print('\n')
            break


    while True:
        day = input('input the day of week \n')
        if day in days_of_week:
            print('\n')
            break


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

    if city.lower() == "new york":
        city = "new_york_city.csv"
    else:
        city = city.lower() + ".csv"

    df = pd.read_csv(city)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month

    df['Month'] = df['Start Time'].dt.month
    result_month = df['Month'].mode()[0]



    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day
    result_day = df['day_of_week'].mode()[0]


    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    result_hour = df['hour'].mode()[0]


    print('Display the most common month : ', calendar.month_name[result_month])
    print('----------------------------------------------')
    print('Most common day: ', result_day)
    print('----------------------------------------------')
    print('Most popular hour: ', result_hour)
    print('----------------------------------------------')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('#################################################')


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df['start'] = df['Start Station']

    # TO DO: display most commonly used start station
    result_Start = df['start'].mode()[0]
    print ('The most common start station is: ', result_Start)
    print('----------------------------------------------')
    # TO DO: display most commonly used end station
    df['end'] = df['End Station']
    result_end = df['end'].mode()[0]
    print('Display most commonly used end station: ', result_end)
    print('----------------------------------------------')


    # TO DO: display most frequent combination of start station and end station trip
    common_trip = df['start'] + ' to ' + df['end']
    print('Display most frequent combination of start station and end station trip ', common_trip.mode()[0])
    print('----------------------------------------------')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('#################################################')




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    trip_start = pd.to_datetime(df['Start Time'])
    trip_end = pd.to_datetime(df['End Time'])
    df['Total'] = trip_start - trip_end

    # TO DO: display total travel time
    total_time =  df['Total'].sum()
    print("Display total travel time: " + str(total_time))
    print('----------------------------------------------')


    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Display mean travel time: " + str(mean_time))
    print('----------------------------------------------')




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('#################################################')



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_type = df['User Type'].value_counts()
    print('Display counts of user types: ', user_type)
    print('----------------------------------------------')


    # TO DO: Display counts of gender

    gender_number = df['Gender'].value_counts()
    print('Display counts of gender: ', gender_number)
    print('----------------------------------------------')


    # TO DO: Display earliest, most recent, and most common year of birth

    earliest = df.sort_values('Birth Year').iloc[0]
    recent = df.sort_values('Birth Year').iloc[-1]
    common_year = df['Birth Year'].mode()[0]

    print('Display earliest, most recent, and most common year of birth :', earliest['Birth Year'],recent['Birth Year'], common_year)



    print("\nThis took %s seconds." % (time.time() - start_time))

    print('#################################################')


def display_data(df):

    row_length = df.shape[0]


    for i in range(0, row_length, 5):

        yes = input('\nWould you like to examine the particular user trip data? Type \'yes\' or \'no\'\n> ')
        if yes.lower() != 'yes':
            break


        # split each json row data
        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
        for row in row_data:
            # pretty print each user data
            parsed_row = json.loads(row)
            json_row = json.dumps(parsed_row, indent=2)
            print(json_row)

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
