
import numpy as np

verifyingNumber = 0 
result = []
listMultiplicator = [2, 1, 2, 1, 2, 1, 2 , 1, 2]

while True:
    try:
        verifyingNumber = input("Input your identification; ")
        listDigits = [str(x) for x in str(verifyingNumber)]
        listDigits.remove("-")
        listDigits = listDigits[:-1]
        listDigits = list(map(int, listDigits))
        array1 = np.array(listMultiplicator, dtype=np.int16)
        array2 = np.array(listDigits, dtype=np.int16)
        result = (array1 * array2)
        result = list(map(str, result))
        listDigits = []
        for x in result: 
            if len(x) > 1: 
              listDigits.append(x[0])
              listDigits.append(x[1])
            else:
              listDigits.append(x)
        listDigits = list(map(int, listDigits))   
        
        numsum = sum(listDigits)
        controlNumber = (10 - (numsum % 10)) % 10
      
                
    except KeyboardInterrupt:
        print("Exiting the starbase")
        break 
    # 811218-9876