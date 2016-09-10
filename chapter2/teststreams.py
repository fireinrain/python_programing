"""
read numbers till eof and show squares
"""
def interact():
    print('hello stream world')
    while True:
        try:
            reply=input('enter a number>')
        except EOFError as e:
            break
        else:
            num=int(reply)
            print('%d squares is %d' % (num,num**2))
    print('bye....bye')
if __name__=="__main__":
    interact()