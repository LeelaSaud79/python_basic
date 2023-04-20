'''import decimal
print(0.1)
print(decimal.Decimal(0.5))
import fractions
print(fractions.Fraction(1.5))
import math
print(math.sin(1))
import datetime
datetime_object=datetime.date.today()
print(datetime_object)
print(dir(datetime))'''
from datetime import date
timestamp=date.fromtimestamp(1234559887)
print(timestamp)

