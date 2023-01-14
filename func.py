def get_curr_ratings(cols):
    rating_cols = [col for col in cols if "Rating" in col]
    return rating_cols[-1]
