import pandas as pd

gdp = {"country": ["United States", "China", "Japan", "Germany", "United Kingdom"],
       "capital": ["Washington, D.C.", "Beijing", "Tokyo", "Berlin", "London"],
       "population": [323, 1389, 127, 83, 66],
       "gdp": [19.42, 11.8, 4.84, 3.42, 2.5],
       "continent": ["North America", "Asia", "Asia", "Europe", "Europe"]}

gdp_df = pd.DataFrame(gdp)

print(gdp_df)

# add index columns
gdp_df = pd.DataFrame(
    gdp,
    columns=['country', 'capital', 'population', 'gdp', 'continent'],
    index=['us', 'cn', 'jp', 'de', 'uk']
)

# gdp_df.index = ["US", "CN", "JP", "DE", "UK"]
# gdp_df.columns = ["Country", "Capital", "Population", "GDP", "Continent"]

print(gdp_df)

# add rank
gdp_df['rank'] = 'GDP'

gdp_df['Area'] = [9.15, 9.38, 0.37, 0.35, 0.24]

print(gdp_df)


# Series

series = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(series)

print(type(gdp_df.Area))

print(gdp_df.gdp > 4)

print(gdp_df[['country', 'gdp']])
