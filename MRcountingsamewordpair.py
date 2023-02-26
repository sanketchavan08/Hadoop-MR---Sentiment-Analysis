from mrjob.job import MRJob
from mrjob.step import MRStep

class MRcountingsamewordpair(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                   reducer=self.reducer),
            MRStep(mapper=self.mapper_2,
                   reducer = self.reducer_2)
        ]
        
    def mapper(self, key, line):
        (word_1,word_2,value) = line.split()
        yield word_1 + ' - ' + word_2, 1
        
    def reducer(self, wordpair, count):
        yield wordpair, sum(count) 
        
    def mapper_2(self, wordpair, countTotal):
        yield float(countTotal), wordpair
        
    def reducer_2(self, countTotal, wordpairs):
        for wordpair in wordpairs:
        
            
             #yield wordpair, countTotal 
             print (wordpair + '  ' + '%04d'%int(countTotal)) 
    
        
                
if __name__ == '__main__':
    MRcountingsamewordpair.run()                