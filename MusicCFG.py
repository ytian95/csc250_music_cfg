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
               Progressions:  p_I, p_ii, p_iii, p_IV, p_V, p_vi
               Chords (triads):  I, ii, iii, IV, V, vi
               Notes (name):  A, B, C#, D, E, F#, G

           Terminals:
               Notes (SPN):  Note_Octave
                   SPN (scientific pitch notation) is a method of specifying pitch
                   by combining a musical note name and a number identifying the note's octave
                       e.g. C_4 = middle C
        '''

        self.grammar = {
            'S': ['p_I'],
            'p_I': ['I I I I p_ii', 'I I I I p_iii', 'I I I I p_IV', 'I I I I p_V', 'I I I I p_vi', 'I I I I p_I', 'I I I I'],
            'p_ii': ['ii ii ii ii p_V', 'ii ii ii ii p_vi'],
            'p_iii': ['iii iii iii iii p_IV', 'iii iii iii iii p_vi'],
            'p_IV': ['IV IV IV IV p_I', 'IV IV IV IV p_ii', 'IV IV IV IV p_V'],
            'p_V': ['V V V V p_vi', 'V V V V p_I'],
            'p_vi': ['vi vi vi vi p_ii', 'vi vi vi vi p_iii', 'vi vi vi vi p_IV', 'vi vi vi vi p_V'],
            'I': ['D','F#', 'A'],
            'ii': ['E', 'G', 'B'],
            'iii': ['F#', 'A', 'C#'],
            'IV': ['G', 'B', 'D'],
            'V': ['A', 'C#', 'E'],
            'vi': ['B', 'D', 'F#'],
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
            if (sym == 'p_I' or sym == 'p_ii' or sym == 'p_iii' or sym == 'p_IV' or sym == 'p_V' or sym == 'p_vi'):
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
    






    
