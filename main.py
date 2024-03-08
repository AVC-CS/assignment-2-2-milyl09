def main():
    
    ##################################################
    # Comlete your code here
    #Use the same variables: celsius fahrenheit 
    ##################################################
    celsius = float (input('enter a temperature in Celsius: '))
    
    fahrenheit = (celsius * 1.8) + 32

    print (f'celsius \t {fahrenheit:.2f}')

    
    ########################################
    # Do not delete the return statement
    ########################################
    
    return celsius, fahrenheit


if __name__ == '__main__':
    main()
