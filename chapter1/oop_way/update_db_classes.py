import shelve

db = shelve.open('class-shelve')
for i in db:
    print(i)
# sue=db['sue']
# db = shelve.open('class-shelve')
# sue = db['sue']
# sue.giveRaise(0.25)
# # db['sue'] = sue
#
# tom = db['tom']
# tom.giveRaise(0.2)
# # db['tom'] = tom
# db.close()