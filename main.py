from user import *
from generators import *
from file_management import *
import config
import time

users = []

# Generate user data
def generate_user_data():
    user_names = generate_random_name(config.users_to_generate)
    user_emails = generate_email_address(user_names)
    user_countries, user_locales = random_country_and_locale(config.users_to_generate)

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

# Export data
if config.csv_export: save_as_csv(users)
if config.sql_export: save_as_sql(users)

end = time.time()

print(f"Generated {'{:,}'.format(config.users_to_generate)} users in {(end - start):0.4f} seconds.")