import pandas as pd
import os
print(os.getcwd())

wynag = pd.read_csv("../data-sets/wynagrodzenia22.csv", sep=";", decimal=",")

print(wynag)
wynag.info()

print("-" * 30)

mean_wynag = wynag[["2010", "2019"]].mean()
print(mean_wynag)

print("-" * 30)

median_wynag = wynag[["2010", "2019"]].median()
print(median_wynag)

print("-" * 30)

var_wynag = wynag[["2010", "2019"]].var()
print(var_wynag)

print("-" * 30)

std_wynag = wynag[["2010", "2019"]].std()
print(std_wynag)

print("-" * 30)

q1_wynag = wynag[["2010", "2019"]].quantile(0.25)
q2_wynag = wynag[["2010", "2019"]].quantile(0.75)
print(q1_wynag)
print(mean_wynag)
print(q2_wynag)

# dla wojewodztwa
wynagrodzenia = pd.read_csv("../data-sets/wynagrodzenia22.csv", sep=";", decimal=",", index_col=0).T
lodzkie = wynagrodzenia["ŁÓDZKIE"].mean()

print(lodzkie)

# zawiera wszystko ;)
print(wynagrodzenia.describe())