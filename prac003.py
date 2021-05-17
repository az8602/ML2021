import numpy as np
import pandas as pd

raw_data={'name':['kevin','sally','hoyeon','lux'],
          'height':[178.2,162.9,160.6,156.2],
          'gender':['male','female','female',None]}
pd_data=pd.DataFrame(raw_data)
pd_data.head()