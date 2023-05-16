# Homework 2

You are working as a software developer at a currency exchange company call AUPP Currency EX.

Your manager assigned you to create an application that can handle transactions below:

1. Exchange from USD to RIEL, USD rate=4000៛.
2. Exchange from YUAN to RIEL, YUAN rate=643៛.
3. Exchange from BATH to RIEL, BATH rate=123៛.

Technical requirement:

The application development team required you to create a function call currency*conversion that take **2 parameters**, \_currency* and _amount_.

Make sure that currency_conversion function return the following value in different situation:

when invalid currency provide, make sure the function return `‘not found’`
if the amount is number type, make sure the function return `‘invalid amount’` 3. if both parameters are correct, return convert value from the function example: `currency_conversion('USD', 2)` # function should return 8000
