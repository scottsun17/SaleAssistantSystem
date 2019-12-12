# Project Two - Sales Assistant Management System
This is an accounting system to help Team Rocket to manage its' illegal Pokemon trading business. The system is divided into two part: <b>sales assistant section</b> and <b>manager section</b>
<br />
<br />
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

Some Demos:

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
	- Same function as assistant function
