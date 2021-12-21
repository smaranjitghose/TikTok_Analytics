def clean_json(data):
    """
    Method to flatten and clean the raw json data obtained from the TikTok API
    """

    # Decide the attributes to be dropped and flattened after EDA
    expand_attributes = ['video', 'author', 'music', 'stats', 'authorStats']
    drop_attributes = ['challenges', 'duetInfo', 'textExtra', 'stickersOnItem']
    # Create an empty dictionary for the preprocessed data
    res = dict()
    # Loop through each video
    for i, vid in enumerate(data):
        # Initialize the value of ith video to an empty dictionary 
        res[i] = dict()
        # Iterate over each attribute of the video 
        for k, v in vid.items():
            # If the attribute is essential for the analysis
            if k not in drop_attributes:
                # If the attribute can be broken down into multiple attributes
                if k in expand_attributes:
                    for sub_k, sub_v in v.items():
                        res[i][k + '_' + sub_k] = sub_v
                # If the attribute cannot be broken down into multiple attributes
                else:
                    res[i][k] = v

    return res
