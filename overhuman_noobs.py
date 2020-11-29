import pandas as pd
import numpy as np

from natasha import (
    MorphVocab,
    DatesExtractor
)

data = pd.read_table('/content/overhumanized-dev-fp.tsv')


vocab = MorphVocab()
extractor = DatesExtractor(vocab)

result_data = []

def get_date_from_string(s):
    res = []
    matches = [x for x in extractor(s)]
    for mch in matches:
        result = ""
        y = mch.__dict__['fact'].__dict__['year']
   #     m = mch.__dict__['fact'].__dict__['month']
    #    d = mch.__dict__['fact'].__dict__['day']
        
        if y is not None:
            result += str(y)
     #       if m is not None:
      #          if m//10 == 0:
       #             result += "-0"+str(m)
        #        else: 
         #           result += "-"+str(m)
          #      if d is not None:
           #         if d//10 == 0:
            #              result += "-0"+str(d)
             #       else:
              #          result += "-"+str(d)
        res.append(result)
    return res
        

for i in range(len(data)):
    res = get_date_from_string(data.iloc[i,1])
    result_concat = " - ".join(res)
 #   result_data.append((result_concat))
    result_data.append((data.iloc[i,1], result_concat))
    
#df_submit = pd.DataFrame(result_data)
df_submit = pd.DataFrame(result_data, columns=["Id", "Expected"])
print(df_submit.head(10))
df_submit.to_csv("submission.tsv", index=False)
