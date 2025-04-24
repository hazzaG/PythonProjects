import pygame
import numpy
import math
import time
import threading

pygame.init()
pygame.mixer.init()

bits = 16
sample_rate = 44100
pygame.mixer.pre_init(sample_rate, bits)

def sine_x(amp, freq, time, phase=0):
    return int(round(amp * math.sin((2 * math.pi * freq * time)+phase)))

class Tone:
    def sine(freq, phase=0, duration=1, speaker=None):
        
        num_samples = int(round(duration * sample_rate))

        sound_buffer = numpy.zeros((num_samples, 2), dtype = numpy.int16)

        amplitude = 2 ** (bits - 1) -1


        for sample_num in range(num_samples):




            t =  float(sample_num) / sample_rate

            sine = sine_x(amplitude, freq, t, phase)
        
            if speaker == "r":
                sound_buffer[sample_num][1] = sine
            if speaker == "l":
                sound_buffer[sample_num][0] = sine
            else:
                sound_buffer[sample_num][1] = sine
                sound_buffer[sample_num][0] = sine
        
        phase = (((math.asin((sine)/44100))/amplitude) + (2 * math.pi * freq * t))%360
        #print(phase)

        sound = pygame.sndarray.make_sound(sound_buffer)
        sound.play(loops=1, maxtime=int(duration * 1000))
        #time.sleep(duration)
        """
        if pygame.mixer.Sound.get_volume(sound) > 0.99 and pygame.mixer.Sound.get_volume(sound) > 0.06:
            while sound.get_volume():
                sound.set_volume(sound.get_volume()-0.005)
                pygame.time.wait(5)
                #print(pygame.mixer.Sound.get_volume(sound))
        # to avoid pop-in/pop-out by not fading in/out the begining and ending out a sound: https://stackoverflow.com/questions/32435091/prevent-popping-at-end-of-sound-in-pygame-mixer
        pygame.mixer.Sound.set_volume(sound,0.05)
        if pygame.mixer.Sound.get_volume(sound) < 0.99:
            while sound.get_volume():
                sound.set_volume(sound.get_volume()+0.005)
                pygame.time.wait(1)
        """
        return phase
        # this crackling might just be solveable I hope, something to do with the phase, found it here: https://stackoverflow.com/questions/42192239/remove-control-clicking-sound-using-pyaudio-as-an-oscillator
        # might have to rewrite this class or make a new one

        
    @staticmethod
    def create_tone_from_list(freq_list, duration=1, speaker=None):
        freq_threads = []
        for freq in freq_list:
            freq_thread = threading.Thread(target=Tone.sine, args=[freq, duration, speaker])
            freq_threads.append(freq_thread)

        for freq_thread in freq_threads:
            freq_thread.start()

        for freq_thread in freq_threads:
            freq_thread.join