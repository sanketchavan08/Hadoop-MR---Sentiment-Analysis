from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_REGEXP = re.compile(r"[\w']+")

class MRWordFrequencyCount(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_words,
                   reducer=self.reducer_count_words),
            MRStep(mapper=self.mapper_make_counts_key,
                   reducer = self.reducer_output_words)
        ]

    def mapper_get_words(self, _, line):
        x = ('few', 'may', 'must', 'none', 'whole', 'here', 'against', 'toward', 'ourselves', 'and', 'he', 'themselves', 'but', 
        'anywhere', 'one', 'used', 'often', 'him', 'been', 'the', 'take', 'my', 'anyhow', 'unless', 'please', 'never', 'however', 'same', 
        'throughout', 'too', 'whence', 'third', 'sometimes', 'until', 'into', 'if', 'most', 'namely', 'put', 'empty', 'along', 'each', 'his', 
        'amongst', 'perhaps', 'then', 'quite', 'something', 'due', 'nowhere', 'least', 'much', 'an', 'for', 'elsewhere', 'these', 'various', 
        'two', 'whether', 'nine', 'whenever', 'well', 'else', 'name', 'now', 'other', 'twelve', 'nothing', 'so', 'four', 'onto', 'through', 
        'could', 'might', 'its', 'next', 'will', 'seems', 'whereupon', 'is', 'beyond', 'someone', 'meanwhile', 'noone', 'they', 'hundred', 
        'fifteen', 'it', 'top', 'twenty', 'doing', 'any', 'being', 'again', 'latterly', 'anything', 'how', 'thus', 'thereafter', 'were', 
        'several', 'before', 'whoever', 'we', 'me', 'whereafter', 'back', 'behind', 'that', 'i', 'from', 'keep', 'mostly', 'thereupon', 
        'except', 'together', 'anyway', 'hereafter', 'seem', 'every', 'in', 'no', 'be', 'cannot', 'also', 'thereby', 'had', 'out', 'are', 
        'off', 'others', 'seeming', 'to', 'us', 'whereby', 'am', 'side', 'first', 'whom', 'can', 'afterwards', 'alone', 'between', 'last',
        'own', 'beforehand', 'around', 'more', 'some', 'say', 'all', 'just', 'therefore', 'whither', 'under', 'latter', 'which', 'a', 'there', 
        'via', 'somehow', 'amount', 'becoming', 'both', 'give', 'at', 'did', 'nobody', 'anyone', 'or', 'somewhere', 'get', 'done', 'front', 'was', 
        'why', 'where', 'such', 'after', 'should', 'bottom', 'hereby', 'towards', 'your', 'otherwise', 'without', 'yourselves', 'seemed', 'ten', 
        'neither', 'thru', 'always', 'formerly', 'eight', 'those', 'rather', 'therein', 'fifty', 'former', 'hence', 'really', 'during', 'as', 
        'nevertheless', 'less', 'not', 'using', 'ca', 'hereupon', 'show', 'since', 'forty', 'while', 'everyone', 'down', 'everything', 'six', 
        'wherein', 'many', 'what', 'herein', 'himself', 'among', 'she', 'though', 'move', 'with', 'herself', 'by', 'very', 'make', 'when', 'about', 
        'ours', 'wherever', 'whose', 'moreover', 'see', 'up', 'have', 'made', 'sixty', 'call', 'thence', 'this', 'mine', 'of', 'besides', 'myself', 
        'over', 'becomes', 'do', 'either', 'once', 'yet', 'yours', 'has', 'their', 'became', 'full', 'become', 'would', 'part', 'nor', 'yourself', 
        'them', 'above', 'who', 'still', 'regarding', 'itself', 'than', 'within', 'because', 'below', 'already', 'beside', 'serious', 'you', 'another', 
        'her', 'hers', 'indeed', 'per', 'further', 'sometime', 'ever', 'across', 'although', 'upon', 'whereas', 'does', 'go', 'whatever', 'even', 'only', 
        'our', 'enough', 're', 'three', 'five', 'everywhere', 'almost', 'eleven', 'on', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "it's", "we'll", '00bd', '00a0', 'rt', 'ok', 'https','ed','00b3','00b7', 'co')
        
        
        words = WORD_REGEXP.findall(line)
        
        for word in words:
            word = word.lower()
            if word not in x:
                yield word, 1
                
                

    def reducer_count_words(self, word, values):
        s = sum(values)
        if s > 11:
           yield word, s
        

    def mapper_make_counts_key(self, word, count):
        yield '%04d'%int(count), word

    def reducer_output_words(self, count, words):
        for word in words:
            #yield count, word
            print(count + '  ' + word, end ="\n")

if __name__ == '__main__':
    MRWordFrequencyCount.run()
