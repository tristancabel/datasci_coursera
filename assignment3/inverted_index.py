import MapReduce
import sys

"""
Inverted index Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document contents
    # value: document identifier
    value = record[0]
    key = record[1]
    words_list = []
    words = key.split()
    for w in words:
      if w not in words_list:
          words_list.append(w)
          mr.emit_intermediate(w, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of documents
    # total = 0
    #for v in list_of_values:
    #  total += v
    mr.emit((key, list_of_values))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
