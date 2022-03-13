<h1 align="center">
    100 Days of Code: Day 36
  <br>
</h1>

## Objective
- This project's goal is to create a stock trading news alert project.

## main.py
- The Alpha Vantage API is used to get Tesla stock prices..
- The price from yesterday and the price from the day before yesterday are compared, and if the difference is larger than 5%, the latest news about the company that has influenced the share price is provided to the user through sms by using the Twilio API.
- The news that is sent to the user is retrieved using the News API.
- Note:- Simply altering the name of the STOCK NAME variable will provide you with information about your selected stock.
