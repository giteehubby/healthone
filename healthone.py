import tkinter as tk
from tkinter import messagebox, ttk
from password_gen import generate_password
from response_function import record,search


'''
健康手机密码管理器 - 现代化界面版本

主要功能：
- 密码生成：自定义长度、包含字符类型
- 密码保存：安全存储密码记录
- 密码查询：快速检索已保存的密码
'''

plen = 0
psw = ''

# 深色主题配色方案
COLORS = {
    'primary': '#60A5FA',      # 主色调 - 亮蓝色
    'secondary': '#F472B6',    # 辅助色 - 亮粉色
    'accent': '#FBBF24',       # 强调色 - 亮黄色
    'success': '#34D399',      # 成功色 - 绿色
    'background': '#111827',   # 背景色 - 深灰
    'surface': '#1F2937',      # 表面色 - 中深灰
    'text_primary': '#F9FAFB', # 主文本色 - 浅色
    'text_secondary': '#D1D5DB', # 辅助文本色 - 中浅色
    'border': '#374151',       # 边框色 - 灰色
    'input_bg': '#374151',     # 输入框背景 - 灰色
    'hover': '#4B5563'         # 悬停色 - 稍亮灰色
}

########################信号槽#######################
def validate_input():
    """验证输入并生成密码"""
    plen_input = entry.get()
    special_input = special_entry.get()
    
    if special_input == '':
        add_chars = []
    else:
        add_chars = [c for c in special_input]
    
    try:
        global plen
        plen = int(plen_input)
        if plen <= 0 or plen > 100:
            messagebox.showerror("输入无效", "密码长度应在1-100之间！")
            return
            
        global psw
        psw = generate_password(plen=plen, number_only=not(letter_var.get()), add_chars=add_chars)
        
        # 更新密码显示，使用现代化样式
        password_display.config(state='normal')
        password_display.delete(1.0, tk.END)
        password_display.insert(1.0, psw)
        password_display.config(state='disabled')
        
        # 显示成功提示
        status_label.config(text="✓ 密码生成成功", fg=COLORS['success'])

    except ValueError:
        messagebox.showerror("输入无效", "请输入一个有效的整数！")
        status_label.config(text="✗ 输入格式错误", fg=COLORS['accent'])

def call_record():
    """保存密码记录"""
    if name_entry.get() and psw:
        record(name_entry.get(), psw, messagebox)
        status_label.config(text="✓ 密码已保存", fg=COLORS['success'])
    else:
        if not name_entry.get():
            messagebox.showerror("缺少输入", "请输入密码名称！")
        elif not psw:
            messagebox.showerror("缺少密码", "请先生成密码！")

def call_search():
    """搜索密码记录"""
    wake_text = wake_entry.get().strip()
    target_text = wake_label["text"]
    
    if wake_text == target_text:
        result = search(name_entry.get())
        password_display.config(state='normal')
        password_display.delete(1.0, tk.END)
        password_display.insert(1.0, result)
        password_display.config(state='disabled')
        status_label.config(text="✓ 查询完成", fg=COLORS['success'])
    else:
        password_display.config(state='normal')
        password_display.delete(1.0, tk.END)
        password_display.insert(1.0, "请先正确输入提示语")
        password_display.config(state='disabled')
        status_label.config(text="✗ 验证失败", fg=COLORS['accent'])

def copy_password():
    """复制密码到剪贴板"""
    if psw:
        root.clipboard_clear()
        root.clipboard_append(psw)
        status_label.config(text="✓ 密码已复制到剪贴板", fg=COLORS['success'])
    else:
        messagebox.showwarning("提示", "没有可复制的密码")

def clear_all():
    """清空所有输入"""
    entry.delete(0, tk.END)
    special_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    wake_entry.delete(0, tk.END)
    password_display.config(state='normal')
    password_display.delete(1.0, tk.END)
    password_display.config(state='disabled')
    letter_var.set(False)
    status_label.config(text="已清空所有内容", fg=COLORS['text_secondary'])
    global psw
    psw = ''

# 创建主窗口
root = tk.Tk()
root.title("健康手机密码管理器 v2.0")
root.geometry("600x750")
root.configure(bg=COLORS['background'])
root.resizable(True, True)

# 设置窗口图标（如果有的话）
# root.iconbitmap('icon.ico')

# 创建主容器
main_frame = tk.Frame(root, bg=COLORS['background'], padx=30, pady=20)
main_frame.pack(fill='both', expand=True)

# 标题区域
title_frame = tk.Frame(main_frame, bg=COLORS['background'])
title_frame.pack(fill='x', pady=(0, 30))

title_label = tk.Label(title_frame, 
                      text="🔐 健康手机密码管理器", 
                      font=('Microsoft YaHei', 20, 'bold'),
                      fg=COLORS['primary'],
                      bg=COLORS['background'])
