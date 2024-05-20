import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    df = sales.merge(product,on='product_id',how='right') #right join
    #sale date is none or not in first quarter
    saleproducts = df[(df['sale_date'] > '2019-03-31') | (df['sale_date'] < '2019-01-01') | (df['sale_date'].isna())] 
    df = product[~product['product_id'].isin(saleproducts['product_id'])]
    return df[['product_id','product_name']]