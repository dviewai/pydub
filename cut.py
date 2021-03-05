from pydub import AudioSegment

file1 = r'C:\Work\per\start1\YeahToh_full.mp3'
file2 = r'C:\Work\per\start1\YeahTo_part2.mp3'
fileout = r'C:\Work\per\start1\YeahToh_final.mp3'

file4 = r'C:\Work\per\start1\Aania_Amishi_full.mp3'
fileout = r'C:\Users\amitk\Desktop\Anniversary\Aania_Amitshi_full.mp3'

file5 = r'C:\Work\per\start1\tu_meri_full.mp3'
file6 = r'C:\Work\per\start1\merey_hotho_full.mp3'
fileout = r'C:\Users\amitk\Desktop\Anniversary\amit_solo.mp3'
startMin = 0
startSec = 7

endMin = 0
endSec = 46

# Time to miliseconds
startTime = startMin*60*1000+startSec*1000
endTime = endMin*60*1000+endSec*1000

# Opening file and extracting segment
song = AudioSegment.from_mp3(file5)
extract1 = song[startTime:endTime]

#part2
startMin = 0
startSec = 0

endMin = 1
endSec = 10

# Time to miliseconds
startTime = startMin*60*1000+startSec*1000
endTime = endMin*60*1000+endSec*1000
song2 = AudioSegment.from_mp3(file6)
extract2 = song2[startTime:endTime]


final = extract1+extract2

# Saving
final.export( fileout, format="mp3")