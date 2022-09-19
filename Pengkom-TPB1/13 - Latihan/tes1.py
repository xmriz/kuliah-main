char = 'z'
huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(len(huruf)):
    if char == 'z':
        char = 'a' 
    elif char == huruf[i]:
        char = huruf[i+1]
        break

print(char)