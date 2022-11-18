"""
This is a helper function file to store all the metadata and functions
    that help support the data analysis process for GRID3 User Surveys
"""

import pandas as pd
import numpy as np
from IPython.display import Markdown,display

def printmd(string):
    """
    Given a string, print a formatted
    markdown string with stylized fonts
    """
    display(Markdown(string))

class data_cleaner:
    def __init__(self,df):
        """
        This is a standard data cleaner
        made by Allen Hu
        """
        self.df = df
  
    def standardize_str(self,full=True,verbose=False,start=0,stop=15):

        """
        Given a dataframe, start and stop
        clean all the uneven capitalization
        of the string inputs
        
        MOD:1
        """
        import string

        count_not_string = 0

        if full:
            start = 0
            stop = self.df.shape[1]
        for i in range(start,stop):
            try:
                self.df.iloc[:,i] = self.df.iloc[:,i].apply(lambda x: string.capwords(x.lower()))
            #combining the same object encoded differently
            except:
                count_not_string += 1

        if verbose:
            print(f"Modified: {stop-count_not_string}/{stop} || Not Modified: {count_not_string}/{stop}\n-> With start:{start} and stop:{stop}")
        return self.df
    
    
    def string_splitter(string,demark=' '):
        lst_str = string.split(demark)


    


