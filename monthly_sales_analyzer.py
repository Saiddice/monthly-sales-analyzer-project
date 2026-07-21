sales_data = [
    {"day": 1,  "product_a": 150, "product_b": 80,  "product_c": 200},
    {"day": 2,  "product_a": 160, "product_b": 90,  "product_c": 180},
    {"day": 3,  "product_a": 140, "product_b": 100, "product_c": 220},
    {"day": 4,  "product_a": 170, "product_b": 85,  "product_c": 190},
    {"day": 5,  "product_a": 155, "product_b": 95,  "product_c": 210},
    {"day": 6,  "product_a": 165, "product_b": 110, "product_c": 175},
    {"day": 7,  "product_a": 145, "product_b": 75,  "product_c": 230},
    {"day": 8,  "product_a": 180, "product_b": 120, "product_c": 195},
    {"day": 9,  "product_a": 175, "product_b": 105, "product_c": 205},
    {"day": 10, "product_a": 130, "product_b": 70,  "product_c": 240},
    {"day": 11, "product_a": 190, "product_b": 115, "product_c": 185},
    {"day": 12, "product_a": 160, "product_b": 90,  "product_c": 200},
    {"day": 13, "product_a": 150, "product_b": 100, "product_c": 215},
    {"day": 14, "product_a": 185, "product_b": 125, "product_c": 180},
    {"day": 15, "product_a": 170, "product_b": 95,  "product_c": 225},
    {"day": 16, "product_a": 140, "product_b": 80,  "product_c": 235},
    {"day": 17, "product_a": 195, "product_b": 130, "product_c": 190},
    {"day": 18, "product_a": 165, "product_b": 110, "product_c": 210},
    {"day": 19, "product_a": 155, "product_b": 85,  "product_c": 220},
    {"day": 20, "product_a": 175, "product_b": 100, "product_c": 205},
]

def total_sales_by_product(data, product_key):
    total = 0
    for day in data:
        total += day[product_key]
    return total

def average_daily_sales(data, product_key):
    total = total_sales_by_product(data, product_key)
    return total / len(data)

def best_selling_day(data):
    best_day = None
    best_total = -1
    for day in data:
        day_total = day["product_a"] + day["product_b"] + day["product_c"]
        if day_total > best_total:
            best_total = day_total
            best_day = day["day"]
    return best_day

def days_above_threshold(data, product_key, threshold):
    count = 0
    for day in data:
        if day[product_key] > threshold:
            count += 1
    return count

def top_product(data):
    totals = {
        "product_a": total_sales_by_product(data, "product_a"),
        "product_b": total_sales_by_product(data, "product_b"),
        "product_c": total_sales_by_product(data, "product_c"),
    }
    best_product = None
    best_total = -1
    for product_key, total in totals.items():
        if total > best_total:
            best_total = total
            best_product = product_key
    return best_product

def worst_selling_day(data):
    worst_day = None
    worst_total = None
    for day in data:
        day_total = day["product_a"] + day["product_b"] + day["product_c"]
        if worst_total is None or day_total < worst_total:
            worst_total = day_total
            worst_day = day["day"]
    return worst_day

def top_3_days(data):
    day_totals = []
    for day in data:
        day_total = day["product_a"] + day["product_b"] + day["product_c"]
        day_totals.append((day["day"], day_total))
    day_totals.sort(key=lambda item: item[1], reverse=True)
    return day_totals[:3]

def sales_range(data, product_key):
    values = [day[product_key] for day in data]
    return max(values) - min(values)

if __name__ == "__main__":
    print("=== FUNCIONES OBLIGATORIAS ===")
    print("Ventas totales Producto A:", total_sales_by_product(sales_data, "product_a"))
    print("Ventas totales Producto B:", total_sales_by_product(sales_data, "product_b"))
    print("Ventas totales Producto C:", total_sales_by_product(sales_data, "product_c"))
    print("Promedio diario Producto A:", average_daily_sales(sales_data, "product_a"))
    print("Mejor día de ventas:", best_selling_day(sales_data))
    print("Días con Producto A sobre 170:", days_above_threshold(sales_data, "product_a", 170))
    print("Producto más vendido:", top_product(sales_data))
    print("\n=== RETOS OPCIONALES ===")
    print("Peor día de ventas:", worst_selling_day(sales_data))
    print("Top 3 días:", top_3_days(sales_data))
    print("Rango ventas Producto C:", sales_range(sales_data, "product_c"))
