# © 2025 Fr0zst. All rights reserved. 
# Unauthorized copying prohibited.
import os
import subprocess

def download_song_from_spotify(spotify_link):
    """
    Downloads a song from a Spotify URL using spotDL.
    The downloaded file is placed in the user's default downloads directory.
    """
    try:
        # Determine the user's default downloads folder
        download_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
        
        if not os.path.exists(download_folder):
            print(f"Downloads folder not found. Using current directory: {os.getcwd()}")
            download_folder = os.getcwd()

        print(f"Attempting to download song to: {download_folder}")

        # Construct the spotDL command
        command = ['spotdl', spotify_link, '--output', download_folder]

        # Run the command in a subprocess
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        print("\n--- Download Success ---")
        print(result.stdout)
        print(f"Check your '{download_folder}' folder for the downloaded song.")

    except subprocess.CalledProcessError as e:
        print("\n--- Download Error ---")
        print(f"An error occurred while downloading the song: {e.stderr}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    # Display header
    print("\033[1mSpotify Mp3 Converter\033[0m")  # Bold text
    print("Made By Fr0zst\n")  # Normal text
    
    link = input("Please enter the Spotify song URL: ")
    if link:
        download_song_from_spotify(link)
    else:
        print("No Spotify link was entered.")

