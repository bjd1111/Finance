a = '1'

def next(a):
    i = 1
    count = 1
    number = ''
    while True:
        
        num = a[i-1]
        
        if i==len(a):
            
            number+=str(count)+str(num)
            break
        
        if a[i] == num:
            count += 1
            i+=1

        elif i==1:
            number+='1'+str(num)
            i+=1
        else:
            
                
            number += str(count)+str(num)
            count = 1
            i+=1
            
             
    return number

           
def ne(a):
    s = []
    while len(s) <40:
        s.append(a)
        a = next(a)
    return s

 
    
print len(ne(a)[30])
