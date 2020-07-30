# In python we have date, time, datetime, timezone and timedelta. Let's explore all these.

# Main module to work with dates in python is datetime module
import datetime
import pytz

# before working with dates and times it is important to understand difference between naive and aware dates
# and times
# naive dates and times don't have information to determine things like timezones or daylight savings times
# to avoid confusion and be aware of that information we use aware dates and times

# Let's first explore about naive dates and times:
# for a normal date we use date() constructor and it works with year, month, day
d = datetime.date(2020, 7, 29)  # here be sure to pass regular integers as days and months with no leading 0
print(d)
# d = datetime.date(2020, 07, 29)
# print(d)  # this will give a syntax error since we added leading 0 to month as 07

# to get today's local date we use date.today() method
tday = datetime.date.today()
print(tday)  # prints current local date

# to get more information about our dates we can used year, month and day attributes
print(tday.year)
print(tday.month)
print(tday.day)

# to get the day of the week we can use weekday() or isoweekday() methods
print(tday.weekday())  # for weekday() monday is 0 to sunday which is 6
print(tday.isoweekday())  # for isoweekday() monday is 1 to sunday which is 7

# Now let's look at timedelta. Timedelta is simply the difference between two dates or times. And they are
# extremely useful when we do operations on our dates and times
# we use timedelta() method by passing the duration of difference between the dates or times as argument
# if we add or subtract a timedelta from a date we get another date
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)  # prints what the date will be after 7 days from now
print(tday - tdelta)  # prints what the date was before 7 days from now

# if we instead add or subtract a date from another date we get timedelta as the result
bday = datetime.date(2020, 9, 30)
till_bday = bday - tday
print(till_bday.days)  # prints number of days until birthday from today
print(till_bday.total_seconds())  # prints total number of seconds until birthday from today

# now let's look at times. In times we work with hours, minutes, seconds and micro seconds.
t = datetime.time(9, 30, 45, 100000)  # here we are specifying new local time in hrs, mins, secs & milli-secs
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

# Generally we would be needing both date and time simultaneously, for thais we use datetime.datetime module
dt = datetime.datetime(2020, 7, 30, 17, 41, 30, 100000)
print(dt)  # prints both date ant time
print(dt.date())  # prints only date
print(dt.time())  # prints only time
print(dt.hour)  # prints hour

# we can also add and subtract timedelta duration
tdelta_1 = datetime.timedelta(days=7)
print(dt + tdelta_1)  # prints the date adding one week

# we can also add hours or minutes or seconds with this datetime.datetime module
tdelta_2 = datetime.timedelta(hours=12)
print(dt + tdelta_2)  # prints the date adding 12 hours

# Let's see some of the alternative constructors that come with datetime
dt_today = datetime.datetime.today()  # .today() returns the current today's local time with timezone equals none
dt_now = datetime.datetime.now()  # .now() gives us the option of passing the timezone. If it is left empty then
# timezone will be equal to none
dt_utcnow = datetime.datetime.utcnow()  # .utcnow gives the current utc time but tzinfo is still set to none

print(dt_today)
print(dt_now)
print(dt_utcnow)

# Now let's look into time zone aware dates and times. This is done using third party package called pytz.
# We can install pytz using pip and type the command in the terminal as -> pip install pytz
dt_tz = datetime.datetime(2020, 7, 30, 18, 18, 45, tzinfo=pytz.UTC)  # by using tzinfo=pytz.UTC we are
# making it timezone aware
print(dt_tz)  # prints date and time with extra 00:00

dt_now_tz = datetime.datetime.now(tz=pytz.UTC)
print(dt_now_tz)  # prints current date and time with timezone aware

dt_utcnow_tz = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow_tz)  # prints current utc date and time with timezone aware

# let's convert it to a different timezone
# to see the list of all timezones available wa can use pytz.all_timezones
for tz in pytz.all_timezones:
    print(tz)

dt_asia = dt_now_tz.astimezone(pytz.timezone('Asia/Calcutta'))
print(dt_asia)

# Making naive datetime timezone aware by running timezone localized function
dt_now_ldn = datetime.datetime.now()
ldn_tz = pytz.timezone('Europe/London')

dt_now_ldn = ldn_tz.localize(dt_now_ldn)
dt_usa = dt_now_ldn.astimezone(pytz.timezone('America/Montreal'))
print(dt_usa)

# Best way to pass these dates and time for internal use is by using isoformat() method
print(dt_now.isoformat())

# To print these dates and times in a specific format we can look at the format codes in the
# python documentation for any type of display format
# for this we use strftime() method and pass in format code
# if we want to display as July 30, 2020 we can use %B %d, %Y format code in strftime() method
print(dt_now.strftime('%B %d, %Y'))  # prints -> July 30, 2020

# to convert a string to datetime we use strptime() method and pass string and what date format that string is in
dt_str = 'July 30, 2020'
d_t = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(d_t)
