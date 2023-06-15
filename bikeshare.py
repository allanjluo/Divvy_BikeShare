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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please enter a city (Chicago, New York City, Washington): ").lower()
    while city not in CITY_DATA:
        print("Invalid city! Please try again.")
        city = input("Please enter a city (Chicago, New York City, Washington): ").lower()


    # get user input for month (all, january, february, ... , june)
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

    month = input("Please enter a month (All, January, February, March, April, May, June): ").lower()
    while month not in valid_months:
        print("Invalid month! Please try again.")
        month = input("Please enter a month (All, January, February, March, April, May, June): ").lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    day = input("Please enter a day (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ").lower()

    while day not in valid_days:
        print("Invalid day! Please try again.")
        day = input("Please enter a day (All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday): ").lower()

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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = df['month'].mode()[0]
    print('The most common month: ', months[common_month - 1].title())


    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week: ', common_day)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour: ', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station: ", most_common_start_station)


    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station: ", most_common_end_station)


    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    most_frequent_trip = df['Trip'].mode()[0]
    print("Most frequent combination of start station and end station trip: ", most_frequent_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time (in seconds): ", total_travel_time)
    print("Total travel time (in minutes): ", total_travel_time / 60)
    print("Total travel time (in hours): ", total_travel_time / 3600)


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time (in seconds): ", mean_travel_time)
    print("Mean travel time (in minutes): ", mean_travel_time / 60)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of User Types:")
    print(user_types)


    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of Gender:")
        print(gender_counts)
    else:
        print("\nGender information is not available for this city.")


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])

        print("\nEarliest Year of Birth:", earliest_year)
        print("Most Recent Year of Birth:", most_recent_year)
        print("Most Common Year of Birth:", most_common_year)
    else:
        print("\nBirth year information is not available for this city.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Prompts the user to see raw data and displays it in chunks of 5 rows at a time.

    Args:
        df (pandas.DataFrame): The DataFrame containing the raw data.

    Returns:
        None
    """
    response = input("Would you like to see 5 lines of raw data? Enter 'yes' or 'no': ").lower()
    index = 0

    while response == 'yes' and index < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5

        if index >= df.shape[0]:
            print("End of raw data reached.")
            break

        response = input("Would you like to see 5 more lines of raw data? Enter 'yes' or 'no': ").lower()

        while response not in ['yes', 'no']:
            print("Invalid input! Please enter 'yes' or 'no'.")
            response = input("Would you like to see 5 more lines of raw data? Enter 'yes' or 'no': ").lower()

    if response == 'no':
        print("Raw data display ended.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
