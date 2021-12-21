# TikTok Analytics

This project is built to simulate a real world scenario where a market team of a company would require analytics data from TikTok to make decisions about penetrating the platform with it's presence.


> NOTE📌:
>
> This project was built using community maintained open source software and is intended only for educational purposes



## Usage⚒️:


## Project Workflow Timeline🏗️ :

1. Analyse TikTok Platform
  
> Insight: TikTok prevents automated scrapping natively by using signed requests

2. Alternatives for getting data with least amount of resources (time and money):

    - [Python TikTok API [Unofficial]](https://github.com/davidteather/TikTok-Api) ✅
    - [Tik API](https://tikapi.io/)
3. Creating virtual environment for project

```
conda create --name tiktok python=3.9
```

4. Activate virtual environment and install dependencies

```
conda activate tiktok
conda install TikTokApi pandas streamlit
```

5. Create an empty directory and initialize it as a git repository

```
mkdir tiktok_analytics
cd tiktok_analytics
git init
```

6. Get TikTok Cookie Data
    1. Open Google Chrome (similar for Brave or Mozilla Firefox or Edge)
    2. Visit [TikTok's website](https://www.tiktok.com/)
    3. Inspect the Website [CTRL + Shift + I]
    4. Click on the *Applications* tab
    5. Move to the *Storage* section
    6. Select *Cookies*
    7. Copy the value for s_v_web_id

7. Fetch Data using API
> Insight: Initialize API with test end points rather than production end points

8. Store Raw Data as JSON

9. Perform Exploratory Data Analysis on raw JSON data 

10. Write Scripts for [Pre-Processing](./src/process_data.py) Data

11. Save Cleaned Data as Dataframe

12. Build Basic [Dashboard](./app.py) [Use Streamlit]

13. Make Visualizations: [Use Ploty]
    - Top videos trending in the hashtag
    - Top creators for the hastag
    - Length of videos for the hastag
    - Reach of videos for the hashtag

14. Add Feature to get hashtag data in real time

> Insight: There is a conflict in the asynchronous functioning of streamlit and Tiktok API. 
> Workaround: Instead of declaring a function to fetch and process the data, execute it in a separate script (Use subprocess)


15. Create a requirements.txt file

16. Make a remote repository on GitHub, Add Remote to local repository and push the commits to GitHub
```
git remote add origin htttps://www.github.com/your_user_name/your_repo_name.git
git remote --verbose
git add .
git commit -m "v1.0.0"
git push origin master
```

> It is assumed that you commited your changes progressively while building the project

15. Create [shell script](./setup.sh) and [Procfile](./Procfile) to host dashboard on Heroku

> Install Heroku CLI if not done already

16. Create an instance of Heroku Dyno, push the dashboard source, build and deploy it.



## License 📜



[<p align = 'center'><img src = 'https://media.giphy.com/media/XfD8VJDUurgMjNEP72/giphy.gif' width = 40%></p>](./LICENSE)
