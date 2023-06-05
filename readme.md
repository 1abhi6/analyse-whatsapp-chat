# WhatsApp Chat Analyzer

## Description
WhatsApp Chat Analyzer is a Python-based project that allows you to analyze exported text files from WhatsApp chats, whether they are individual or group chats. The project aims to provide insightful analysis and visualizations based on the chat data. It utilizes various libraries such as numpy, pandas, plotly, streamlit, and more to facilitate data manipulation, analysis, and visualization.

**Please Note** : This project is currently under development, and new features and enhancements are being actively added.

## Features
- Import and parse WhatsApp chat data from exported text files.
- Identify chat participants and their respective message frequencies.
- Generate word clouds to visualize commonly used words in the chat.
- Calculate and display chat statistics such as total messages, average message length, and message distribution.
- Analyze chat activity patterns based on different timeframes (hourly, daily, weekly, monthly).
- Create interactive visualizations using plotly to present chat insights.
- Utilize streamlit for building a user-friendly web interface to interact with the project.

## Installation
1. Clone the GitHub repository:

   ```bash
   git clone https://github.com/1abhi6/analyse-whatsapp-chat.git
   ```

2. Change into the project directory:

   ```bash
   cd analyse-whatsapp-chat
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Export the WhatsApp chat you want to analyze as a text file. This can be done by opening the chat, clicking the three-dot menu, and selecting "More" > "Export chat".
2. Place the exported text file in the project directory.
3. Run the project:

   ```bash
   streamlit run app.py
   ```

4. The project will start a local web server and display a URL. Open the provided URL in your web browser to access the WhatsApp Chat Analyzer interface.
5. Upload the exported text file using the provided interface.
6. Explore the various analysis options and visualizations available to gain insights into the WhatsApp chat.

## Roadmap
The WhatsApp Chat Analyzer project is continuously evolving, and the following features and improvements are planned:

- Integration with additional messaging platforms (e.g., Telegram, Facebook Messenger).
- Deployment

## Contributing
Contributions to the WhatsApp Chat Analyzer project are welcome! If you have any ideas, bug reports, or feature requests, please open an issue on the GitHub repository. If you'd like to contribute code, feel free to submit a pull request following the standard GitHub workflow.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- The developers of numpy, pandas, plotly, streamlit, and other open-source libraries used in this project.
- The contributors to the WhatsApp Chat Analyzer project.
- Inspiration from similar projects and the vibrant open-source community.

## Contact
For any inquiries or feedback, please contact:
- Abhishek Gupta: [abhi@getifyme.com](mailto:abhi@getifyme.com)

Feel free to reach out with any questions, suggestions, or collaboration opportunities. Happy analyzing!