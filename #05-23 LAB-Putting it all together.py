#Define a simple function used as a parameter to the sort function to sort the list.
def get_event_date(event):
  return event.date

# Define the processing function: 
# The Dictionary Process:
# Inside the function, events are sorted by using the sort method, passing the function created as the key
def current_users(events):
  events.sort(key=get_event_date)
  # Before iterating through our list of events, a dictionary is needed to store the names and users of a machine.
  machines = {}
  # Creating the iteration process, to iterate through a list of events. 
  for event in events:
    # Check if the machine affected by this event is in the dictionary.  If it's not, it will be added with an empty set as the value.
    if event.machine not in machines:
      machines[event.machine] = set()
    # The add and remove methods are used to add and remove, respectively, elements from a set.
    # For login events, users are added to the list; for logout events, users are removed from the list.
    if event.type == "login":
      machines[event.machine].add(event.user)
    # elif statement to allow users who are not listed as logging on to be removed.
    elif event.type == "logout" and event.user in machines[event.machine]:
        machines[event.machine].remove(event.user)
  return machines
# Once iteration through the list of events is complete, the dictionary will contain all the machines to be referenced as 'keys', with a set containing the current users of the machines as the 'values'.
# This function and this part of the processing handles the dictionary.

# The Printing Process: Generating a report
# In the report, use the items method to iterate over and return the pairs of  keys and values in the dictionary.
def generate_report(machines):
  for machine, users in machines.items():
    # "Now, before we print anything, we want to ensure that we don't print any machines where nobody is currently logged in. This could happen if a user logged in and then logged out. To avoid that, we tell the computer only to print when the set of users has more than zero elements."
    if len(users) > 0:
      # "Now, we said earlier that we want to print the machine name, followed by the users logged into the machine, separated by commas. Let's generate the string of logged in users for that machine using the method join."
      user_list = ", ".join(users)
      # "Now, we can generate the string we want using the format method"
      print("{}: {}".format(machine, user_list))

# "No output should be generated from running the custom function definitions above.  To check that our code is doing everything it's supposed to do, we need an `Event` class.  The code in the next cell below initializes our `Event` class.  Go ahead and run this cell next."
class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)
