import ccextractor as cc
import re
import codecs
import os

"""
            #Handling underline
            buff = ""
            underline_flag = 0
            for i,font_type in enumerate(font_line): 
                if font_type == 'U' and not underline_flag:
                        buff = buff + '<u> '
                        underline_flag = 1
                        underline=1
                elif font_type =="R" and underline_flag: 
                        buff = buff + '</u>'
                        underline_flag = 0
                        continue;
                buff +=  letter[i]
            #adding a new line after buff has seen underline
            #need to cross check with CCExtractor output as to how they are doing
            if underline:
                buff+= "\n"
            else:
                buff=""
"""
color_text_start={
        "0":"",
        "1":"<font color=\"#00ff00\">",
        "2":"<font color=\"#0000ff\">",
        "3":"<font color=\"#00ffff\">",
        "4":"<font color=\"#ff0000\">",
        "5":"<font color=\"#ffff00\">",
        "6":"<font color=\"#ff00ff\">",
        "7":"<font color=\"",
        "8":"",
        "9":""
};
color_text_end={
        "0":"",
        "1":"</font",
        "2":"</font>",
        "3":"</font>",
        "4":"</font>",
        "5":"</font>",
        "6":"</font>",
        "7":"</font>",
        "8":"",
        "9":""
};


def comparing_grids(text, font, color):
    temp = []
    for letter,color_line in zip(text,color):
        color = 0
        buff=""
        color_flag = 0
        if "                                " not in letter:
            for i,font_type in enumerate(color_line): 
                if font_type != '9' and not color_flag:
                        color = 1
                        prev = font_type
                        buff = buff + color_text_start[font_type]
                        color_flag = 1
                elif font_type=='9' and color_flag: 
                        buff = buff + color_text_end[prev]
                        color_flag = 0
                #        buff = buff + '</font>'
                buff += letter[i]
        if color:
            temp.append(buff)
        else:
            temp.append(letter)
    if temp:
        text = temp
        temp=[]
    for letter,font_line in zip(text,font):
        indices = []
        italics = 0
        if unicode("                                ",'utf-8') not in letter:
                buff=""
                #Handling italics
                prev = font_line[0]
                for i,font_type in enumerate(font_line): 
                        if font_type == 'I' and (prev=='R' or i==0):
                                italics  = 1
                                indices.append(i)
                        elif font_type =="R" and prev =='I': 
                                indices.append(i)
                        prev = font_type
                if italics:
                    open = 1
                    for i in xrange(len(letter)):
                        if i in indices:
                            if open:
                                buff+='<i>'
                                open=0
                            else:
                                buff+='</i>'
                                open=1
                        buff+=letter[i]
                    if len(indices)%2!=0 and italics:
                        buff+='</i>'
                    temp.append(buff)
                else:
                    temp.append(letter)
    if temp:
        text = temp
        temp=[]
    return (text,font, color)

    
def generate_output_srt( filename, d):
    try:
        d['text'] = [unicode(item,'utf-8') for item in d['text']]
    except:
        print "PYTHON ERROR"
        print
        exit(0)
    d['text'],d['font'], d['color'] = comparing_grids(d['text'],d['font'],d['color'])
    for item in d['text']:
        if "                                " not in item:
            #o = re.sub(r'[\x00-\x1e]',r'',item)
            #o = re.sub(r'\x1f[!@#$%^&*()]*', r'', o)
            #d = unicode(o,'utf-8')
            with open(filename,'ab+') as fh:
                fh.write(item.encode('utf-8'))
                fh.write("\n")
                fh.flush()
         #       os.fsync(fh)
    with open(filename,'ab+') as fh:
        fh.write("\n")
        #os.fsync(fh)
