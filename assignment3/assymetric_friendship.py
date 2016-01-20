import MapReduce
import sys

"""
assymetric Friendship Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate((personA,personB), 1)
    mr.emit_intermediate((personB,personA), 0)
    
def reducer(key, list_of_values):
    # key: personA,personB
    # value: list of 1 or 0. 
    if (sum(list_of_values) == 0):
        mr.emit((key[0], key[1]))
    #else:
    #    print "NO",key,list_of_values

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
