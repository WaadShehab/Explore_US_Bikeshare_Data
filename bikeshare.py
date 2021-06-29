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
        city =input('\n choose city to filter by?chicago, new york city, washington?\n')
        city=city.lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Sorry, Try again")
            continue
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("\n choose month that you want filter by? january, february, ... , june or all\n ")
        month=month.lower()
        if month not in ('january','february','march','april','may','june','all'):
            print("Sorry, Try again")
            continue
        else:
            break
            
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("\n choose day that you want filter by? satuerday,sunday, monday,tuesday,wednesday,thursday,friday or all \n ")
        day=day.lower()
        if day not in ('sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'):
            print("Sorry, Try again")
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
    df =pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month=df['month'].mode()[0]
    print ("Most common month:",popular_month)
    # TO DO: display the most common day of week
    popular_day=df['day_of_week'].mode()[0]
    print ("Most common day:",popular_day)
                                  

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print ("Most common hour:",popular_hour)    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station=df['Start Station'].mode()[0]
    print("most commonly used start station:",Start_Station)

    # TO DO: display most commonly used end station
    End_Station=df['End Station'].mode()[0]
    print("most commonly used End station:",End_Station)


    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station'].map(str)+'&'+df['End Station']
    combination=df['combination'].value_counts().idxmax()
    print("most commonly used Combination of start and end station trip:",combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    try:
       df['Time Delta']=df['End Time']-df['Start Time']
       total_time=df['Time Delta'].sum()
       print("total travel time :",total_time)
    except Exception as e:
       print("couldn't calculate total travel time")             
    
                              

    # TO DO: display mean travel time
    try:
       total_mean=df['Time Delta'].mean()
       print("the mean travel time :",total_mean)
    except Exception as e:
       print("couldn't calculate the mean travel time")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type'].value_counts()
    print('user types:\n',user_types)
    

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print("Gender:\n",gender)
    else:
        print("There is no gender information in this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print("earliest :\n",earliest)
        recent = df['Birth_Year'].max()
        print("recent :\n",recent)
        common_birth = df['Birth Year'].mode()[0]
        print("common_birth :\n",common_birth)
    else:
        print("There is no birth year information in this city.")

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
