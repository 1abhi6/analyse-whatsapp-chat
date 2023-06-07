# WhatsApp Chat Analyzer

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/1abhi6/whatsapp-chat-analyzer/blob/main/LICENSE)

A Python tool to analyze and visualize WhatsApp chat data.

![Preview](notebook\images\gif_img.gif)

## Table of Contents

- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Instructions](#instructions)
- [Examples](#examples)
- [License](#license)
- [Contact](#contact)

## About

WhatsApp Chat Analyzer is a Python tool that enables you to analyze and visualize your WhatsApp chat data, whether it's a one-to-one chat or a group chat. With this tool, you can also analyze the data for a single person. It provides various metrics and insights about your chat history, including message count, word count, media sharing, most common words, most used emojis, activity timeline, and more. The tool is built using Python, Pandas, Streamlit, Emoji, and other libraries.

## Features

- Calculate total messages and words
- Identify media shared
- Extract URLs
- Generate word cloud
- Find most common words
- Analyze emoji usage
- Create activity timeline
- Visualize daily message counts
- Determine the most active day of the week
- Identify the most active month
- Generate an activity heatmap
- Analyze group-specific data (active users, chat percentages)

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/1abhi6/analyse-whatsapp-chat.git
   ```

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Export your WhatsApp chat history as a text file (.txt) following the instructions provided in the [Instructions section](#instructions).

2. The project will be hosted soon.

3. Run the `app.py` script:

   ```shell
   streamlit run app.py
   ```

4. Launch the web application by opening the provided local URL in your web browser.

5. Select the chat file (.txt) and click on Show Chat Analysis button.

6. Explore the generated metrics, charts, and insights based on your WhatsApp chat data.

## Instructions

### How to Generate a .txt File without Media from WhatsApp?

**Note:** Steps are similar in Android or iOS device.

To generate a .txt file without media from the WhatsApp app, you can follow these general steps:

1. Open the WhatsApp Android app on your device.

2. Navigate to the chat you want to export and open it.

3. Tap the three-dot menu icon in the top-right corner of the chat screen.

4. From the menu options, select "More" or "Settings" (the specific option may vary depending on the WhatsApp version).

5. Look for the "Export chat" or similar option and select it. This option allows you to export the chat conversation.

6. Choose whether to include media files or exclude them. In this case, To generate a .txt file without media, select the option to exclude media files.

7. Select the sharing or saving method for the exported file. You can choose to send the file via email, share it through messaging apps, or save it to a cloud storage service.

8. If you choose to save the file, select the destination on your device where you want to save it. Remember the location for later access.

9. Wait for the export process to complete. This may take a few moments depending on the size of the chat and the speed of your device.

Please note that these steps are a general guideline and may vary slightly depending on the version of WhatsApp or any updates made to the app.

## Examples

Here are some examples of the insights you can obtain using WhatsApp Chat Analyzer:

### Word Cloud

![Word Cloud](./images/word_cloud.png)

### Most Common Words

![Most Common Words](./images/most_common_words.png)

### Activity Timeline

![Activity Timeline](./images/activity_timeline.png)

### Daily Message Counts

![Daily Message Counts](./images/daily_message_counts.png)

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.

## Contact

For any questions or inquiries, feel free to reach out to me at:

- Website: [Abhishek Gupta](https://abhi.getifyme.com/)
