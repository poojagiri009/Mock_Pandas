import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders_2019 = orders[(orders['order_date'] >= '2019-01-01') & (orders['order_date'] <= '2019-12-31')]
    df = users.merge(orders_2019,left_on='user_id',right_on='buyer_id',how='left')
    df_count = df.groupby(['user_id','join_date'])['order_id'].count().reset_index()
    return df_count[['user_id','join_date','order_id']].rename(columns={'user_id':'buyer_id','order_id':'orders_in_2019'})
    
    