# YoutubeVidsInSpotify
### Description:
A Python script that allows you to download an album from YouTube and split it up into songs, using a timestamps file as a reference.

### Usage:
Pretty simple to use, all that's required is to have installed ffmpeg and set up a ```timestamps.txt``` file. The ```timestamps.txt``` file has a very specific format (sorry but I didn't know / couldn't be asked to create a general timestamp format so I've just made up a convention) so be careful when creating the file. Once the file has been created according to the format below, the program will prompt you for the URL of the YouTube Video, a destination folder (choose either downloads or music, Spotify kinda bugs out, or at least it did for me unless I added it to downloads) and the location of your ```timestamps.txt``` file. It will then begin the download of the YouTube video. It will download the whole thing as an audio-only ```.mp3``` file which will later be deleted. The splitting will then begin according to the specified time stamps in the ```timestamps.txt``` file and will be stored in the previously specified destination folder. They will be stored as ```.aac``` files (which are basically just space-efficient audio files that are still able to be read by Spotify) and the original ```.mp3``` file will be deleted. The files should then appear in the `Local Files` section of your Spotify account.

### Format of the ```timestamps.txt``` file:
Once again, really important to get this right. The format is as follows:

**```"number". "title" "time"```**


where number is the track number, title is the track title and time is the timestamp in HH:MM:SS format.
**NOTE: THE FULL STOP AFTER ```number``` IS REALLY IMPORTANT**

### Examples of valid ```timestamps.txt``` file formatting:
1. The Black Tower (Oracle of Seasons & Ages) 1:30
2. Zora Village (Oracle of Seasons & Ages) 3:06
3. Church (A Link to the Past) 4:24
4. Dancing Dragon Dungeon (Oracle of Seasons & Ages) 5:57
5. End Credits (Oracle of Seasons & Ages) 8:00
6. Cave (A Link to the Past) 10:01
7. Dungeon (The Legend of Zelda) 11:01
8. Hyrule Castle (A Link to the Past) 12:10
9. Guardian Battle (Breath of the Wild) 15:05
10. Chamber of the Sages (Ocarina of Time) 18:42
11. Tarm Ruins (Oracle of Seasons & Ages) 20:26
12. Title Screen (Zelda II The Adventure of Link) 22:22
...

**NOTE: THE FULL STOP AFTER ```number``` IS REALLY IMPORTANT**

I'm kinda new to this so this was a lot of chatGPT/ messy code so if anyone spots any bugs you are free to improve the code however you want, just let me know if you make any cool changes. Thanks for reading!

> NOTE: It's normal for it to run for a decently long time, I downloaded and split videos that were 4 hours long in around 5ish mins so dont worry it will work.

> NOTE: chatGPT can create the ```timestamps.txt``` file for you if you ask it to match the specified format and give it the timestamps from the YouTube vid.

> NOTE: Idk how to turn into an exe file so I've just put the whole code up (I'm saying it like someone will actually use this lol) 

