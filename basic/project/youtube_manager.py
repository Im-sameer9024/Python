
import json

def load_data():
    try:
        with open("youtube.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def list_all_videos(videos):
    pass

def add_video(video):
    pass

def update_video(video):
    pass

def delete_video(video_id):
    pass

while True:
    print("\n YouTube Manager")
    print("1. Add Video")
    print("2. Update Video")
    print("3. Delete Video")
    print("4. Exit")
    choice = input("Enter your choice: ")

    match choice:
        case '1':
            print("Adding a new video...")
            # Code to add video
            add_video([])
        case '2':
            print("Updating an existing video...")
            # Code to update video
            update_video([])

        case '3':
            print("Deleting a video...")
            # Code to delete video
            delete_video()
        case '4':
            print("Exiting the YouTube Manager. Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")