title_label.pack()

subtitle_label = tk.Label(title_frame, 
                         text="安全生成 • 智能管理 • 健康使用", 
                         font=('Microsoft YaHei', 10),
                         fg=COLORS['text_secondary'],
                         bg=COLORS['background'])
subtitle_label.pack(pady=(5, 0))

# 密码生成区域
gen_frame = tk.LabelFrame(main_frame, 
                         text="🎲 密码生成", 
                         font=('Microsoft YaHei', 12, 'bold'),
                         fg=COLORS['primary'],
                         bg=COLORS['surface'],
                         relief='solid',
                         bd=1)
gen_frame.pack(fill='x', pady=(0, 20), padx=5, ipady=15)

# 密码长度输入
length_frame = tk.Frame(gen_frame, bg=COLORS['surface'])
length_frame.pack(fill='x', padx=20, pady=10)

length_label = tk.Label(length_frame, 
                       text="密码长度:", 
                       font=('Microsoft YaHei', 10),
                       fg=COLORS['text_primary'],
                       bg=COLORS['surface'])
length_label.pack(side='left')

entry = tk.Entry(length_frame, 
                width=10, 
                font=('Consolas', 11),
                relief='solid',
                bd=1,
                bg=COLORS['input_bg'],
                fg=COLORS['text_primary'],
                insertbackground=COLORS['text_primary'],
                highlightthickness=2,
                highlightcolor=COLORS['primary'])
entry.pack(side='left', padx=(10, 20))
entry.insert(0, "12")  # 默认长度

letter_var = tk.BooleanVar(value=True)
letter_check = tk.Checkbutton(length_frame, 
                             text="包含字母", 
                             variable=letter_var,
                             font=('Microsoft YaHei', 10),
                             fg=COLORS['text_primary'],
                             bg=COLORS['surface'],
                             activebackground=COLORS['surface'],
                             activeforeground=COLORS['text_primary'],
                             selectcolor=COLORS['input_bg'])
letter_check.pack(side='left')

# 特殊字符输入
special_frame = tk.Frame(gen_frame, bg=COLORS['surface'])
special_frame.pack(fill='x', padx=20, pady=10)

special_label = tk.Label(special_frame, 
                        text="特殊字符:", 
                        font=('Microsoft YaHei', 10),
                        fg=COLORS['text_primary'],
                        bg=COLORS['surface'])
special_label.pack(side='left')

special_entry = tk.Entry(special_frame, 
                        width=15, 
                        font=('Consolas', 11),
                        relief='solid',
                        bd=1,
                        bg=COLORS['input_bg'],
                        fg=COLORS['text_primary'],
                        insertbackground=COLORS['text_primary'],
                        highlightthickness=2,
                        highlightcolor=COLORS['primary'])
special_entry.pack(side='left', padx=(10, 0))
special_entry.insert(0, "!@#$")  # 默认特殊字符

# 生成按钮
button_frame = tk.Frame(gen_frame, bg=COLORS['surface'])
button_frame.pack(fill='x', padx=20, pady=15)

gen_button = tk.Button(button_frame, 
                      text="🎯 生成密码", 
                      command=validate_input,
                      font=('Microsoft YaHei', 11, 'bold'),
                      bg=COLORS['primary'],
                      fg='white',
                      relief='flat',
                      padx=20,
                      pady=8,
                      cursor='hand2',
                      activebackground=COLORS['hover'])
gen_button.pack(side='left')

copy_button = tk.Button(button_frame, 
                       text="📋 复制", 
                       command=copy_password,
                       font=('Microsoft YaHei', 10),
                       bg=COLORS['accent'],
                       fg='white',
                       relief='flat',
                       padx=15,
                       pady=8,
                       cursor='hand2',
                       activebackground=COLORS['hover'])
copy_button.pack(side='left', padx=(10, 0))

clear_button = tk.Button(button_frame, 
                        text="🗑️ 清空", 
                        command=clear_all,
                        font=('Microsoft YaHei', 10),
                        bg=COLORS['text_secondary'],
                        fg='white',
                        relief='flat',
                        padx=15,
                        pady=8,
                        cursor='hand2',
                        activebackground=COLORS['hover'])
clear_button.pack(side='right')

# 密码显示区域
display_frame = tk.LabelFrame(main_frame, 
                             text="🔍 生成结果", 
                             font=('Microsoft YaHei', 12, 'bold'),
                             fg=COLORS['primary'],
                             bg=COLORS['surface'],
                             relief='solid',
                             bd=1)
display_frame.pack(fill='x', pady=(0, 20), padx=5, ipady=15)

password_display = tk.Text(display_frame, 
                          height=3, 
                          font=('Consolas', 12, 'bold'),
                          fg=COLORS['success'],
                          bg=COLORS['input_bg'],
                          relief='solid',
                          bd=1,
                          wrap='word',
                          state='disabled',
                          cursor='arrow',
                          selectbackground=COLORS['hover'],
                          selectforeground=COLORS['text_primary'])
