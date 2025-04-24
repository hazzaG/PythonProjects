from utility import freq_map
from tone import Tone
import threading
import time

class Note:
    def __init__(self, note_str, duration=1):
        main_note = note_str[0].upper()
        self.note_str = main_note + note_str[1:]
        self.duration = duration
        self.freq = freq_map[self.note_str]

    def play(self, speaker=None):
        Tone.sine(self.freq, duration=self.duration, speaker=speaker)

    @staticmethod
    def rest(duration):
        time.sleep(duration)

    @staticmethod
    def play_chord(notes_list):
        note_threads = []

        for note in notes_list:
            note_thread = threading.Thread(target=note.play)
            note_threads.append(note_thread)

        for note_thread in note_threads:
            note_thread.start()

        for note_thread in note_threads:
            note_thread.join()

