from ExtractTable import ExtractTable
import pandas as pd
import numpy as np

class ExtractTableFromImage:
    

    def __init__(self, api_key):
        self.api_key = api_key

    def image_to_df(self,filepath):
        et_sess = ExtractTable(api_key=self.api_key)        # Replace your VALID API Key here
        print(et_sess.check_usage())        # Checks the API Key validity as well as shows associated plan usage 
        table_data = et_sess.process_file(filepath=filepath, output_format="df")
        return table_data[0]