"""
import pandas as pd
#创建一个空系列
s = pd.Series()
print(s)
"""
"""
#s=pd.Series(data,np.arange(4))
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s=pd.Series(data)#或者s=pd.Series(data,np.arange(4))
print(s)
"""
"""
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s=pd.Series(data,index=[1001,1002,1003,1004])
print(s)
"""
import pandas as pd
import numpy as np
data = {'a':1,'b':"abc",'c':3.5}
s=pd.Series(data)
print(s)