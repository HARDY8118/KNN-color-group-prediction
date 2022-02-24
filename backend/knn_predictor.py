import tensorflow as tf
tf.get_logger().setLevel('WARNING')
import csv
import random
from collections import Counter
import re

class KNN_Predictor:
    
    groups = ['Pink','Purple','Red','Orange','Yellow','Green','Cyan','Blue','Brown','White',"Grey"]
    
    def __init__(this):
        this.__data = []
    
    def load_csv(this,filename,skip_header=False):
        try:
            _f = open(filename,'r')
            _reader = csv.reader(_f,delimiter=',')
            _data = []
            if skip_header:
                next(_reader)
            for row in _reader:
                _r, _g, _b = int(row[2].strip()), int(row[3].strip()), int(row[4].strip())
                _c = KNN_Predictor.groups.index(row[-1].strip())

                _data.append([_r, _g, _b, _c])
            _f.close()
            this.__data = tf.constant(_data)
            return True
        except Exception as e:
            print(e)
            return False
    
    @staticmethod
    def from_hex(h):
        h = str(h)
        if re.match("^(#)?[a-fA-F0-9]{6}$",h) is None:
            return None

        start_index = 0
        if h[0] == '#':
            start_index = 1
        return [
            int(h[start_index:start_index+2],16),
            int(h[start_index+2:start_index+4],16),
            int(h[start_index+4:start_index+6],16)
        ]
    
    def predic(this, color, k=5, sample_size=None, test_size=None):
        if type(color) == str:
            color = KNN_Predictor.from_hex(color)
        
        if color is None:
            return "Invalid color provided"
        
        if type(color) == list:
            if len(color) != 3:
                return "Invalid values provided"
            else:
                color = tf.constant(color)

        features = tf.gather(this.__data,[0,1,2],axis=1)
        labels = tf.gather(this.__data,[3],axis=1)

        diff = (features - color)
        diff_squared = diff**2
        sums = tf.reduce_sum(diff_squared,axis=1)
        sums = tf.reshape(sums,[-1,1])
        diff_squared_sum = tf.concat([sums,labels],axis=1)
        diff_squared_sum_sorted = sorted(diff_squared_sum.numpy().tolist(),key=lambda r:r[0])

        top_k = [_[1] for _ in diff_squared_sum_sorted[:k]]
        
        most_frequent = Counter(top_k).most_common(1) # get 1 of most frequent

        if 0<=most_frequent[0][0]<=10:
            return KNN_Predictor.groups[most_frequent[0][0]]
        return "Invalid output generated"
