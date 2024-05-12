import pandas as pd

def read_tuition_from_excel():
    # Load the Excel file (assuming it's in the same directory as this script)
    try:
        df = pd.read_excel("tuition.xlsx")
    except FileNotFoundError:
        print("Error: The 'tuition.xlsx' file was not found.")
        return None

    # Create a dictionary from the DataFrame
    tuition_dict = dict(zip(df["Program"], df["Tuition"]))

    return tuition_dict

def main():
    tuition_fees = read_tuition_from_excel()
    if tuition_fees:
        program = input("Choose an MSc program (business, economics, finance): ").lower()
        if program in tuition_fees:
            print(f"The tuition fee for {program.capitalize()} is ${tuition_fees[program]:,.2f}")
        else:
            print("Invalid program choice. Please select from business, economics, or finance.")
    else:
        print("Unable to read tuition data. Make sure 'tuition.xlsx' exists in the same directory.")

if __name__ == "__main__":
    main()
