#Crypto currency Aggration: python 

--------
Overview:
--------
Create a python tool that can trade automatically for me using aggregation trading.
This will connect to CryptoToCompare API, check the most resent times __*(Due to free API I’m limited to 100k calls a month)*__ 

__Calls limited:__

* Call / day: 35k
* Call / hour: 2,500
* Call / minute: 100
* Call / second: 10 


__The main currencies that will be watched and traded:__

* BitCoin (BTC)
* Bitcoin Cash (BCH)
* Ethereum (ETH)
* Ethereum Classic (ETC)
* Litecoin (LTC)


### TaskList:

- [x] Set up Request Python and get it working
- [x] Connect to CryptoToCompare and get JSON response back 
- [x] Formate json response to a usable formate
- [ ] Build a Calculation Rules Engine (CRE) to find out risks and possible proffits for some inverstments 
- [ ] Create a visual repesentation of the crypto graph, showing the peaks and dips of the currency 
-  [ ] Link to a handheld device and make the app moblie 
-  [ ] Exspanded the app so i can pitch it to brothers and family 
-  [ ] Once its stable then pay for a API key allowing more advance techniques and tracking
- [ ] use a for loop to extract the keys into an array 
- [ ] look into using classes later to make it more safe etc


####Math WIP:
-[ ] use the math lib to work out risk and rewards
- [ ] use floats to do calculations 

-[x] extract time from response and formate correctly
- [ ] extract date from all of json and save in historical array
