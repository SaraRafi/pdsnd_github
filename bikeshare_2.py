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


    city = input("Select Chicago, New York City or Washington(please type your selection)\n").lower()

    while city not in CITY_DATA.keys():
        city = input("You enetered an invalid input, let try again :)  ")


     # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month are you interested in? \nSelect all or January to May : \n" ).lower()

     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input ("Please enter the day of the week : \n")

    return city, month, day

    print('-'*40)


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
    df = pd.read_csv(CITY_DATA.get(city))

    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    #filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month']== month]

    #filter by day of week if applicable
    if day != 'all':
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week']== day.title()]

    # ## drop rows with missing value_counts
    df.dropna(axis = 0, inplace = True)

    return df

def raw_data_request(df):
    data_request = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while data_request.lower() == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        request = input('Do you wish to see 5 more lines?Enter yes or no.\n' ).lower()
        if request.lower() != 'yes':
            break

print('-'*40)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].value_counts().idxmax()

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()

    print("Popular Month : {}".format(popular_month))
    print("Popular Day of the week : {}".format(popular_day))
    print("Popular Hour : {}".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combination'] = df['Start Station'].str.cat(df['End Station'],sep=" ")
    popular_station_combination = df['Station Combination'].value_counts().idxmax()

    print("Popular Start Station : {}".format(popular_start_station))
    print("Popular End Station : {}".format(popular_end_station))
    print("Popular Start and End Station Combination {}:".format(popular_station_combination) )



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()

    print("Total Travel Time : {}".format(total_travel_time))
    print("Average Travel Time : {}".format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(gender)
    except:
        print("Not Enough Data on Gender of Users")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birthyear = df['Birth Year'].min()
        recent_birthyear = df['Birth Year'].max()
        most_common_birthyear = df['Birth Year'].value_counts().idxmax()

        print("The earliest Birth Year : {}".format(int(earliest_birthyear)))
        print("The most recent Birth Year : {}".format(int(recent_birthyear)))
        print("The most common Birth Year : {}".format(int(most_common_birthyear)))
    except:
        print("Not Enough Data on Birthyear of Users")




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        raw_data_request(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
