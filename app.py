import src.setting_output.SettingOutputData as SettingOutputData
from src.extract_table import ExtractTableFromImage
from src.clean_df import CleanDf
from globals import EXTRACT_TABLE_APIKEY
import pandas as pd



"""
- Primeiro o usuario tira foto da sumula com results;
- Depois ele faz o upload na aplicacao;
- Visualiza os resultados digitalizados;
- Faz as modificacoes que forem necessarias, essas podem ser do tipo: nome de coluna, exclusão de linhas, adição de linhas, edição de linhas;
- Ai o usuario escolhe as colunas a serem exibidas na sumula de resultados;
- ve um preview do que será exportado para a planilha;
- Recebe uma planilha com resultado e com a sumula digitalizada;
"""



def main_pipeline():


    #et_client = ExtractTableFromImage(EXTRACT_TABLE_APIKEY)
    #df = et_client.image_to_df("image_files/image_test_5.jpg")
    #df.to_pickle("pk_df_5.pkl")  
    df = pd.read_pickle("pk_df.pkl")
    workflow = SettingOutputData(df)
    print("Resultados escaneados:")
    df = workflow.replace_header_by_first_row()
    print(df)
    ##here we need to add a modification values interation
    df = workflow.modify_row_pipeline()
    df = workflow.remove_empty_columns()
    df = workflow.remove_row_with_null_result()
    print(df)
    df = workflow.classification_by_event_type()
    df = workflow.transform_data_to_user_request()
    #AINDA PRECISA ADICIONAR COLUNAS OPCIONAIS, COMO A PONTUACAO
    print(df)
    return 0

#main_pipeline()