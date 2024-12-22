from pytubefix import YouTube
import os
import ffmpeg
from tkinter import filedialog
import time

def main(): 
    start = time.perf_counter()

    try:
        url = input("Video URL that you want to download: ")
        print("select output destination folder")
        output_filepath = filedialog.askdirectory(title="Select output destination")
        print("select the timestamps txt file")
        txt_file_path =  filedialog.askopenfilename(title="Select the txt file",filetypes=[("Text Files" , "*.txt")]) 

        print("downloading...")    
        file_name = downloader(url,output_filepath)
        file_path = output_filepath + "/" +file_name + ".mp3"
        
    except:
        print("something went wrong bud")
    else:
        print("done")
        print("splitting into smaller parts...")
        split_file_by_timestamps(file_path,txt_file_path,output_filepath) 
        print("done")
        print("removing large mp3 file...")
        os.remove(file_path)
        end = time.perf_counter()
        time_taken = end-start
        print("removed!")
        print(f"Program completed in {time_taken}s!")
    
def downloader(input_URL: str , path: str) -> str:
    '''
    Downloads an AUDIO ONLY version of the specified Youtube Video URL to a specified path
    
        Parameters:
            input_URL (str): Input URL of any Youtube Video
            path (str): Output path of where to place the downloaded audio mp3
        
        Returns:
            Downloaded file's file name, also downloads the file
    '''
    yt = YouTube(input_URL)
    yt.streams.get_audio_only().download(mp3=True,output_path=path)
    return yt.title

def extract_start_time(line):
    """
    Extracts the start time from the timestamp line in the format '100 - Hyrule Castle TP 0:00'.
    Returns the start time in HH:MM:SS format.
    """
    parts = line.strip().split()
    # The last part should be the time (e.g., '0:00', '1:43', etc.)

    
    return parts[-1]

def get_file_duration(input_file):
    """
    Gets the total duration of the media file using FFmpeg.
    Returns the duration in seconds.
    """
    try:
        # Get the duration in seconds
        probe = ffmpeg.probe(input_file, v='error', show_entries='stream=duration')
        duration = int(float(probe['streams'][0]['duration']))
        
        hours = int(duration // 3600)
        minutes = int((duration - 3600*hours) // 60)
        seconds = int(duration - 3600*hours - 60*minutes)

        return hours,minutes,seconds
    except ffmpeg.Error as e:
        print(f"Error retrieving file duration: {e}")
        return None

def split_file_by_timestamps(input_file, timestamps_file,output_path):
    """
    Splits a media file into smaller files based on timestamps provided in a text file.
    
    Parameters:
        input_file (str): Path to the input media file (e.g., mp4, mp3).
        timestamps_file (str): Path to the text file containing the timestamps.
        output_prefix (str): Prefix for the output files.
    """


    try:
        end_of_file = get_file_duration(input_file)
        final_time = str(end_of_file[0]) + ":" + str(end_of_file[1]) +":"+ str(end_of_file[2])
        
        with open(timestamps_file, 'r') as file:
            lines = file.readlines()
            for idx in range(len(lines)):
                _,second_part = lines[idx].split(".")
                titleish = second_part.split(':')[0]
                title = titleish[0:len(titleish)-2]

                # Process each line and extract the timestamps
                start_time = extract_start_time(lines[idx])  # Current start time
                if start_time == extract_start_time(lines[-1]):
                    end_time = final_time
                else:
                    end_time = extract_start_time(lines[idx + 1])  # Start time of next segment

                output_file = f"{output_path}/{idx+1}{title}.aac"  # Change the extension as needed

                # Use FFmpeg to split the file based on start and end times
                ffmpeg.input(input_file, ss=start_time, to=end_time).output(output_file,acodec = "aac").run(overwrite_output=True)
                print(f"Segment {idx + 1} saved as {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

            


    
if __name__ == "__main__":
    ans = input("is the timestamps.txt file updated for this video (check code)? (y/n) ")
    if ans == 'y':
        main()
    elif ans == 'n':
        print("update timestamps.txt")
