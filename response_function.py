from datetime import datetime
# from utils.function_tool import write_json
from file_io import csv2dict,dict2csv,add2csv,add_name_time

record_path = './record.csv'



def record(name:str,value:str,messagebox,save_path:str=record_path):
    new_record = {"password":value,"time":str(datetime.now()).split('.')[0]}
    existing_record = csv2dict(save_path)
    if existing_record is None:
        # 不存在该文件
        add2csv(save_path,name,new_record)
        add_name_time(name,new_record["time"])
    else:
        if name in existing_record.keys():
            result = messagebox.askyesno(
                title="确认操作",          # 标题
                message=f"{name}已存在密码，是否替换？",  # 提示内容
                icon="question"           # 图标类型：question/warning/info/error
            )
            if not result:
                return
        existing_record[name] = new_record
        add_name_time(name,new_record["time"])
        dict2csv(save_path,existing_record)


def search(name:str,save_path:str=record_path):
    existing_record = csv2dict(save_path)
    if existing_record is None:
        # 不存在该文件
        return "there is no record right now"
    else:
        if name in existing_record.keys():
            return f'{existing_record[name]["password"]} saved in {existing_record[name]["time"]}'
        
        else:return f"there is no record of {name}"


            

            
