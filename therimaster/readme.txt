This project intended to turn a T.16000M FCS Hotas Thrustmaster joystick and throttle into a musical instrument of sorts.
Unfortunately, the limits digital signal when compared to analogue have resulted in an annoying background noise that ruins the overall effect.
The main issue is that I am currently unable to prevent the audio signal from dropping to zero between discrete tones. This causes a popping sound and when wishing to switch between tones 100 times a second this will cause a constant tone of 100Hz.
A workaround for this could be to record the input to a wav file and play continuously from there, however this defeats the point of this program playing sound at runtime.
The fix for this seems to be beyond my knowledge for now despite much searching. I have learned a fair amount about pygame, signal processing and sound from this project. 
