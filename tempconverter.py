"""This is a temperatureconverter"""

def main():
    choose = int(input('Choose Unit Celsius(1), Fahrenheit(2), Kelvin(3), Exit(4): '))
    temp = int(input('Input temperature: '))

    if choose == 1:
        print(f'{temp} °C\n')
        CtoF = (temp * 9/5) + 32
        CtoK = temp + 273.15
        print(f'Celsius to Fahrenheit: {CtoF}°F \nCelsius to Kelvin: {CtoK}°K\n')
        main()
    
    elif choose == 2:
        print(f'{temp} °F\n')
        FtoC = (temp - 32) * 5/9
        FtoK = (temp - 32) * 5/9 + 273.15
        print(f'Fahrenheit to Celsius: {FtoC}°C \nFahrenheit ro Kelvin: {FtoK}°K\n')
        main()
    
    elif choose == 3:
        print(f'{temp} °K\n')
        KtoF = (temp - 273.15) * 9/5 + 32
        KtoC = temp - 273.15
        print(f'Kelvin to Fahrenheit: {KtoF}°F \nKelvin ro Celsius: {KtoC}°C\n')
        main()
    
    elif choose == 4:
        exit()
    
    else:
        print('try again')
        main()


if __name__ == '__main__':
    main()
