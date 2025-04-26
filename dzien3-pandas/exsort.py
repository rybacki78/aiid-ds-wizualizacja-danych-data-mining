import pandas as pd

wynagrodzenia = pd.read_csv("data-sets/wynagrodzenia22.csv", sep=";", decimal=",")
print(wynagrodzenia)
wynagrodzenia.info()

wynagrodzenia2 = wynagrodzenia.sort_values(by="2019")
print(wynagrodzenia2)