import MapReduce
import sys

"""
Matrix multiplication Example in the Simple Python MapReduce Framework
assume max matrices 5x5
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    matrix = record[0]
    line = record[1]
    col = record[2]
    val = record[3]
    if (matrix == "a"):
        mr.emit_intermediate((line,0), (col,val))
        mr.emit_intermediate((line,1), (col,val))
        mr.emit_intermediate((line,2), (col,val))
        mr.emit_intermediate((line,3), (col,val))
        mr.emit_intermediate((line,4), (col,val))
    else:
        mr.emit_intermediate((0,col), (line ,val))
        mr.emit_intermediate((1,col), (line ,val))
        mr.emit_intermediate((2,col), (line ,val))
        mr.emit_intermediate((3,col), (line ,val))
        mr.emit_intermediate((4,col), (line ,val))

    
def reducer(key, list_of_values):
    # key: (line,col) of out
    # value: val of out
    res = 0
    val_list = [0]*5
    for couple in list_of_values:
        if val_list[couple[0]] != 0:
            res = res + couple[1]*val_list[couple[0]]
            val_list[couple[0]] = 0
        else:
            val_list[couple[0]]=couple[1]
            
    mr.emit((key[0], key[1], res))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
