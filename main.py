from pydub import AudioSegment

beat = AudioSegment.from_wav("beat.wav")
sax = AudioSegment.from_wav("sax.wav")

reversed_sax = sax.reverse()
reversed_sax.export("sax_reversed.wav")

print(len(beat), len(sax))

beat2 = beat * 2
beat2.export('beat2.wav')

mixed = beat2.overlay(sax)
mixed.export('mixed.wav')

final = beat + beat2 + mixed * 2 + reversed_sax + sax
final.export('final_audio.wav')


