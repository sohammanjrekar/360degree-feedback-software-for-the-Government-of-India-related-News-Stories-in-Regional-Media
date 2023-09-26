import os
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the YouTube Data API version
API_VERSION = 'v3'

# Define the OAuth2 scopes required for the YouTube Data API
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def authenticate_with_oauth2():
    # Initialize the OAuth2 flow
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json',  # Path to your client secret JSON file
        SCOPES
    )

    # Run the OAuth2 flow to obtain credentials
    credentials = flow.run_local_server(port=0)

    # Build the YouTube Data API client with the authenticated credentials
    youtube = build('youtube', API_VERSION, credentials=credentials)
    
    return youtube

def get_caption_data(youtube, video_id):
    # Retrieve the closed captioning data for the video
    captions = youtube.captions().list(
        part="snippet",
        videoId=video_id
    ).execute()

    # Extract the caption tracks
    caption_tracks = captions.get("items", [])

    if not caption_tracks:
        print("No caption tracks found for the video.")
    else:
        print(f"Found {len(caption_tracks)} caption track(s) for the video:")
        for track in caption_tracks:
            print(f"Caption Track ID: {track['id']}")
            print(f"Language: {track['snippet']['language']}")
            print(f"Kind: {track['snippet']['trackKind']}")
            print(f"Status: {track['snippet']['status']}")

if __name__ == "__main__":
    # Define the YouTube video ID you want to analyze
    video_id = "liJVSwOiiwg"  # Replace with your desired video ID

    # Authenticate using OAuth2
    youtube = authenticate_with_oauth2()

    # Get caption data for the video
    get_caption_data(youtube, video_id)
