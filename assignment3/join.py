import MapReduce
import sys

"""
Relational join Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    table = record[0]
    order_id = record[1]
    mr.emit_intermediate(order_id, record)
    
def reducer(key, list_of_values):
    # key: order
    # value: (table, data)
    id_order=0
    id_items=[]    
    for idx,record in enumerate(list_of_values):
        if(record[0] ==  "order"):
            id_order=idx;
        elif(record[0] == "line_item"):
            id_items.append(idx);

    for id_item in id_items:
        data_out = []
        order = list_of_values[id_order]
        for i in range(10):
            data_out.append(order[i])
        item = list_of_values[id_item]
        for i in range(17):
            data_out.append(item[i])
        mr.emit(data_out)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
