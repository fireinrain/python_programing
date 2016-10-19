#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com


# 简单的记笔记类

import datetime

# 为所有的新标签备注储存下一个可用的id
last_id=0

class Note:
    """
    展示一个notebook应用，通过字符串查找相关的note
    """
    def __init__(self,memo,tags=''):
        """
        初始化笔记，包括传入的，笔记内容和标签，
        还需要自己设定创建时间和序号
        :param memo:
        :param tags:
        """
        self.memo=memo
        self.tags=tags
        self.creation_date=datetime.date.today()
        global last_id
        last_id+=1
        self.id=last_id

    def match(self,filter):
        """
        检查传入匹配或是过滤项是否有结果
        :param filter:
        :return:
        """
        return filter in self.memo or filter in self.tags


class Notebook:
    """
    展现一个note的集合，包含的方法有创建note，查找note
    修改note，修改tangs标签
    """
    def __init__(self):
        """
        为一个Notebook对象实现一个收集列表
        """
        self.notes=[]

    def new_note(self,memo,tags=''):
        """
        创建note并把它添加到notes列表张
        :param memo:
        :param tags:
        :return:
        """
        self.notes.append(Note(memo,tags))

    def _find_note(self,note_id):
        """
        将修改方法中的查找note的过程抽象出来作为单独的方法，
        但是这个方法是有单下划线的，意味着只能在内部使用
        :param note_id:
        :return:
        """
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note

        return None


    def modify_memo(self,note_id,memo):
        """
        查找到传入id的note并实现修改
        :param note_id:
        :param memo:
        :return:
        """
        # for note in self.notes:
        #     if note.id==note_id:
        #         note.memo=memo
        #         break

        note=self._find_note(note_id)
        if note:
            note.memo=memo
            return True
        else:
            return False
        # print(self._find_note(note_id))

    def modify_tags(self,note_id,tags):
        """
        查找传入id的note，并修改其包含的tags
        :param note_id:
        :param tags:
        :return:
        """
        # for note in self.notes:
        #     if note.id==note_id:
        #         note.tags=tags
        #         break
        self._find_note(note_id).tags=tags


    def search(self,filter):
        """
        按照传入的字符串实现查找并返回
        :param filter:
        :return:
        """
        return [note for note in self.notes if note.match(filter)]



