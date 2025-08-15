# 🔐 健康手机密码管理器

一个现代化的密码生成和管理工具，帮助用户生成安全密码并养成健康的手机使用习惯。

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![GUI](https://img.shields.io/badge/GUI-Tkinter-orange.svg)
![Encryption](https://img.shields.io/badge/Encryption-Fernet-red.svg)

## 📖 项目简介

健康手机密码管理器是一个基于 Python 和 Tkinter 开发的桌面应用程序，专门设计用于：

- 🎲 **安全密码生成**：支持自定义长度、字符类型的密码生成
- 💾 **加密存储**：使用 Fernet 加密算法安全存储密码记录
- 🔍 **智能查询**：通过验证机制安全检索已保存的密码
- 🎯 **健康提醒**：内置健康使用手机的理念和提醒

## ✨ 主要特性

### 🛡️ 安全特性
- **Fernet 加密**：所有密码记录使用军用级加密算法保护
- **安全验证**：查询密码需要输入特定验证语句
- **本地存储**：所有数据存储在本地，确保隐私安全

### 🎨 界面特性
- **深色主题**：采用现代化深色主题设计，减少眼部疲劳
- **响应式布局**：支持窗口大小调整，界面自适应
- **用户友好**：直观的操作界面，支持键盘快捷键
- **视觉反馈**：操作状态实时显示，成功/错误提示清晰

### 🔧 功能特性
- **灵活密码生成**：
  - 自定义密码长度（1-100位）
  - 可选包含字母（大小写）
  - 支持自定义特殊字符
  - 一键复制到剪贴板
- **密码管理**：
  - 安全保存密码记录
  - 防重复保存确认
  - 时间戳记录
- **便捷操作**：
  - 回车键快速生成
  - 一键清空所有内容
  - 状态栏实时反馈

## 🚀 快速开始
- 无需部署，拷贝dist文件夹即可食用！运行dist下的healthone.exe即可运行
- 创建的密码加密保存在record.csv中，key.key是小程序需要的密钥，不要删除！

### 环境要求

- **Python**: 3.8 或更高版本
- **操作系统**: Windows / macOS / Linux
- **依赖库**: 详见 `requirements.txt`

### 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/your-username/healthone.git
cd healthone
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **运行程序**
```bash
python healthone.py
```

### 打包为可执行文件

使用 PyInstaller 打包为独立的可执行文件：

```bash
# 生成可执行文件
pyinstaller healthone.spec

# 或者使用命令行直接打包
pyinstaller --onefile --windowed healthone.py
```

打包后的文件位于 `dist/` 目录下。

## 📱 使用指南

### 1. 密码生成

1. **设置密码长度**：在"密码长度"输入框中输入所需的密码位数（1-100）
2. **选择字符类型**：勾选"包含字母"以包含大小写字母
3. **添加特殊字符**：在"特殊字符"输入框中输入需要包含的特殊字符
4. **生成密码**：点击"🎯 生成密码"按钮或按回车键
5. **复制密码**：点击"📋 复制"按钮将密码复制到剪贴板

### 2. 密码保存

1. **输入密码名称**：在"密码名称"输入框中输入便于记忆的名称
2. **保存密码**：点击"💾 保存"按钮
3. **确认替换**：如果名称已存在，系统会询问是否替换

### 3. 密码查询

1. **输入验证语句**：强制先在在"验证输入"框中输入提示语句才能查询
   ```
   放下手机，享受生活！
   ```
2. **查询密码**：点击"🔍 查询"按钮
3. **查看结果**：密码信息将显示在生成结果区域
4. **忘记密码名字怎么查？**：密码名字与建立时间藏在dist/password_names文件中！

### 4. 其他功能

- **清空内容**：点击"🗑️ 清空"按钮清除所有输入
- **状态查看**：界面底部状态栏显示操作结果

## 📂 项目结构

```
healthone/
├── healthone.py          # 主程序入口和GUI界面
├── password_gen.py       # 密码生成模块
├── response_function.py  # 记录和查询功能
├── file_io.py           # 文件操作模块
├── crypt.py             # 加密解密模块
├── requirements.txt     # 项目依赖
├── README.md           # 项目文档
├── healthone.spec      # PyInstaller配置
├── record.csv          # 加密的密码记录文件
├── password_names      # 密码名称记录
└── test.ipynb          # 测试笔记本
```

## 🔒 安全说明

### 加密机制
- 使用 **Fernet** 对称加密算法保护密码文件
- 加密密钥在程序运行时动态生成
- 文件在读写时自动加密/解密

### 数据安全
- 所有密码记录仅存储在本地计算机
- 不涉及网络传输，确保数据隐私
- 程序关闭后，敏感数据不会在内存中残留

### 使用建议
1. 定期备份 `record.csv` 文件
2. 不要与他人分享验证语句
3. 建议在安全的环境中使用此工具
4. 定期更新程序以获得安全补丁

## 🛠️ 开发说明

### 核心模块

#### `healthone.py` - 主界面
- 基于 Tkinter 的现代化GUI界面
- 响应式布局和美观的视觉设计
- 用户交互逻辑和事件处理

#### `password_gen.py` - 密码生成
```python
def generate_password(plen: int = 6, number_only: bool = True, 
                     add_chars: Union[Tuple[str], List[str]] = []):
    # 生成指定长度和字符集的密码
```

#### `crypt.py` - 加密模块
```python
def encrypt_csv(file_path: str, output_path: str = None):
    # 使用Fernet加密CSV文件

def decrypt_csv(file_path: str, output_path: str = None):
    # 解密CSV文件
```

### 配色方案

项目采用现代化的深色主题配色，提供舒适的视觉体验：

```python
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
```

## 🤝 贡献指南

欢迎为项目做出贡献！请遵循以下步骤：

1. Fork 项目仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交变更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

### 代码规范
- 遵循 PEP 8 Python 代码规范
- 添加适当的注释和文档字符串
- 确保新功能有相应的测试

## 📄 许可证

本项目采用 MIT 许可证。详情请参阅 [LICENSE](LICENSE) 文件。

## 📞 联系方式

- **项目维护者**: 您的姓名
- **邮箱**: your.email@example.com
- **项目主页**: https://github.com/your-username/healthone

## 🙏 致谢

- 感谢 Python 社区提供的优秀库和工具
- 感谢所有为项目提供建议和反馈的用户
- 特别感谢 [cryptography](https://cryptography.io/) 项目提供的安全加密支持

## 📈 版本历史

### v2.0.0 (当前版本)
- ✨ 全新现代化界面设计
- 🔧 增强的密码生成功能
- 🛡️ 改进的安全性和加密机制
- 📋 新增密码复制功能
- 🗑️ 添加一键清空功能

### v1.0.0
- 🎉 初始版本发布
- 🔐 基本密码生成和管理功能
- 💾 文件加密存储
- 🔍 密码查询验证机制

---

**健康使用手机，远离数字成瘾** 💚

*本项目致力于帮助用户管理密码的同时，提醒大家保持健康的数字生活方式。* 