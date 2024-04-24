# Advanced YT Analytics

## Overview

Advanced YT Analytics is a Python program that provides real time comprehensive analytics for YouTube videos and channels. It fetches video data, including details, metadata, and statistics, as well as channel data based on a given video ID. The program calculates ratios such as view-like, view-dislike, like-dislike, and comment ratios, and displays this information in an easy-to-read format.

The program features simple-to-use and easy-to-understand code, with comments explaining each section for better clarity and ease of customization.

This program also includes an accurate dislike count feature, despite YouTube removing the dislike count from public view. The program uses a third-party provider to retrieve accurate dislike counts for videos.

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/bzm10/Advanced-YT-Analytics
    ```

2. Navigate to the project directory:

    ```shell
    cd Advanced-YT-Analytics
    ```

3. Install the required packages:

    ```shell
    pip install requests
    pip install google-api-python-client
    pip install python-dotenv
    ```

4. It's recommended to use a virtual environment for better isolation and dependency management.

### Alternatively, you can simply download the code.

## Obtaining an Free API Key

To use this program, you'll need a YouTube API key. Follow these steps to obtain one:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the YouTube Data API v3 for the project.
4. Create credentials (API key) for the project.
5. Copy the API key and set it as an environment variable named `YT_KEY`.

## Usage

To run the program, execute the following command in the terminal:

```shell
python main.py
```

You may need to replace the default video ID in the script with the ID of the video you want to analyze.

## Example Output

Here is an example of the output you might see when you run the program:

```
Video Data For: erLbbextvlY
Video Title: 7 Days Stranded On An Island
Video Published At: 2024-03-30T16:00:01Z
Video Thumbnail: https://i.ytimg.com/vi/erLbbextvlY/hqdefault.jpg
Views: 129,182,012
Likes: 4,988,630
Dislikes: 78,664
Comments: 138,990
Duration: 22:26
Caption: true
Definition: hd
Licensed Content: True
Video Tags: ['Stranded on an island','mrbeast','7 day challenge']
View-Like Ratio: 3.86%
View-Dislike Ratio: 0.06%
Like-Dislike Ratio: 1.58%
Comment Ratio: 0.11%

Channel Data For: UCX6OQ3DkcsbYNE6H8uQQuVA
Channel Title: MrBeast
Channel Published At: 2012-02-20T00:43:50Z
Channel Thumbnail: https://yt3.ggpht.com/fxGKYucJAVme-Yz4fsdCroCFCrANWqw0ql4GYuvx8Uq4l_euNJHgE-w9MTkLQA805vWCi-kE0g=s800-c-k-c0x00ffffff-no-rj
Subscribers: 253,000,000
Views: 47,258,169,440
Videos: 576
Country: US
Channel Keywords: ['mrbeast','mrbeast6000']
Custom URL: @mrbeast
Banner Image: https://yt3.googleusercontent.com/NP3nTQ3kxLiXV-kLXKS2zaNL6ESMMBv74m-d5a--q5ThgLD6I-IyqLwAbj-AbClWNbORBg3Pcg
```

## Additional Information

- The program uses the `requests` package for making HTTP requests and the `google-api-python-client` package for interacting with the YouTube API.
- Ensure you have set the `YT_KEY` environment variable with your YouTube API key before running the program.

## Feel Free to Use and Edit

Feel free to use, edit, and customize this program for your own projects. Whether you're a beginner or an experienced developer, the code's simplicity and clarity make it easy to work with. Contributions, suggestions, and feedback are welcome!
