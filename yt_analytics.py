# Import necessary modules
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import requests

# Load environment variables and set up YouTube API client
load_dotenv()
API_KEY = os.getenv('YT_KEY')  # YouTube API key from environment variables
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Function to fetch video data (details, metadata, and statistics)
def fetch_video_data(video_id):
    """
    Fetch video data, including details, metadata, and statistics.
    
    Args:
        video_id (str): The ID of the video.
    
    Returns:
        dict: The data about the video.
    """
    # Define API request parts for video data
    part_types = 'contentDetails,snippet,statistics'
    
    # Make the API request to fetch video data
    video_request = youtube.videos().list(part=part_types, id=video_id)
    video_response = video_request.execute()
    
    # Check if video data is available
    if not video_response['items']:
        print("No data available for the provided video ID.")
        return None
    
    # Extract video data
    video_data = video_response['items'][0]
    content_details = video_data['contentDetails']
    snippet = video_data['snippet']
    statistics = video_data['statistics']
    
    # Display video data and calculate ratios
    print_video_data(snippet, content_details, statistics, video_id)
    calculate_and_print_video_ratios(statistics, video_id)
    
    # Return channel ID for fetching channel data
    return snippet.get('channelId', 'N/A')

# Function to print video data
def print_video_data(snippet, content_details, statistics, video_id):
    """
    Print video details including title, publication date, thumbnail, views, likes, dislikes, comments, duration, caption, definition, licensed content, and tags.
    
    Args:
        snippet (dict): Video snippet containing metadata.
        content_details (dict): Content details of the video.
        statistics (dict): Statistics of the video.
        video_id (str): The ID of the video.
    """
    print("Video Data For:", video_id)
    print("Video Title:", snippet.get('title', 'N/A'))
    print("Video Published At:", snippet.get('publishedAt', 'N/A'))
    print("Video Thumbnail:", snippet['thumbnails']['high'].get('url', 'N/A'))
    print("Views:", statistics.get('viewCount', 'N/A'))
    print("Likes:", statistics.get('likeCount', 'N/A'))
    print("Dislikes:", get_dislike_count(video_id))  # Fetch dislike count
    print("Comments:", statistics.get('commentCount', 'N/A'))
    print("Duration:", content_details.get('duration', 'N/A'))
    print("Caption:", content_details.get('caption', 'N/A'))
    print("Definition:", content_details.get('definition', 'N/A'))
    print("Licensed Content:", content_details.get('licensedContent', 'N/A'))
    print("Video Tags:", snippet.get('tags', []))

# Function to calculate and print video ratios
def calculate_and_print_video_ratios(statistics, video_id):
    """
    Calculate and print video ratios such as view-like, view-dislike, like-dislike, and comment ratios.
    
    Args:
        statistics (dict): Statistics of the video.
        video_id (str): The ID of the video.
    """
    views = int(statistics.get('viewCount', 0))
    likes = int(statistics.get('likeCount', 0))
    dislikes = int(get_dislike_count(video_id))
    comments = int(statistics.get('commentCount', 'N/A'))
    
    if views > 0:
        # Calculate ratios
        view_like_ratio = (likes / views) * 100
        view_dislike_ratio = (dislikes / views) * 100
        like_dislike_ratio = (dislikes / likes) * 100
        view_comment_ratio = (comments / views) * 100
        
        # Display ratios
        print(f"View-Like Ratio: {view_like_ratio:.2f}%")
        print(f"View-Dislike Ratio: {view_dislike_ratio:.2f}%")
        print(f"Like-Dislike Ratio: {like_dislike_ratio:.2f}%")
        print(f"Comment Ratio: {view_comment_ratio:.2f}%")
    else:
        print("Insufficient data to calculate ratios.")

# Function to get dislike count from third-party provider
def get_dislike_count(video_id):
    """
    Fetch dislike count for a video using a third-party provider.
    
    Args:
        video_id (str): The ID of the video.
    
    Returns:
        int: The dislike count of the video, or 'N/A' if not available.
    """
    dislike_api_url = f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
    response = requests.get(dislike_api_url)
    dislike_data = response.json()
    return dislike_data.get('dislikes', 'N/A')

# Function to fetch and display channel data
def fetch_and_display_channel_data(channel_id):
    """
    Fetch and display channel data based on channel ID.
    
    Args:
        channel_id (str): The ID of the channel.
    """
    # Define API request parts for channel data
    part_types = 'contentDetails,snippet,statistics,brandingSettings'
    
    # Make the API request to fetch channel data
    channel_request = youtube.channels().list(part=part_types, id=channel_id)
    channel_response = channel_request.execute()
    
    # Check if channel data is available
    if not channel_response['items']:
        print("No data available for the provided channel ID.")
        return
    
    # Extract channel data
    channel_data = channel_response['items'][0]
    content_details = channel_data['contentDetails']
    snippet = channel_data['snippet']
    statistics = channel_data['statistics']
    branding_settings = channel_data['brandingSettings']

    # Display channel data
    print_channel_data(snippet, statistics, branding_settings,channel_id)

# Function to print channel data
def print_channel_data(snippet, statistics, branding_settings,channel_id):
    """
    Print channel data including title, publication date, thumbnail, subscribers, views, videos, country, keywords, custom URL, and banner image.
    
    Args:
        snippet (dict): Channel snippet containing metadata.
        statistics (dict): Statistics of the channel.
        branding_settings (dict): Branding settings of the channel.
    """
    print("Channel Data For:", channel_id)
    print("Channel Title:", snippet.get('title', 'N/A'))
    print("Channel Published At:", snippet.get('publishedAt', 'N/A'))
    print("Channel Thumbnail:", snippet['thumbnails']['high'].get('url', 'N/A'))
    print("Subscribers:", statistics.get('subscriberCount', 'N/A'))
    print("Views:", statistics.get('viewCount', 'N/A'))
    print("Videos:", statistics.get('videoCount', 'N/A'))
    print("Country:", snippet.get('country', 'N/A'))
    print("Channel Keywords:", snippet.get('keywords', []))
    print("Custom URL:", snippet.get('customUrl', 'N/A'))
    print("Banner Image:", branding_settings['image'].get('bannerExternalUrl', 'N/A'))

# Main function
def main():
    """
    Main function to fetch video and channel data.
    """
    # Define video ID (can be made into a function parameter for flexibility)
    video_id = 'erLbbextvlY'  # Replace with your video ID
    
    # Fetch video data and display it
    channel_id = fetch_video_data(video_id)
    
    # If a valid channel ID is found, fetch and display channel data
    if channel_id != 'N/A':
        fetch_and_display_channel_data(channel_id)

# Run the main function
if __name__ == "__main__":
    main()
