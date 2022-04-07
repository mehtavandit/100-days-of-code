<h1 align="center">
    100 Days of Code: Day 47
  <br>
</h1>

## Objective
- This project's purpose is to create an automatic Amazon price tracker for a product that a user wishes to purchase. 

## main.py
- The requests module is used to import the content of the user's wish product page, which is then scraped using the Beautifulsoup library. 
- The product's price is retrieved, and if it is less than the pre-determined price, then the user is notified about the price reduction via email by using the SMTP. 
