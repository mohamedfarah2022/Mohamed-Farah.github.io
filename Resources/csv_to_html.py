import pandas as pd

cities_data_to_load = "Resources/cities.csv"

cities_data = pd.read_csv(cities_data_to_load)

cities_df = pd.DataFrame(cities_data)

cities_html = cities_df.to_html(index=False)

file = open('Resources/csv_to_html.txt', 'w')
file.write(cities_html)
file.close