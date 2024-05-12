## Random user account generator

Create a list of random user accounts with the following fields:
- UUID
- Name
- Email
- Password
- Country
- Locale
- Signup time (epoch)

#### Usage
Update `USERS_TO_GENERATE` in `main.py` to change the number of users to generate.

#### Output
The output will be saved to `output/users.csv`

#### Performance
1000 users - 0.0239s
10000 users - 0.2055s
1000000 users - 21.6710s

#### Notes
Only locale and country are linked, the rest of the data is random - for example, you may see a .co.uk email domain with a locale of es_MX, but will see accounts with es_MX having Mexico as the country. Passwords generated should NOT be used, these are just hashes of the users name for testing purposes and are not secure.