password_display.pack(fill='x', padx=20, pady=10)

# 密码管理区域
manage_frame = tk.LabelFrame(main_frame, 
                            text="💾 密码管理", 
                            font=('Microsoft YaHei', 12, 'bold'),
                            fg=COLORS['primary'],
                            bg=COLORS['surface'],
                            relief='solid',
                            bd=1)
manage_frame.pack(fill='x', pady=(0, 20), padx=5, ipady=15)

# 密码名称输入
name_frame = tk.Frame(manage_frame, bg=COLORS['surface'])
name_frame.pack(fill='x', padx=20, pady=10)

name_label = tk.Label(name_frame, 
                     text="密码名称:", 
                     font=('Microsoft YaHei', 10),
                     fg=COLORS['text_primary'],
                     bg=COLORS['surface'])
name_label.pack(side='left')

name_entry = tk.Entry(name_frame, 
                     width=25, 
                     font=('Microsoft YaHei', 11),
                     relief='solid',
                     bd=1,
                     bg=COLORS['input_bg'],
                     fg=COLORS['text_primary'],
                     insertbackground=COLORS['text_primary'],
                     highlightthickness=2,
                     highlightcolor=COLORS['primary'])
name_entry.pack(side='left', padx=(10, 20))

save_button = tk.Button(name_frame, 
                       text="💾 保存", 
                       command=call_record,
                       font=('Microsoft YaHei', 10, 'bold'),
                       bg=COLORS['success'],
                       fg='white',
                       relief='flat',
                       padx=20,
                       pady=6,
                       cursor='hand2',
                       activebackground=COLORS['hover'])
save_button.pack(side='left')

# 查询验证区域
search_frame = tk.LabelFrame(main_frame, 
                            text="🔐 安全查询", 
                            font=('Microsoft YaHei', 12, 'bold'),
                            fg=COLORS['primary'],
                            bg=COLORS['surface'],
                            relief='solid',
                            bd=1)
search_frame.pack(fill='x', pady=(0, 20), padx=5, ipady=15)

# 验证提示语
wake_info_frame = tk.Frame(search_frame, bg=COLORS['surface'])
wake_info_frame.pack(fill='x', padx=20, pady=5)

wake_label = tk.Label(wake_info_frame, 
                     text="放下手机，享受生活！", 
                     font=('Microsoft YaHei', 9, 'italic'),
                     fg=COLORS['secondary'],
                     bg=COLORS['surface'])
wake_label.pack()

# 验证输入
verify_frame = tk.Frame(search_frame, bg=COLORS['surface'])
verify_frame.pack(fill='x', padx=20, pady=10)

verify_label = tk.Label(verify_frame, 
                       text="验证输入:", 
                       font=('Microsoft YaHei', 10),
                       fg=COLORS['text_primary'],
                       bg=COLORS['surface'])
verify_label.pack(side='left')

wake_entry = tk.Entry(verify_frame, 
                     width=35, 
                     font=('Microsoft YaHei', 10),
                     relief='solid',
                     bd=1,
                     bg=COLORS['input_bg'],
                     fg=COLORS['text_primary'],
                     insertbackground=COLORS['text_primary'],
                     highlightthickness=2,
                     highlightcolor=COLORS['primary'])
wake_entry.pack(side='left', padx=(10, 20))

search_button = tk.Button(verify_frame, 
                         text="🔍 查询", 
                         command=call_search,
                         font=('Microsoft YaHei', 10, 'bold'),
                         bg=COLORS['secondary'],
                         fg='white',
                         relief='flat',
                         padx=20,
                         pady=6,
                         cursor='hand2',
                         activebackground=COLORS['hover'])
search_button.pack(side='left')

# 状态栏
status_frame = tk.Frame(main_frame, bg=COLORS['background'])
status_frame.pack(fill='x', pady=(10, 0))

status_label = tk.Label(status_frame, 
                       text="欢迎使用健康手机密码管理器", 
                       font=('Microsoft YaHei', 9),
                       fg=COLORS['text_secondary'],
                       bg=COLORS['background'])
status_label.pack()

# 版权信息
footer_frame = tk.Frame(main_frame, bg=COLORS['background'])
footer_frame.pack(fill='x', pady=(20, 0))

footer_label = tk.Label(footer_frame, 
                       text="健康使用手机，远离数字成瘾 | © 2024", 
                       font=('Microsoft YaHei', 8),
                       fg=COLORS['text_secondary'],
                       bg=COLORS['background'])
footer_label.pack()

# 绑定回车键事件
def on_enter_key(event):
    validate_input()

entry.bind('<Return>', on_enter_key)
special_entry.bind('<Return>', on_enter_key)

# 运行主循环
root.mainloop()