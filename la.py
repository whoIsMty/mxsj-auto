import matplotlib.font_manager as fm

# 获取所有系统字体
fonts = fm.findSystemFonts(fontpaths=None, fontext='ttf')

# 打印所有字体路径和名称
for font in fonts:
    try:
        font_name = fm.FontProperties(fname=font).get_name()
        print(f"Font Path: {font} - Font Name: {font_name}")
    except Exception as e:
        print(f"Error reading font {font}: {e}")
