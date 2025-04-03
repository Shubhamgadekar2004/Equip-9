from collections import defaultdict
def process_queries(maintenance_logs, queries):
    date_costs = defaultdict(int)
    for equip_id, date, cost in maintenance_logs:
        date_costs[date] += cost
    results = []
    for start_date, end_date in queries:
        total_cost = sum(cost for date, cost in date_costs.items() if start_date <= date <= end_date)
        results.append(total_cost) 
    return results
maintenance_logs = []
n = int(input("Enter number of maintenance records: "))
print("Enter records in format: equipment_id date(YYYY-MM-DD) cost")
for _ in range(n):
    equip_id, date, cost = input().split()
    maintenance_logs.append((int(equip_id), date, int(cost)))
queries = []
q = int(input("Enter number of queries: "))
print("Enter queries in format: start_date(YYYY-MM-DD) end_date(YYYY-MM-DD)")
for _ in range(q):
    start_date, end_date = input().split()
    queries.append((start_date, end_date))
result = process_queries(maintenance_logs, queries)
print("Total maintenance costs for queries:", result)
