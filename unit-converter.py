def convert_unit(value, from_unit, to_unit):
    # Length conversions
    length_units = {
        'mm': 1,
        'cm': 10,
        'm': 1000
    }
    
    # Weight conversions
    weight_units = {
        'gram': 1,
        'kg': 1000
    }
    
    if from_unit in length_units and to_unit in length_units:
        return value * length_units[from_unit] / length_units[to_unit]
    elif from_unit in weight_units and to_unit in weight_units:
        return value * weight_units[from_unit] / weight_units[to_unit]
    else:
        return None

def main():
    print("Unit Converter")
    
    while True:
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from (mm/cm/m/gram/kg): ").lower()
        to_unit = input("Enter the unit to convert to (mm/cm/m/gram/kg): ").lower()
        
        result = convert_unit(value, from_unit, to_unit)
        
        if result is not None:
            print(f"{value} {from_unit} is equal to {result} {to_unit}")
        else:
            print("Error: Invalid unit conversion. Please check your input.")
        
        another = input("Do you want to perform another conversion? (yes/no): ").lower()
        if another != 'yes':
            break
    
    print("Thank you for using the Unit Converter!")

if __name__ == "__main__":
    main()
