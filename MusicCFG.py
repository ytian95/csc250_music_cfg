import re
import random

class MusicCFG():
    def __init__(self):
        '''Initialize a grammar with rules for generating music in D Major
        '''

        self.grammar = {
            'S': ['I'],
            'I': ['I\' I\' I\' I\' ii', 'I\' I\' I\' I\' iii', 'I\' I\' I\' I\' IV', 'I\' I\' I\' I\' V', 'I\' I\' I\' I\' vi', 'I\' I\' I\' I\' I', 'I\' I\' I\' I\''],
            'ii': ['ii\' ii\' ii\' ii\' V', 'ii\' ii\' ii\' ii\' vi'],
            'iii': ['iii\' iii\' iii\' iii\' IV', 'iii\' iii\' iii\' iii\' vi'],
            'IV': ['IV\' IV\' IV\' IV\' I', 'IV\' IV\' IV\' IV\' ii', 'IV\' IV\' IV\' IV\' V'],
            'V': ['V\' V\' V\' V\' vi'],
            'vi': ['vi\' vi\' vi\' vi\' ii', 'vi\' vi\' vi\' vi\' iii', 'vi\' vi\' vi\' vi\' IV', 'vi\' vi\' vi\' vi\' V'],
            'I\'': ['D','F#', 'A'],
            'ii\'': ['E', 'G', 'B'],
            'iii\'': ['F#', 'A', 'C#'],
            'IV\'': ['G', 'B', 'D'],
            'V\'': ['A', 'C#', 'E'],
            'vi\'': ['B', 'D', 'F#'],
            'D': ['D_4', 'D_5'],
            'E': ['E_4', 'E_5'],
            'F#': ['F#_4', 'F#_5'],
            'G': ['G_3', 'G_4', 'G_5'],
            'A': ['A_4', 'A_5'],
            'B': ['B_4', 'B_5'],
            'C#': ['C#_4', 'C#_5']
            };

        self.chords = [];

    def genMusic(self, symbol):
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
    






    
