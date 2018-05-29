'''
calculates features for a given file
'''

import pandas as pd

class FeatureCalculator:
    def __init__(self, source_file):
        self.source_file = source_file
        self.data = pd.read_csv(source_file, skip_blank_lines=True)
        self.SEQ = 'seq'


    def set_sequence_column(self, seq):
        self.SEQ = seq


    def save_features(self, columns=[]):
        '''
        exports all data with features to a new file
        '''
        if not columns:
            columns = self.data.columns.tolist()

        feature_file = self.source_file+"._features"
        self.data.to_csv(feature_file, sep=',', columns=columns)
        print("Saved to " + feature_file)


    def gc_content(self):
        '''
        feature: adds gc_content attribute
        '''
        def calc(seq):
            g = seq.count('G')
            c = seq.count('C')
            return ( (g+c) / len(seq) ) * 100

        self.data['gc_content'] = self.data[self.SEQ].apply(calc)
        return self.data
