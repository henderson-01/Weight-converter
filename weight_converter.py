# My Weight converter.


def convert_weight():
    try:
        weight = float(input("\nEnter your weight: "))
    except ValueError:
        print("Oops! Please enter a valid number for the weight.")
        return

    unit = input("Kilograms or Pounds (K or P): ").strip().upper()

    if unit == "K":
        converted = weight * 2.205
        result = f"{converted:.2f} Pounds"
    elif unit == "P":
        converted = weight / 2.205
        result = f"{converted:.2f} Kgs"
    else:
        print(f"'{unit}' is invalid. Use 'K' or 'P'.")
        return

    print(f"\nYour weight is {result}")
    print("Thank you for using the weight converter. Goodbye... 👋\n")


if __name__ == "__main__":
    convert_weight()
