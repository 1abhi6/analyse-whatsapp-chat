import streamlit as st
from abc import ABC, abstractmethod

from preprocessor import Preprocess
from analysis import (Analyse,
                      UserList,
                      GroupSpecificAnalysis
                      )
from components import Plot, PADDING_TOP


class Sidebar(ABC):
    def __init__(self):
        st.sidebar.title('WhatsApp Chat Analyser')
        self.sidebar()

    def sidebar(self):
        upload_file = st.sidebar.file_uploader('Choose a text file')
        if upload_file is not None:
            bytes_data = upload_file.getvalue()
            data = bytes_data.decode('utf-8')

            try:
                preprocessor_obj = Preprocess(data)
                self.df = preprocessor_obj.text_to_df()
                self.user_list_obj = UserList(self.df)
                users_list = self.user_list_obj.user_list()

                self.selected_user = st.sidebar.selectbox(
                    'Show Analysis', users_list)
                self.analysis_obj = Analyse(self.df, self.selected_user)

                self.show_analysis_btn()

            except Exception as e:
                # st.sidebar.error(
                #     'Invalid file format, The file should be Whatsapp exported .txt file.'
                # )
                st.sidebar.error(e)

    @abstractmethod
    def show_analysis_btn(self):
        pass


class Main(Sidebar):
    def __init__(self):

        # Page configuration
        st.set_page_config(
            layout='wide', page_title="Abhi's WhatsApp Analyser", page_icon='📊')
        super().__init__()

    def show_analysis_btn(self):
        if st.sidebar.button('Show Chat Analysis'):
            
            if not self.selected_user == 'Overall':
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write()

                with col2:
                    # Give custom padding at top
                    st.markdown(PADDING_TOP, unsafe_allow_html=True)

                    st.title("{}'s Analysis".format(self.selected_user))

                with col3:
                    st.write()

            else:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write()

                with col2:
                    # Give custom padding at top
                    st.markdown(PADDING_TOP, unsafe_allow_html=True)

                    st.title('Overall Chat Analysis')

                with col3:
                    st.write()

                self.group_specific_analysis = GroupSpecificAnalysis(
                    self.df, self.selected_user)

            self.plot = Plot(self.df, self.selected_user)

            st.divider()
            self.quick_metric()
            st.divider()
            self.plot_most_active_users()
            st.divider()
            self.plot_word_cloud()

    def quick_metric(self):
        st.subheader('Quick Metrices',
                     help='Quick overview of the entire chat')

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            num_messages = self.analysis_obj.num_messages()
            st.metric(label='Total Messages', value=num_messages)

        with col2:
            total_words = self.analysis_obj.total_words()
            st.metric(label='Total Words', value=total_words)

        with col3:
            media_shared = self.analysis_obj.media_shared()
            st.metric(label='Media Shared', value=media_shared)

        with col4:
            links_shared = self.analysis_obj.links_shared()
            st.metric(label='Links Shared', value=links_shared)

    def plot_most_active_users(self):
        if self.selected_user == 'Overall':
            col1, col2 = st.columns(2)
            with col1:
                st.subheader('Most Active Users',
                             help='Most active user with number of chats')
                self.plot.plot_most_active_users()

            with col2:
                st.subheader('Most Active Users (Percentage)',
                             help='Most active user with percentage of chats')

                users = self.group_specific_analysis.most_active_users_percentage()
                st.dataframe(users)

    def plot_word_cloud(self):
        st.subheader('Frequently Used Words',
                     help='Wrod cloud of frequently used words')
        self.plot.plot_word_cloud()


if __name__ == '__main__':
    Main()
