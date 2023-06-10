import os
import eyed3
import yaml
import time

def format_duration(duration_in_seconds):
    hours = int(duration_in_seconds // 3600)
    minutes = int((duration_in_seconds % 3600) // 60)
    seconds = int(duration_in_seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Read the ID3 tags and creation time from an mp3 file
def read_id3_tags(audio_file_path):
    audio_file_id3 = eyed3.load(audio_file_path)
    title = audio_file_id3.tag.title
    duration = format_duration(audio_file_id3.info.time_secs)
    comments = "\n".join(comment.text for comment in audio_file_id3.tag.comments)
    file_size_in_bytes = os.path.getsize(audio_file_path)
    file_size_formatted = "{:,}".format(file_size_in_bytes)
    return title, duration, comments, file_size_formatted

# Read the audio folder and information in the saved files
def create_audio_list_from_files():
    audio_list = []
    for filename in os.listdir("./audio"):
        if filename.endswith(".mp3"):
            audio_file_path = os.path.join(os.path.abspath("./audio"), filename)
            title, duration, comments, file_size = read_id3_tags(audio_file_path)
            audio_list.append({
                "title": title,
                "description": comments,
                "file": "/audio/" + filename,
                "duration": duration,
                "length": file_size
            })
    return audio_list

# Read the ID3 tags from a list of audio files and output as YAML
audio_data = create_audio_list_from_files()

# Get the directory of the current Python file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create the audio_data.yaml file in the current directory
yaml_file_path = os.path.join(current_dir, "audio_data.yaml")
with open(yaml_file_path, "w") as f:
    yaml.dump(audio_data, f, default_flow_style=False, sort_keys=False)