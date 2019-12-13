# Project Two - Sales Assistant Management System
This is an accounting system to help Team Rocket to manage its' illegal Pokemon trading business. The system is divided into two part: <b>sales assistant section</b> and <b>manager section</b>
<br />
<br />

# Software Instruction
1. Downloads source codes and database (included in the zip file)
2. Install Dependencies
<B>Dependencies:</b>

|Package|Version  |
|--|--|
|prettytable|0.7.2|
|numpy|1.17.4|
|pandas|0.25.3|
|requests|2.22.0|

3. run SaleManagementSystem.py to start the program

# Program Functionalities
Team Rocket Users may log in as Sales Assistants or Division Manager.  <br />
<b>Sales Assistant Login</b>
To log in as a <b>Sales Assistant</b>, user may input regular sales assistant username and password. The system recognizes sales assistant account and will automatically redirect to sale assistant page for further operations. (See account.json for more existing usernames and passwords).
<br /> 
<b>Manager Login</b>
To log in as a <b>manager</b>, user may input special manager user name and password. The system recognizes manager username and password and will automatically redirect to manager page for further operations.<br />
The System has only one manager account:
Username: teamrocket
Password: teamrocket
 <br /> 
 <b>Add new Account</b>
 The system allows user to add new sales assistants by adding new accounts. Account information is stored in account.json file

## Sales Assistant Section
This section of the system allows team rocket sale assistant to log each purchase and sell of Pokemon. Here is a description of the functionalities:

 - Purchase a Pokemon: 
	 - Assistant records each Pokemon purchased; if team rocket has already had that Pokemon in inventory, the purchasing operation will be denied.
	 - Each purchase requires sales assistant to record purchase price and estimated sell price. Sales assistant cannot purchase a Pokemon at a price higher than its' estimated sell price 
 - Sell a Pokemon:
	 - Assistant records the actual selling price, marked the Pokemon as sold in record, and record the assistant ID in record for the sell
	 - The system prevents  assistant from selling a Pokemon at price lower than purchase price
 - Check Inventory:
	 - List out all available Pokemon for sale
- Check Pokemon Information by PokeIndex:
	- Allow sale assistant to quickly look up Pokemon information such as attack, defense, and other status
	- Help assistant determines the value of a Pokemon
- Clear Screen
	- Clear UI Screen for readability
- Save and Exit
	- Allow the assistant to safely record all transaction to the Database (a Json file) and log out from the system

<b>Demos:</B>

Sale Assistants login to this section to record purchasing and selling of Pokemon. 
<br />
![Assistant Login](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/assistant_operation.PNG)

<br />
To Purchase a Pokemon: <br />

![Purchase Recording](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/Purchase_pokemon.PNG)
<br />

## Manager Section 
This section of the system allows team rocket manager to monitor its Pokemon trading business, evaluate each sales assistant's performance, and monitor inventory. <br />
Here is a description of the functionalities:

 - Check Profit by Each Assistant
	 - This function allows the manager to check total profit made by each assistant. Low performers can be easily identified. Team Rocket does not need low performer.
- Check Total Profit
	- This function sums up all profits made in the division. Team Rocket does not need low performing division.
-  Check Pokemon Inventory
	- List out all available Pokemon for sale
- List All Sale Representatives
	- Display all Team Rocket Sales Assistants
- Log Out
	- Allow manager to safely log out without any change to the database

<b>Demos:</B>
A list of manager operations:

![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/manager_operations.PNG)

Operation 1 - check profit by sales assistants

![operation 1](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/profit_by_individual.PNG)

Operation 2 - Check Total Profit![operation 2](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/total_profit.PNG)

Operation 4 - List all Sales Assistant Accounts
![operation 4](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/lsit_assistants.PNG)

## Database (JSON Files)
The system relies on three database tables for operations:
 1. External Pokemon Database - [JSON](https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/pokedex.json) file by [Fanzeyi](https://github.com/fanzeyi/pokemon.json)
 2. Internal Database for username and password management - [account.json](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/code/data/account.json)
 3. Internal Database for transaction management - [record.json](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/code/data/record.json)

## Flow Chart
The system flow chart walks through basic design of the system. 
![System Flow Chart](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/SystemChart.png)

## Credits:
Author: Scott (Ziteng) Sun

External Sources: 
Pokedex JSON file - [fanzeyi](https://github.com/fanzeyi/pokemon.json) 

## Copyright Notice:
All Pokemon related information are copyrighted by the Pokémon Company and its affiliates. This repository is merely a fun program creation of data collected by the editors of [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Main_Page).
