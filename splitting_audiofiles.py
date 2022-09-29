# Import necessary libraries
from pydub import AudioSegment
  
# Input audio file to be sliced
audio = AudioSegment.from_wav("lisa_ekhart.wav")
  
'''
Slicing the audio file into smaller chunks with overlapping
'''
# Length of the audiofile in milliseconds
n = len(audio)
  
# Variable to count the number of sliced chunks
counter = 1
   
# Interval length at which to slice the audio file.
# as length is 4411520 seconds, and interval is 100 seconds,

# it splits the audio to 30 sec with 1 sec overalap
interval = 30 * 1000
overlap = 1 * 1000

# Initialize start and end seconds to 0
start = 0
end = 0
# Flag to keep track of end of file.
# When audio reaches its end, flag is set to 1 and we break
flag = 0

# Iterate from 0 to end of the file,
# with increment = interval
for i in range(0, 2 * n, interval):

    # During first iteration,
    # start is 0, end is the interval
    if i == 0:
        start = 0
        end = interval

    # All other iterations,
    # start is the previous end - overlap
    # end becomes end + interval
    else:
        start = end - overlap
        end = start + interval

    # When end becomes greater than the file length,
    # end is set to the file length
    # flag is set to 1 to indicate break.
    if end >= n:
        end = n
        flag = 1

    # Storing audio file from the defined start to end
    chunk = audio[start:end]

    # Filename / Path to store the sliced audio
    filename = 'chunk'+str(counter)+'.wav'

    # Store the sliced audio file to the defined path
    chunk.export(filename, format ="wav")
    # Print information about the current chunk
    print("Processing chunk "+str(counter)+". Start = "
                        +str(start)+" end = "+str(end))

    # Increment counter for the next chunk
    counter = counter + 1

    # Slicing of the audio file is done.
    

