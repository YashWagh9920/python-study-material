import requests

def main():
    company_name = input("enter company name:-")
    url = f"https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query={company_name}"
    response = requests.get(url)
    data = response.json()
    list1 = data["data"]["data"]
    print(data["message"])
    print("\n")
    
    print("Stock Information of",company_name,"is :-")
    for item in list1 :
        print(item["Name"])
        print(item["MarketCap"])
        print(item["CurrentPrice"])
        print("\n")
    

if __name__ == "__main__":
    main()