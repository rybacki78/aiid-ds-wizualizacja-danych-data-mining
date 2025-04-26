import pandas as pd

handel = pd.read_excel("data-sets/handel25.xlsx")

print(handel)

print("_" * 30)

kurs = pd.read_csv("data-sets/kurs4.csv", sep=";", decimal=",")

print(kurs)
kurs.info()

print("_" * 30)

sport = pd.read_csv("data-sets/sport2.csv", sep="#")
print(sport)
sport.info()

print("_" * 30)

wynagrodzenia = pd.read_csv("data-sets/wynagrodzenia22.csv", sep=";", decimal=",")
print(wynagrodzenia)
wynagrodzenia.info()