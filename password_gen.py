import random
import string
from typing import Union, Tuple, List

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
number_chars = list(string.digits)

def generate_password(plen:int=6,number_only:bool=True,add_chars:Union[Tuple[str], List[str]]=[]):
    # 先得到候选字符集
    char_list = number_chars + add_chars
    if not number_only:
        char_list = char_list + lowercase_letters + uppercase_letters
    # 随机放回采样，拼接
    return ''.join(random.choices(char_list,k=plen))

