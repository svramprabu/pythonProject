def createboard():
    
    for i in range(3):
        print('|',end='')
        for j in range(3):
            print(' _ ',end="|")
        print()

createboard()