import random
import time
import csv
import config

# Generate a random name, consisting of a first and last name
def generate_random_name(generation_count = None):
    names_first_file = open(config.first_names_filepath, 'r')
    names_last_file = open(config.last_names_filepath, 'r')
    
    first_names_list = list(map(str.strip, names_first_file.readlines()))
    last_names_list = list(map(str.strip, names_last_file.readlines()))

    # Return a single random name if `count` is not provided
    if generation_count == None:
        return f"{first_names_list[random.randint(0, len(first_names_list) - 1)]} {last_names_list[random.randint(0, len(last_names_list) - 1)]}".title()

    generated_names = []

    for _ in range(generation_count):
        generated_names.append(f"{first_names_list[random.randint(0, len(first_names_list) - 1)]} {last_names_list[random.randint(0, len(last_names_list) - 1)]}".title())
    
    return generated_names

# Generate an email address, based off a name, or list of names
def generate_email_address(names_for_emails):
    domains_list_file = open(config.domains_filepath, 'r')

    domains_list = list(map(str.strip, domains_list_file.readlines()))

    if isinstance(names_for_emails, list):
        generated_email_list = []

        for _ in range(len(names_for_emails)):
            generated_email_list.append(f"{names_for_emails[_].lower().replace(' ', '.')}{random.randint(0, 1000)}@{random.choice(domains_list)}")

        return generated_email_list
    
    return f"{names_for_emails.lower().replace(' ', '.')}{random.randint(0, 1000)}@{random.choice(domains_list)}"

# Generate a random signup time
def random_signup_time():
    return time.time() - random.randint(100, 1000000)

def random_country_and_locale(count = None):
    countries_and_locales_list = list(csv.reader(open(config.countries_and_locales_filepath, 'r')))

    if count == None:
        return random.choice(countries_and_locales_list).strip().split(',')
    
    generated_countries = []
    generated_locales = []

    for _ in range(count):
        country_locale = random.choice(countries_and_locales_list)
        generated_countries.append(country_locale[0].strip())
        generated_locales.append(country_locale[1].strip())

    return generated_countries, generated_locales