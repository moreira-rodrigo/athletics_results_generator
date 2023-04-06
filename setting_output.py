class SettingOutputData:

    NOT_VALID_RESULTS=['DNS','DSQ','DNF','NM']
    EVENT_TYPE = {"1":"PISTA","2":"CAMPO"}

    def __init__(self, df):
        self.df = df

    def classification_by_event_type(self):
        df = self.df
        NOT_VALID_RESULTS = self.NOT_VALID_RESULTS
        event_type = self.get_event_type()
        if event_type == "PISTA":
            df = df.sort_values("RESULTADO").reset_index(drop = True)
        else:
            df = df.query("RESULTADO not in @NOT_VALID_RESULTS")
            df = df.sort_values("RESULTADO",ascending=False).reset_index(drop = True)
        df.index = df.index + 1
        self.df = df
        return df

    def transform_data_to_user_request(self):
        df = self.df 
        columns_list = self.get_final_result_columns()
        df = df[columns_list]
        df = df.reset_index(drop = True)
        df.index = df.index + 1
        self.df = df
        return df

    def get_columns_from_df(self):
        return list(self.df.columns)

    def get_final_result_columns(self):
        df = self.df
        columns_to_final_result = []
        print("Quais destas colunas deseja manter no resultado final:")
        columns = self.get_columns_from_df()
        columns_dict = dict(zip([i for i in range(0, len(columns)-1)],columns))
        for key,value in columns_dict.items():
            print("Selecione: "+ str(key) + " para " + str(value))
        print("Digite FIM para finalizar")
        value_selected = input()
        while(value_selected != "FIM" or len(columns_dict) == 0):
            columns_to_final_result.append(columns_dict[int(value_selected)])
            columns_dict.pop(int(value_selected))
            for key,value in columns_dict.items():
                print("Selecione: "+ str(key) + " para " + str(value))
            print("Digite FIM para finalizar")
            value_selected = input()
        print("Colunas selecionadas: ")
        print(columns_to_final_result)
        self.df = df
        return columns_to_final_result         


    def get_row_index(self):
        df = self.df
        print("Qual linha voce quer editar?")
        row_to_edit = int(input())
        while not row_to_edit < len(df):
            print("Escolhe um indice de linha valido!")
            row_to_edit = int(input())
        return row_to_edit

    def get_column_to_edit(self):
        print("Qual coluna quer editar?")
        columns = self.get_columns_from_df()
        print(columns)
        column_name = input()
        while column_name not in columns:
            print("Escolha uma coluna valida")
            column_name = input()
        return column_name
    
    def modify_row_by_index(self):
        df = self.df
        linha = self.get_row_index()
        coluna = self.get_column_to_edit()
        print("Escolha o novo valor:")
        value = input()
        df.at[linha,coluna]=value
        self.df = df
        return df
    

    def modify_row_pipeline(self):
        df = self.df
        print("Existe algum registro a ser modificado? Digite SIM ou NAO")
        modification_status = input()
        while modification_status == "SIM":
            self.modify_row_by_index()
            print(df)
            print("Existe algum outro registro a ser modificado? Digite SIM ou NAO")
            modification_status = input()
        self.df = df
        return df

    def get_event_type(self):
        """
            This method is to get if the event is track or field and order the result by this
        """
        print("Escolha entre os tipos de prova:")
        for key,value in self.EVENT_TYPE.items():
            print("Digite ["+str(key) + "] Para " + value)
        event_id = input()
        while event_id not in self.EVENT_TYPE.keys():
            print("Voce escolheu tipo de prova errado. Selecione de novo:")
            event_id = input()
        print("Criando tratativas para provas de "+self.EVENT_TYPE[event_id])
        return self.EVENT_TYPE[event_id]

    def replace_header_by_first_row(self):
        df = self.df
        df.columns = df.iloc[0]
        df = df[1:]
        self.df = df
        return df
    
    def remove_empty_columns(self):
        df = self.df
        for column in df.columns: 
            if column == '' or column == "0":
                df.drop(columns=[''])
        self.df = df
        return df
    
    def remove_row_with_null_result(self):
        df = self.df
        df = df[df.RESULTADO != '']
        self.df = df
        return df