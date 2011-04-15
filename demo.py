from framecontext import *

__frame__ = {'module':'module'}

class Test(object):
    __frame__ = {'class':'class'}

    def __init__(self):
        __frame__ = {'method':'method'}

        print collect_frame_contexts()

class SubTestA(Test):
    __frame__ = {'class':'subclassA'}

    def __init__(self):
        __frame__ = {'method':'subclassA'}

        print collect_frame_contexts()

class SubTestB(Test):
    __frame__ = {'class':'subclassB'}

    def __init__(self):
        __frame__ = {'method':'subclassB'}

        print collect_frame_contexts()

class SubTestC(Test):
    __frame__ = {
        'module':'overridden by subclassC',
        'class':'subclassC'
        }

    def __init__(self):
        __frame__ = {'method':'subclassC'}
        print collect_frame_contexts(immediate="subclassC")

def testalone():
    __frame__ = {'method':'standalone'}
    print collect_frame_contexts()

t_base = Test()
t_subA = SubTestA()
t_subB = SubTestB()
t_subC = SubTestC()
testalone()

print collect_frame_contexts(module='overridden by immediate context')
