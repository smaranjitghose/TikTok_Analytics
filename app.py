import streamlit as st
import pandas as pd
from subprocess import call
import plotly.express as px

def main():

    # Basic App Configuration
    st.set_page_config(
        page_title="TikTok Analytics",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            "Get Help": "https://github.com/smaranjitghose/TikTokAnalytics/",
            "Report a bug": "https://github.com/smaranjitghose/TikTokAnalytics/issues",
            "About": "# This app serves as a MVP for real time data analysis for social media platforms like TikTok and Instagram."
        },)

    # Create sidebar text and buttonds
    st.sidebar.markdown("<div><img src='https://png2png.com/wp-content/uploads/2021/08/Tiktok-logo-png.png' width=100 /><h1 style='display:inline-block'>Tiktok Analytics</h1></div>", unsafe_allow_html=True)
    st.sidebar.markdown("A dashboard for real time data analysis of TikTok data")
    hashtag = st.sidebar.text_input(label = "Enter hastag" ,max_chars=100 ,help = "Enter a hashtag without any spaces and less than 100 characters long",placeholder = "Eg: #stopasianhate")

    # Button to initiate the analysis
    if st.sidebar.button("Get Data"):
        with st.spinner('Fetching Data...'):
            # Run get data function here
            call(['python', 'src/get_data.py', hashtag])
            # Load in existing data to test it out
            df = pd.read_csv('./data/preprocessed/tiktokdata.csv')
        st.balloons()
        
        # Most effective videos for this hashtag
        st.markdown(f"### Top videos trending for #{hashtag}")
        fig_1 = px.scatter(df, 
                           x="stats_shareCount", y="stats_commentCount",
                           size='stats_playCount', color='stats_playCount',
                           hover_data=['desc'],
                           labels = {'stats_commentCount': 'Number of comments', 'stats_shareCount': 'Number of shares', 'stats_playCount': 'Number of times played'} )
        
        st.plotly_chart(fig_1, use_container_width=True)


        # Most effective content creaters for this hashtag

        st.markdown(f"### Top content creaters for #{hashtag}")
        fig_2 = px.scatter(df, 
                           x='authorStats_followerCount', y='authorStats_heartCount',
                           size='authorStats_videoCount', color='authorStats_videoCount',
                           hover_data=['author_nickname'],
                           labels = {'authorStats_videoCount': 'Number of Videos', 'authorStats_followerCount': 'Number of followers', 'authorStats_heartCount': 'Number of hearts recieved'} )
        
        st.plotly_chart(fig_2, use_container_width=True)
        


        # Distribution of number of shares 
        st.markdown(f"### Distribution of number of shares for  #{hashtag}")
        fig_3 = px.histogram(df,
                             x="stats_shareCount", nbins=20, 
                            labels={"stats_shareCount": "Number of shares", "count": "Count"})
        st.plotly_chart(fig_3, use_container_width=True)


        
        left_col, right_col = st.columns(2)

        # Duration of videos
        fig_4 = px.strip(df, 
                        x= "desc", y = "video_duration",
                        color = "stats_diggCount",
                        hover_data=['video_duration'],
                        title = "Duration of videos",
                        labels={"video_duration": "Video Duration", "desc": "Videos"})
        fig_4.update_xaxes(showticklabels=False)
        left_col.plotly_chart(fig_4, use_container_width=True)



        # Most Popular videos
        fig_5 = px.histogram(df,
                             x='desc', y='stats_diggCount',
                            hover_data=['desc'],
                            title = "Most Popular videos",
                            labels={"stats_diggCount": "Digg Count", "desc": "Videos"}) 
        fig_5.update_xaxes(showticklabels=False)
        right_col.plotly_chart(fig_5, use_container_width=True)


        # Show Raw Data and provide option to download

        with st.expander('View Raw Data'):
            st.dataframe(df)
            # Convert the dataframe to a csv file
            csv = convert_df(df)
            # Create a button to download the csv file
            st.download_button(
                label="Download as CSV",
                data=csv,
                file_name='tiktok_data.csv',
                mime='text/csv',
            )
        closing_notes()


@st.cache
def convert_df(df):
     return df.to_csv().encode('utf-8')


def remove_footer():
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

def closing_notes():
    st.markdown("Made with ❤️ by [Smaranjit Ghose](https://www.linkedin.com/in/smaranjitghose/)")


if __name__ == '__main__':
    main()