# CrytoCompare Api
Param
(
    $APIKEY = "&api_key={5a9748bb1c9c06420cf3697058624cad4ebb17a94eedad940ac110a1d519b8b6}", 
    $ApiCall = "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,eth&tsyms=USD,EUR,GBP"
 
)

<#
    create a method to get the currency names
    method to get the market ids 
    store in key value pair
    use key values to get statstics from the currencis
#>
#method to get all currency names and store in an array
function GetMarketsNames
{
    $MarketResponse = Invoke-RestMethod -uri $ApiCall -Method Get 

    #Displays the raw formate of the API call USD
    $MarketResponse.RAW.BTC.GBP
   

}

function Main
{
    GetMarketsNames
}
 
Main