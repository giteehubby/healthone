import csv
from crypt import encrypt_csv,decrypt_csv,is_exist

 
def empty_csv(file_path):
    with open(file_path, 'w', encoding='utf-8',newline='') as csvfile:
        pass

def csv2dict(file_path):
    """
    
    返回:
        dict: key:name ,value: {"password":"psw","time":"t"}
    """
    if not is_exist(file_path):
        print(f'{file_path} dosn\'t found')
        return None
    
    # 先解密
    decrypt_csv(file_path,file_path)

    with open(file_path, 'r', encoding='utf-8') as csvfile:
        res = dict()
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if len(row) != 3:continue
            nm, psw, t = row
            res[nm] = {"password":psw,"time":t}

    # 重新加密
    encrypt_csv(file_path,file_path)
    return res
    

def add2csv(file_path,nm,psw_t):
    """
    接受：name,password,time
    返回:
        dict: key:name ,value: {"password":"psw","time":"t"}
    """
    if not is_exist(file_path):
        empty_csv(file_path)
        # 空文件也加密
        encrypt_csv(file_path)
    
    # 先解密
    decrypt_csv(file_path)
    with open(file_path, 'a', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([nm,psw_t['password'],psw_t['time']])
    # 重新加密
    encrypt_csv(file_path)

def dict2csv(file_path,record):
    """
    接受：name,password,time
    返回:
        dict: key:name ,value: {"password":"psw","time":"t"}
    """
    
    with open(file_path, 'w', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        for nm in record.keys():
            csv_writer.writerow([nm,record[nm]['password'],record[nm]['time']])
    # 加密
    encrypt_csv(file_path)

password_names = './password_names'
def add_name_time(nm,t,pn_path=password_names):
    with open(pn_path, 'a', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([nm,t])