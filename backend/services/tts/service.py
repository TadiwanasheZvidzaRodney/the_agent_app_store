import logging

logger = logging.getLogger(__name__)

class TTSServiceStub:
    def __init__(self, voice_type: str = "default"):
        self.voice_type = voice_type
        
    def synthesize_speech(self, text: str, output_path: str):
        logger.info(f"Synthesizing speech with voice '{self.voice_type}' for text: {text}")
        pass

    def transcribe_speech(self, audio_path: str) -> str:
        logger.info(f"Transcribing audio from {audio_path}")
        return "This is a transcribed dummy text from voice note."
