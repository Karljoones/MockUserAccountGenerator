from user import *
from generators import *
import csv
import time

USERS_TO_GENERATE = 1000000

users = []

# Save the data into output/users.csv
def store_list():
    with open('output/users.csv', mode='w', newline='') as users_file_csv:
        users_writer = csv.writer(users_file_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        users_writer.writerow(['UUID','Name', 'Email', 'Password', 'Locale', 'Country', 'Signup Time'])

        for user in users:
            users_writer.writerow([user.get_uuid(), user.name, user.email, user.get_password(), user.locale, user.country, user.signup_time])

        users_file_csv.close()

# Generate user data
def generate_user_data():
    user_names = generate_random_name(USERS_TO_GENERATE)
    user_emails = generate_email_address(user_names)
    user_countries, user_locales = random_country_and_locale(USERS_TO_GENERATE)

    for i in range(len(user_names)):
        user = User(user_names[i])
        user.email = user_emails[i]
        user.set_password(user.name.lower().replace(' ', ''))
        user.locale = user_locales[i]
        user.country = user_countries[i]
        user.signup_time = random_signup_time()
        user.set_uuid()

        users.append(user)

# Main actions
start = time.time()
generate_user_data()
store_list()
end = time.time()

print(f"Generated {'{:,}'.format(USERS_TO_GENERATE)} users in {(end - start):0.4f} seconds. Data saved to output/users.csv.")