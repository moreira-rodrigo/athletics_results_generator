from src.setting_output import SettingOutputData
from src.extract_table import ExtractTable
from globals import EXTRACT_TABLE_APIKEY

et_client = ExtractTable(EXTRACT_TABLE_APIKEY)
workflow = SettingOutputData("df")
workflow.get_event_type()


