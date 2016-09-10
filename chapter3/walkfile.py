import os
for (dirname,subshere,fileshere) in os.walk('.'):
    print('>>>'+dirname+'<<<')
    # for fname in fileshere:
    #     print(os.path.join(dirname,fname))
    print(subshere)