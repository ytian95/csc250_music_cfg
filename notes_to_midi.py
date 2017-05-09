# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import midi
import sys

NOTES = {
        "A_1":midi.A_1, "B_1":midi.B_1, "C#_1":midi.Cs_1, 
        "D_1":midi.D_1, "E_1":midi.E_1, "F#_1":midi.Fs_1, "G_1":midi.G_1,
        "A_2":midi.A_2, "B_2":midi.B_2, "C#_2":midi.Cs_2, 
        "D_2":midi.D_2, "E_2":midi.E_2, "F#_2":midi.Fs_2, "G_2":midi.G_2,                
        "A_3":midi.A_3, "B_3":midi.B_3, "C#_3":midi.Cs_3, 
        "D_3":midi.D_3, "E_3":midi.E_3, "F#_3":midi.Fs_3, "G_3":midi.G_3,
        "A_4":midi.A_4, "B_4":midi.B_4, "C#_4":midi.Cs_4, 
        "D_4":midi.D_4, "E_4":midi.E_4, "F#_4":midi.Fs_4, "G_4":midi.G_4,
        "A_5":midi.A_5, "B_5":midi.B_5, "C#_5":midi.Cs_5, 
        "D_5":midi.D_5, "E_5":midi.E_5, "F#_5":midi.Fs_5, "G_5":midi.G_5,
        }
CHORDS = {
        "I"  : ("D_2", "F#_2", "A_3"),
        "ii" : ("E_2", "G_2", "B_3"),
        "iii": ("F#_2", "A_3", "C#_3"),
        "IV" : ("G_2", "B_3", "D_3"),
        "V"  : ("A_3", "C#_3", "E_3"),
        "vi" : ("B_3", "D_3", "F#_3")
        }
def main():
    note_file_name = sys.argv[1]
    #chord_file_name = sys.argv[2]
    pattern = midi.Pattern()
    
    with open(note_file_name, "r") as f:
        read = f.read()
        notes = read.strip().split(" ")
        track = midi.Track()
        pattern.append(track)
        i = 0
        for note in notes:
            on = midi.NoteOnEvent(tick=(0), velocity=75, pitch=NOTES[note])
            track.append(on)
            off = midi.NoteOffEvent(tick=(100), pitch=NOTES[note])
            track.append(off)
            i += 1
    eot = midi.EndOfTrackEvent(tick=1)
    track.append(eot)
    """
    with open(chord_file_name, "r") as f:
        read = f.read()
        chords = read.strip().split(" ")
        tracks = [midi.Track(), midi.Track(), midi.Track()]
        for t in tracks: 
            pattern.append(t)

        for chord in chords:
            for note, t in zip(CHORDS[chord], tracks):
                on = midi.NoteOnEvent(tick=0, velocity=75, pitch=NOTES[note])
                t.append(on)
                off = midi.NoteOffEvent(tick=150*4, pitch=NOTES[note])
                t.append(off)
    """
        
    midi.write_midifile(note_file_name[:-4] + "_midi.mid", pattern)

main()