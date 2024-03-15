def solution(number, k):
    
    array = list(map(int,number))    
    
    result = [array[0]]

    n = k

    for i in array[1:]:
        if n :
            if result[-1] >= i:
                result.append(i)
            else :
                for j in result[::-1]:
                    if i > j:
                        result.pop()
                        n -= 1
                        if n == 0 :
                            break
                    else :
                        break

                result.append(i)
        
        else:
            result.append(i)

    result = ''.join(map(str, result))

    if len(number) - k < len(result):
        result = result[:len(result) - (len(number) - k) + 1]

    return result