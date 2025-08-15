from cryptography.fernet import Fernet
from pathlib import Path




def is_exist(file_path):
    file_path = Path(file_path)
    return file_path.exists()


if is_exist('./key.key'):
    with open("key.key", "rb") as f:  # 注意使用二进制模式 'rb'
        key = f.read()
else:
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)


# 加密 CSV 文件
def encrypt_csv(input_path,output_path=None):
    # 默认保存为相同的文件名
    if output_path is None:output_path=input_path
    # 文件不存在，无需加密
    if not is_exist(input_path):return
    fernet = Fernet(key)
    with open(input_path, 'rb') as f_in:
        data = f_in.read()
    encrypted_data = fernet.encrypt(data)
    with open(output_path, 'wb') as f_out:
        f_out.write(encrypted_data)

# 解密 CSV 文件
def decrypt_csv(input_path, output_path=None):
    if output_path is None:output_path=input_path
    if not is_exist(input_path):return
    fernet = Fernet(key)
    with open(input_path, 'rb') as f_in:
        encrypted_data = f_in.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(output_path, 'wb') as f_out:
        f_out.write(decrypted_data)

    
