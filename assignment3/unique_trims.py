import MapReduce
import sys

"""
assymetric Friendship Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    unique_id = record[0]
    seq = record[1][0:-10]
    mr.emit_intermediate(seq, 1)

    
def reducer(key, list_of_values):
    # key: seq
    # value: list of 1 
    mr.emit(key)
    #else:
    #    print "NO",key,list_of_values

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
