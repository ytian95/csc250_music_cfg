# MusicCFG.py
#
# Stephanie Xie, Youyou Tian, Jackie Byun
# 05/12/2017
# CSC 250
#
# A program that creates a context-free grammar and generates musical notes over a D Major chord progression.

import re
import random

class MusicCFG():
    def __init__(self):
        '''Initialize a grammar with rules for the most common chord progressions in D Major

           Nonterminals:
               Progressions:  I, ii, iii, IV, V, vi
               Chords (triads):  I', ii', iii', IV', V', vi'
               Notes (name):  A, B, C#, D, E, F#, G

           Terminals:
               Notes (SPN):  Note_Octave
                   SPN (scientific pitch notation) is a method of specifying pitch
                   by combining a musical note name and a number identifying the note's octave
                       e.g. C_4 = middle C
        '''

        self.grammar = {
            'S': ['I'],
            'I': ['p_I p_I p_I p_I ii', 'p_I p_I p_I p_I iii', 'p_I p_I p_I p_I IV', 'p_I p_I p_I p_I V', 'p_I p_I p_I p_I vi', 'p_I p_I p_I p_I I', 'p_I p_I p_I p_I'],
            'ii': ['p_ii p_ii p_ii p_ii V', 'p_ii p_ii p_ii p_ii vi'],
            'iii': ['p_iii p_iii p_iii p_iii IV', 'p_iii p_iii p_iii p_iii vi'],
            'IV': ['p_IV p_IV p_IV p_IV I', 'p_IV p_IV p_IV p_IV ii', 'p_IV p_IV p_IV p_IV V'],
            'V': ['p_V p_V p_V p_V vi', 'p_V p_V p_V p_V I'],
            'vi': ['p_vi p_vi p_vi p_vi ii', 'p_vi p_vi p_vi p_vi iii', 'p_vi p_vi p_vi p_vi IV', 'p_vi p_vi p_vi p_vi V'],
            'p_I': ['D','F#', 'A'],
            'p_ii': ['E', 'G', 'B'],
            'p_iii': ['F#', 'A', 'C#'],
            'p_IV': ['G', 'B', 'D'],
            'p_V': ['A', 'C#', 'E'],
            'p_vi': ['B', 'D', 'F#'],
            'D': ['D_4', 'D_5'],
            'E': ['E_4', 'E_5'],
            'F#': ['F#_4', 'F#_5'],
            'G': ['G_3', 'G_4', 'G_5'],
            'A': ['A_4', 'A_5'],
            'B': ['B_4', 'B_5'],
            'C#': ['C#_4', 'C#_5']
            };

        self.chords = []; # list of chords generated

    def genMusic(self, symbol):
        '''Generate music using grammar
        '''
        
        music = '';
        symbols = random.choice(self.grammar[symbol]);
        for sym in symbols.split():
            if sym not in self.grammar:
                music += sym + ' ';
            else:
                music += self.genMusic(sym);
            if (sym == 'I' or sym == 'ii' or sym == 'iii' or sym == 'IV' or sym == 'V' or sym == 'vi'):
                self.chords.append(sym);

        return music;   

def main():
    m = MusicCFG();
    music = m.genMusic('S');
    f = open("musiccfg.txt", 'w');
    f.write(music + '\n');
    f.close();
    
    f = open("chords.txt", 'w');
    f.write(' '.join(m.chords));
    f.close();

main()
    






    
