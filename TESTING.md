# Program Testing
This file records some of the testing and problems I ran into while developing the program.

## Log in Testing :<br />
I tested different input during login page to ensure that invalid input will not crash the program.
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/Testing/1_login_testing.PNG)
<br /><br />
## Manager Section Testing: <br />
I input teamrocket as username and password to ensure that the program will log me in to the manager section rather than sales assistant section. <br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/Testing/2_log_in_as_manager.PNG)
<br /><br />
## Testing manager input validation: <br />
I tested input various value for the input validation to ensure that invalid input will not go through or crash the program. <br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/Testing/3_manager_input_testing.PNG)
<br />
<br />
## Testing Profit Reporting function and other manager functions: <br />
In this section, I tested the profit reporting function and ran into an error. The program crashed due to type error where I forgot to convert string value to float before doing math operations. The type error was resolved easily.  <br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/Testing/4_testing_report_profit_error.PNG)
<br />
<br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/Testing/5_testing_manager_operations.PNG)
<br />
<br />
## Testing Sale Assistant Purchasing Operation: 
I input invalid input to test input validation. I tested if the program would stop sales assistant log in purchase price higher than sale price. I also tested checking inventory operation and Pokemon Information Function. No bug found here.<br /> 
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/Testing/6_sale_assistant_purchase_testing.PNG)
<br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/Testing/7_inventory_checking.PNG)
<br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/Testing/8_checking_pokemon_information.PNG)
<br /><br />
## Testing Pokemon Selling Function:
I tested the selling function. I tried input invalid input and lower selling price. The system successfully stopped me from those operation without crashing. Sales has been successfully recorded in the JSON file 
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/Testing/9_testing_sell_a_pokemon.PNG)
<br /><br />
## Testing Creating New Accounts:
I also tested adding creating new accounts by input incorrect password reentry and invalid inputs. The system recognize incorrect inputs and prevents me from creating accounts. Eventually, it recognizes correct input and a new account has been added to the JSON file.<br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/Testing/10_adding_new_sale_rep.PNG)
<br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/Testing/11_new_account_added.PNG)