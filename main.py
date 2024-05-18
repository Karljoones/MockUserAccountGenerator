from user import *
from generators import *
from utils.file_management import *
from utils.decorators import time_measurement_decorator
import config
import time

users = []

# Generate user data
@time_measurement_decorator
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

        if config.verbose_processing: print(user)

        users.append(user)

def main():
    start = time.time()

    print(f"Generating {'{:,}'.format(config.users_to_generate)} users...\n")

    generate_user_data()

    # Export data
    if config.csv_export or config.sql_export: create_output_folder()
    if config.csv_export: save_as_csv(users)
    if config.sql_export: save_as_sql(users)

    end = time.time()

    if config.verbose_debugging: print(f"\nSuccess! Generated {'{:,}'.format(config.users_to_generate)} users in {(end - start):0.4f} seconds.\n")
    if config.csv_export: print(f"Data exported to /{config.export_directory}/{config.csv_export_filename}")
    if config.sql_export: print(f"Data exported to /{config.export_directory}/{config.sql_export_filename}")

if __name__ == "__main__":
    main()