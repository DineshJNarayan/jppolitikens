# %%
import sys
import numpy as np
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import scipy as scpy
import sklearn as skl

print('Python: {}'.format(sys.version))
print('numpy: {}'.format(np.__version__))
print('pandas: {}'.format(pd.__version__))
print('scipy: {}'.format(scpy.__version__))
print('sklearn: {}'.format(skl.__version__))


cnx = mysql.connector.connect(user='root', password='Vmcp2020Gain', host='127.0.0.1', database='JPPolitikens')
cursor = cnx.cursor()

with open('query.sql', 'r') as f:
    query = f.read()
cursor.execute(query)

records = cursor.fetchall()
df = pd.DataFrame(records)
df.columns = [  "property_id", "views_date", "month_format", "views_property",
                "views_total_views", "users_total_users", "views_full_opt_in_frac", 
                "users_full_opt_in", "users_full_opt_in_frac", "views_legitimate_int_only_frac",
                "users_legit_int_only", "users_legitimate_int_only_frac", "views_reject_only_frac", 
                "users_reject_only_frac", "views_previously_opt_in_frac", "users_previously_opt_in_frac"    ]

cursor.close()
cnx.close()

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

# Initialise the subplot function using number of rows and columns
figure, axis = plt.subplots(3, 1)
axis[0].plot(df.views_date, df.users_total_users, label="Total users")
axis[0].plot(df.views_date, df.views_total_views, label="Total views")
axis[0].set_title("Total Users vs. Total Views")

axis[1].plot(df.views_date, df.users_full_opt_in_frac, label="Fraction users")
axis[1].plot(df.views_date, df.views_full_opt_in_frac, label="Fraction views")
axis[1].set_title("Fraction Users vs. Fraction Views")

axis[2].plot(df.views_date, df.users_legitimate_int_only_frac, label="Fraction users - legit interest")
axis[2].plot(df.views_date, df.views_legitimate_int_only_frac, label="Fraction views - legit interest")
axis[2].set_title("Fraction Users vs. Fraction Views (Legit Interest only)")
plt.show()
