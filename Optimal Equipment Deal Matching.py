def match_requests_with_sellers(requests, sellers):
    seller_dict = {}
    for equip, price in sellers:
        if equip not in seller_dict or price < seller_dict[equip]:
            seller_dict[equip] = price
    results = []
    for equip, max_price in requests:
        if equip in seller_dict and seller_dict[equip] <= max_price:
            results.append(seller_dict[equip])
        else:
            results.append(None)
    return results
requests = []
num_requests = int(input("Enter the number of buyer requests: "))
print("Enter requests in format: equipment_type max_price")
for _ in range(num_requests):
    equip, max_price = input().split()
    requests.append((equip, int(max_price)))

sellers = []
num_sellers = int(input("Enter the number of sellers: "))
print("Enter sellers in format: equipment_type price")
for _ in range(num_sellers):
    equip, price = input().split()
    sellers.append((equip, int(price)))

result = match_requests_with_sellers(requests, sellers)
print("Matched lowest prices:", result)