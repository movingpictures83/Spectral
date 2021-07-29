
def isnumber(mystring):
    for i in range(0, len(mystring)):
        c = mystring[i]
        if ((not c.isdigit()) and (c != '.') and (not (i == 0 and c == '-' and len(mystring) > 1)) and (c != 'e') and (not (i > 0 and c == '-' and mystring[i-1] == 'e'))):
            return False
    return True

def test(file1, file2):
   firstfile = open(file1, 'r')
   secondfile = open(file2, 'r')
   lines1 = []
   lines2 = []
   for line in firstfile:
      lines1.append(line.strip())
   for line in secondfile:
      lines2.append(line.strip())

   if len(lines1) != len(lines2):
      return False

   for i in range(0, len(lines1)):
      #if (lines1[i][0] != '#'):
         if (lines1[i] != lines2[i]):
            contents1 = lines1[i].split(',')
            contents2 = lines2[i].split(',')
            for j in range(0, len(contents1)):
               if (isnumber(contents1[j]) and not isnumber(contents2[j])):
                    return False
               elif (not isnumber(contents1[j]) and isnumber(contents2[j])):
                   return False
               elif (isnumber(contents1[j])):
                   f1 = abs(float(contents1[j]))
                   f2 = abs(float(contents2[j]))
                   if (abs(f1) < 1):
                       if (abs(f2-f1) > 0.02):
                           print(f1)
                           print(f2)
                           print(abs(f2-f1))
                           return False
                   elif (abs(f2-f1)/f1 > 0.02):
                       print(f1)
                       print(f2)
                       print(abs(f2-f1)/f1)
                       return False
               else:
                   continue
                   #if (contents1[j] != contents2[j]):
                   #    print(contents1[j])
                   #    print(contents2[j])
                   #    return False


   return True    
