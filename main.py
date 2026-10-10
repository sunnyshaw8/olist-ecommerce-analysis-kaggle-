import pandas as pd
##knowing the data
datas =["olist_customers_dataset.csv","olist_geolocation_dataset.csv","olist_order_items_dataset.csv",
        "olist_order_payments_dataset.csv","olist_order_reviews_dataset.csv","olist_orders_dataset.csv",
        "olist_products_dataset.csv","olist_sellers_dataset.csv","product_category_name_translation.csv"]

for i in datas:
    data = pd.read_csv(i)
    print(i)
    print(f"information of {i} :\n :{data.info()} \n \n ")
    print(f"no of empty cell:{data.isna().sum()}\n \n ")
    print(f"first 2 rows of {i} \n {data.head(2)} \n \n")
    print("\n ends \n \n")

#Unique counts of customer_id and customer_unique_id.