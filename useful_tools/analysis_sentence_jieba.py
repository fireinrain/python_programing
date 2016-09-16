#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang



# 简单的结巴分词应用
# 功能
# 1.对文本进行分词处理
# 2.统计每个词出现的频率
# 3.进行排序
# 将排序结果写入文本

# refer：没有对结巴分词有深入的研究，所以分析就比较粗糙
# 但是还是可以定性的分析一些东西的

import jieba

def open_file(filename) :
    # filename = 'lagou_job_java.txt'
    f = open(filename,'rb')
    file_list = f.readlines()
    f.close()
    return file_list

def list_encode(file_list):
    line_container=[]
    for i in file_list:
        each_line=i.decode('utf-8')
        line=each_line.split()


        line_container.append(line)

    return line_container


def process(line_container):
    tf={}
    for line_list in line_container:
        for strings in line_list:

            seg_list = jieba.cut(strings,cut_all=False)
            for word in seg_list:
                if word in tf:
                    tf[word]+=1
                else:
                    tf[word]=1
    return tf
    #
    # tf={}
    # for seg in seg_list :
    #     #print seg
    #     seg = ''.join(seg.split())
    #     if (seg != '' and seg != "\n" and seg != "\n\n") :
    #         if seg in tf :
    #             tf[seg] += 1
    #         else :
    #             tf[seg] = 1
    #
    # f = open("result.txt","w+")
    # for item in tf:
    #     #print item
    #     f.write(item+"  "+str(tf[item])+"\n")
    # f.close()

# def select_sort(lists):
#     count=len(lists)
#     for i in range(0,count):
#         min=1
#         for j in range(i+1,count):
#             if lists[min]>list[j]:
#                 min=j
#             lists[min],lists[i]=lists[i],lists[min]
#     return lists

if __name__ == '__main__' :
    filename=input('请输入文本名称：')
    file=open_file(filename)
    bbt=list_encode(file)
    result=process(bbt)
    list_container=list(result.items())
    container=[]
    for i in list_container:

        cover=[i[1],i[0]]
        container.append(cover)

    container_sort=sorted(container)
    with open('result_java.txt','w+',encoding='utf-8') as file:
        for item in container_sort:
            file.write(item[1]+str(item[0])+'\n')