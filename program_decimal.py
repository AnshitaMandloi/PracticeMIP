from decimal import Decimal
''' Why use Decimal? 
Socho ek bank mein 10 lakh transactions hain. Har ek mein bahut chhota error hai. Total mein paise match nahi honge, aur bank mein ek paisa bhi missing hona bada issue hai.Because in computer it is never stored as 0.1 +0.2= 0.3 rather than that it is stored as 0.3000000004.'''

price=Decimal("100.50")
quantity=3
print(price*quantity)
'''
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\anshi\Python crash course> python program_decimal.py
301.50
'''

