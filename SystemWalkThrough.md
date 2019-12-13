# Sales Assistant Program Walk Through

We will walk through the program as a regular Team Rocket Sales Assistant and as a Team Rocket Division Manager to showcase the powerful program in helping Team Rocket its evil Pokemon Trading Business.
< br />

## Part I - Sale Assistants Section
1. To start, a sales assistant may login as a returning user or create a brand new account with the system. Firstly, let's try create a brand new account:  Pikachu <br /><br />
 ![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/WalkThrough/10_adding_new_account.PNG)

<br />A new account, Pikachu, has been added to our local JSON file:<br />

![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/WalkThrough/11_new_account_data.PNG)
<br /><br />
2. Once logged in, the user is directed to the Sales Assistant Operation page where various functions are provided. We start it first with purchasing a new Pokemon<br /><br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/WalkThrough/2_purchase_pokemon.PNG)
<br /><br />
3. After the Pokemon is purchased, we need to start making some money. Let's sell a Pokemon: <br /><br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/WalkThrough/3_record_sale.PNG)
<br /><br />
The selling function first display the Pokemon inventory to Sales Assistant. Sales Assistant may choose which Pokemon to sell and record its selling price to the system. Here we can see that Pokemon Inventory ID 0 has been sold at a price of 100. This sale made $100 after cost profit for Team Rocket!
<br /><br />
4.  Let's say you are looking at the Pokemon Index and would like to know a Pokemon's basic information such as its name, attack, and HP stats, this program provides the function to search information by Pokemon Index number: <br /><br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/WalkThrough/4_check_info.PNG)
<br /><br />
We looked up Pokemon Index, 777, in the system,  which searched through Pokemon database, and displayed it's basic information.<br /><br />
5. At this point, the sales assistant is satisfied with his/her work today. The sales assistant saves the record and exits the program. The sales assistant's operation is logged to the JSON database: <br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/WalkThrough/5_purchase_recorded_data.PNG)
<br /><br />
## Part II - Manager Section
1. As one of the most important part to Team Rocket's evil operation, manager has the privilege to view performing information that a regular sales assistant cannot access. First of all, a manager login to the system using its secret account name and password: teamrocket, to access the manager view: <br />

![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/WalkThrough/6_manager_view.PNG)
<br /><br />As one can see from the above figure, Team Rocket managers are provided with management tools rather than daily operation tool.<br />

2. Let the manager check out the each Sale Representative's profit for their time working for Team Rocket: <br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/WalkThrough/7_profit_by_Sale_reoresentative.PNG)
<br /><br />We can see in the system, we have 5 accounts. The first account teamrocket is the manager account, which does not do any Pokemon Trading operations. <br /><br />
Sales Assistant, <b>rep123</b>, has generated $277 profit for Team Rocket. rep123 is on the safe side.<br /><br />
Sales Assistant, <b>scottsun</b>, has generated $0 profit for Team Rocket. The manager can easily identify him and will issue a warning to scottsun. If scottsun does not increase his business performance next month, the manager will send an evil rattata to make him disappear at the end of next business cycle. As we all know, Team Rocket is not a charity organization, we need more profits.<br />
<br />
3. The second function allows the manager to view his/her division's total profit in the current business cycle: <br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/WalkThrough/8_total_profit.PNG)
<br /><br />
Similar to the evaluation of each sales assistant, if the division is doing badly, the division manager is under pressure from the higher up. Team Rocket does not provide to useless members. <br />
<br />
4. Team Rocket manager can also use the program to view all sales assistants. This function helps the manager to decide whether he/she needs to hire more people: <br />
![enter image description here](https://raw.githubusercontent.com/scottsun17/SaleAssistantSystem/master/pic/WalkThrough/9_Sale_assistants.PNG)
<br /><br />
5. Team Rocket manager does not involve with daily operations. Thus the manager section does not provide any functionalities to sell or purchase Pokemon. Managers also cannot change each sales assistants' performances. Once data is recorded in the system, no one can change it. <br /><br />
<B>Even though Team Rocket is an evil international criminal organization, we are an equal opportunity criminal employer and value diversity at our organization. We do not discriminate on the basis of race, religion, color, national origin, gender, sexual orientation, age, marital status or disability status.</b>
<br />

## Apply to Team Rocket today! But don't be scottsun, the none performing sales assistant <3