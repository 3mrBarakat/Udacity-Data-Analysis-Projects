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
        city=input("Enter the name of the city you want to analyze (chicago, new york city, washington): ").lower()
        if city!="chicago" and city!="new york city" and city!="washington":
            print("You enter wrong city please try again")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Enter the month want to analyze (all, january, february, ... , june): ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Enter the day of week want to analyze (all, monday, tuesday, ... sunday): ")

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is:{}".format(df['Start Time'].dt.month.mode()[0]))

    # TO DO: display the most common day of week
    print("The most common day is:{}".format(df['Start Time'].dt.weekday_name.mode()[0]))

    # TO DO: display the most common start hour
    print("The most common start hour is:{}".format(df['Start Time'].dt.hour.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is:{}".format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print("The most commonly used end station is:{}".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip".format(df.groupby(['Start Station','End Station']).size().nlargest(1)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is {} seconds".format(df["Trip Duration"].sum()))

    # TO DO: display mean travel time
    print("The mean travel time is {} seconds".format(df["Trip Duration"].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types are:{}".format(user_types))


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print("The count of genders are:{}".format(gender))
    else:
        print("No data available about the gender")
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earlist=df["Birth Year"].min()
        recent=df["Birth Year"].max()
        common=df["Birth Year"].mode()[0]
        print("The earlist year of birth is {}".format(earlist))
        print("The most recent year of birth is {}".format(recent))
        print("The most common year of birth is {}".format(common))
    else:
        print("No data available about the Birth Year")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    print(df.head())
    while True:
        showData=input("Do you want to show the next 100 record ( if you want enter y): ").lower()
        if showData == "y":
            print(df.iloc[:100])
        else:
            break
       
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
