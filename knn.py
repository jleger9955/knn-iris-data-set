from collections import defaultdict


class Knn:

    def __init__(self):
        self.vectors = []
        self.species = []

    def train(self, vector, species):
        self.vectors.append(vector)
        self.species.append(species)

    def predict(self, vector, k):
        lengths = [(vector.scale(-1) + v).norm() for v in self.vectors]
        lenspec = [(length, self.species[i]) for i, length in enumerate(lengths)]
        final = sorted(lenspec, key=lambda t: t[0])[:k]
        prediction = final[0][1]
        ''' The code below is only needed if you expect more than one species in the "final" list variable
        count_spec = defaultdict(int)
        for spc in final:
            count_spec[spc[1]] += 1
        prediction = ''
        for spc, cnt in count_spec.items():
            if count_spec[spc] >= 2:
                prediction = spc
        '''
        return prediction
