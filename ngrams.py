import data_reader
from collections import Counter

def main():
  histories = data_reader.get_bash_histories()
  NGRAM = 4
  for h in histories:
    ngrams = []  
    ngrams.append(zip(*(h.cmds[i:] for i in range(NGRAM))))
    counter = Counter(ngrams[0])
    sorted_ngrams = sorted(counter, key=counter.get, reverse=True)
    
    print '============BASH HISTORY ' + h.name + ' ==================='
    for n in sorted_ngrams:
      print 'NGRAM: ' + str(n) + ' Count: ' + str(counter[n])
    print '============BASH HISTORY END==================='
    print '\n'

if __name__ == '__main__':
  main()