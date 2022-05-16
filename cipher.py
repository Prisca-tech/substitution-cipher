def getName():
    print("Hello, what is your name? ")
    name = str(input(" "))
    print("Hello, name")
    return name
    
    def getInput():

  

    def instantiate():
        x = getInput()
        print("Set encryption parameter: \n What is your prefered number of character jumps? ")
        jumps = int(input( ))
    

    def encrypt():
        x = getInput()

    def decrypt():
      x = getInput()


    def reset():
        x = getInput()

    def history():
        x = getInput()

   # to display a menu
 
print('''
1. Instantiate encryption parameters
2. Encrypt
3. Decrypt text
4. Reset encryption parameters
5. History
''')

choice = int(input("Enter your the number that corresponds with the task you want to perform"))

task = [instantiate, encrypt, decrypt, reset, history]

result = task [choice-1]()

print(result)