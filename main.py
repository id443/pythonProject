from datetime import date
from pyxirr import xirr

# dates = [date(2020, 1, 1), date(2021, 1, 1), date(2022, 1, 1)]
# dates = [date(2020, 1, 1), date(2021, 1, 1), date(2022, 1, 1)]
# amounts = [-1000, 1000, 1000]
amounts = [-4548, 1762.9, 13381.45, 440.73, 220.37, 110.18, 55]
dates = [date(2022,4,1), date(2022,4,2), date(2022,5,2), date(2022,6,2), date(2022,7,2), date(2022,8,2), date(2022,9,2)]
# amounts = [-1000, 1000, 1000]
# feed/ columnar data
xirr(dates, amounts)
# feed tuples
xirr(zip(dates, amounts))
# feed DataFrame
import pandas as pd

xirr(pd.DataFrame({"dates": dates, "amounts": amounts}))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(xirr(pd.DataFrame({"dates": dates, "amounts": amounts})))

