## Random user account generator

Create a list of random user accounts with the following fields:
- UUID
- Name
- Email
- Password
- Country
- Locale
- Signup time (epoch)

#### Configuration
All configuration changes are made in `config.py`, the following options are available:
- `users_to_generate` - The number of users to generate, must be a positive number, no limit.
- `output_filepath` - The file path to save the output to, must be a `.csv` file.
- `first_names_filepath` - The file path to the first names list, must be a `.txt` file.
- `last_names_filepath` - The file path to the last names list, must be a `.txt` file.
- `email_domains_filepath` - The file path to the email domains list, must be a `.txt` file.
- `countries_and_locales_filepath` - The file path to the countries and locales list, must be a `.csv` file (may change in the future).
- `sql_export_table_name` - The table name to use when exporting to SQL, must be a string.
- `sql_export_filepath` - The file path to save the SQL export to, must be a `.sql` file.
- `sql_export` - Whether to export to SQL or not, must be a boolean. Default: `True`
- `csv_export` - Whether to export to CSV or not, must be a boolean. Default: `True`
- `verbose_processing` - Whether to print processing information or not, must be a boolean. Default: `False`

#### Output
The output will be saved to `output/users.csv`, this can be updated using the `output_filepath` variable in `config.py`.

#### Performance
- 1000 users - 0.0239s
- 10000 users - 0.2055s
- 1000000 users - 21.6710s

#### Notes
Only locale and country are linked, the rest of the data is random - for example, you may see a .co.uk email domain with a locale of es_MX, but will see accounts with es_MX having Mexico as the country. Passwords generated should NOT be used, these are just hashes of the users name for testing purposes and are not secure.