from kakao_dictation import *
from pyaudio_record import *
import io


audio_data = record(5) #녹음 데이터 리스트

# file_name = 'test.wav'
# save_wav(filename,sudio_data)
# f=open(file_name, 'rb')
# audio_data = f.read()

audio_stream= io.BytesIO()
save_wav(audio_stream,audio_data)

result = dictation(audio_stream,getvalue())
print('인식결과',result)
