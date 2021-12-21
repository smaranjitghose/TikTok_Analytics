
from TikTokApi import TikTokApi as tiktok
import json
from process_data import clean_json
import pandas as pd
import sys

def get_data(hashtag):
    verifyFp = "verify_kx2ee558_BH6fvQVi_cXHF_4lfK_Bimg_hH0lYMCV6Vm6"
    # Initialize an instance of the TikTokApi class for non-production endpoints
    api = tiktok.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)
    # Get data by hashtag
    trend_data = api.by_hashtag(hashtag)
    # Perform Preprocessing
    trend_data = clean_json(trend_data)
    # Convert to DataFrame
    trend_df = pd.DataFrame.from_dict(trend_data, orient='index')
    # Save to Disk
    trend_df.to_csv('./data/preprocessed/tiktokdata.csv', index=False)


if __name__ == '__main__':
    get_data(sys.argv[1])

