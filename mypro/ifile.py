#功能说明：给末尾无换行符的文件添加换行符、删除数据文件中的空行和注释行
#2017.05.12版

#
def wipestr(str1, str2):
	strsplit = str1.split(str2)
	num = len(strsplit)
	i = 0
	str = ''
	while i < num:
		str = str + strsplit[i]
		i+=1
	return str

def openfile(file_name):
    #print('hello, world')
    file = []
    
    f = open(file_name)
    f.seek(0,0)
    f_lines = list(f)
    num = len(f_lines)

    '''
    #给未添加换行符的末尾添加换行符
    num_last = len(f_lines[num-1])
    
    last = f_lines[num-1][num_last-1]
    if last != 'n' and last != '\n':
        f_lines[num-1] = f_lines[num-1]+'\n'
	'''
    i = num-1
	#剔除空行和注释行、空格
    while i >= 0:
        if f_lines[i] == '\n' or f_lines[i][0] == '#':
            f_lines.pop(i)
        else:
            f_lines[i] = wipestr(f_lines[i], '\n')
            f_lines[i] = wipestr(f_lines[i], ' ')
        i -= 1

    num = len(f_lines)
    i = 0
    while i < num:
        x = f_lines[i].split(',')
        file.append(x)
        i += 1

    return file
