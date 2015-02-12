def get_ngrams(cmds_list, n):
  return zip(*[cmds_list[i:] for i in range(n)])

def plot_ngram_cmds(bh):
  cmd_ngrams = get_ngrams(bh.cmds)
  ngram_counter = Counter(cmd_ngrams)
  for s in ngram_counter:
    ngram_counter[c] /= float(len(bh.cmds))

  plt.bar(range(0, len(ngram_counter.keys())), ngram_counter.values())
  plt.xlabel('Distinct Command Sequences')
  plt.ylabel('Normalised Counts of Distinct Command Sequences')
  plt.show()

def main():
  bash_histories = data_reader.get_bash_histories()

if __name__ == '__main__':
  main()