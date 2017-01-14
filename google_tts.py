"""
Assumes a working internet connection.
"""
from io import BytesIO
import gossip
from gtts import gTTS
from eva import log

@gossip.register('eva.text_to_speech', provides=['google_tts'])
def text_to_speech(context):
    try:
        tts = gTTS(context.get_output_text())
        output = BytesIO()
        tts.write_to_fp(output)
        context.set_output_audio(output.getvalue(), 'audio/mpeg')
        output.close()
    except:
        log.error('Could not convert text to speech with google_tts')
