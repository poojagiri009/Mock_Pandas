import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    is_valid = (cinema['id'] %2 != 0) & (cinema['description'] != 'boring')
    return cinema[is_valid].sort_values(by='rating',ascending=False)