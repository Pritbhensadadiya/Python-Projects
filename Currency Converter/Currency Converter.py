# Currency Converter (INR Based, Bi-directional)

# Updated Dictionary of currency with conversion rates (from INR)
dic = {
    "Argentine Peso": 15.888759,
    "Australian Dollar": 0.017047,
    "Bahraini Dinar": 0.004236,
    "Botswana Pula": 0.151667,
    "Brazilian Real": 0.060204,
    "British Pound": 0.008336,
    "Bruneian Dollar": 0.014461,
    "Bulgarian Lev": 0.018688,
    "Canadian Dollar": 0.015577,
    "Chilean Peso": 10.768563,
    "Chinese Yuan Renminbi": 0.080118,
    "Colombian Peso": 43.331058,
    "Czech Koruna": 0.231548,
    "Danish Krone": 0.071324,
    "Emirati Dirham": 0.041375,
    "Euro": 0.009555,
    "Hong Kong Dollar": 0.087600,
    "Hungarian Forint": 3.719181,
    "Icelandic Krona": 1.362494,
    "Indonesian Rupiah": 187.616412,
    "Iranian Rial": 473.686380,
    "Israeli Shekel": 0.037668,
    "Japanese Yen": 1.664999,
    "Kazakhstani Tenge": 6.129380,
    "Kuwaiti Dinar": 0.003439,
    "Libyan Dinar": 0.060810,
    "Malaysian Ringgit": 0.047301,
    "Mauritian Rupee": 0.510607,
    "Mexican Peso": 0.206507,
    "Nepalese Rupee": 1.600750,
    "New Zealand Dollar": 0.019209,
    "Norwegian Krone": 0.111447,
    "Omani Rial": 0.004335,
    "Pakistani Rupee": 3.191502,
    "Philippine Peso": 0.644944,
    "Polish Zloty": 0.040656,
    "Qatari Riyal": 0.041009,
    "Romanian New Leu": 0.048516,
    "Russian Ruble": 0.941985,
    "Saudi Arabian Riyal": 0.042248,
    "Singapore Dollar": 0.014461,
    "South African Rand": 0.195030,
    "South Korean Won": 15.710100,
    "Sri Lankan Rupee": 3.407286,
    "Swedish Krona": 0.105072,
    "Swiss Franc": 0.008929,
    "Taiwan New Dollar": 0.340965,
    "Thai Baht": 0.358759,
    "Trinidadian Dollar": 0.076425,
    "Turkish Lira": 0.466210,
    "US Dollar": 0.011266
}

print("🌍 Welcome to INR Currency Converter!")

currency_list = list(dic.keys())

while True:
    print("\nChoose Conversion Mode:")
    print("1. INR ➝ Foreign Currency")
    print("2. Foreign Currency ➝ INR")
    print("3. Exit")

    try:
        mode = int(input("\nEnter choice: "))

        if mode == 3:
            print("Exiting the Currency Converter. Goodbye!")
            break

        elif mode == 1:  # INR to Foreign
            print("\nAvailable currency options:\n")
            for i, curr in enumerate(currency_list, start=1):
                print(f"{i}. {curr}")
            print(f"{len(currency_list) + 1}. Back")

            choice = int(input("\nEnter your choice (number): "))

            if choice == len(currency_list) + 1:
                continue
            if 1 <= choice <= len(currency_list):
                amount = float(input("\nEnter the amount in INR: "))
                selected_currency = currency_list[choice - 1]
                converted = amount * dic[selected_currency]
                print(f"\n✅ {amount} INR = {converted:.2f} {selected_currency}")
            else:
                print("❌ Invalid choice!")

        elif mode == 2:  # Foreign to INR
            print("\nAvailable currency options:\n")
            for i, curr in enumerate(currency_list, start=1):
                print(f"{i}. {curr}")
            print(f"{len(currency_list) + 1}. Back")

            choice = int(input("\nEnter your choice (number): "))

            if choice == len(currency_list) + 1:
                continue
            if 1 <= choice <= len(currency_list):
                amount = float(input(f"\nEnter the amount in {currency_list[choice - 1]}: "))
                selected_currency = currency_list[choice - 1]
                converted = amount / dic[selected_currency]
                print(f"\n✅ {amount} {selected_currency} = {converted:.2f} INR")
            else:
                print("❌ Invalid choice!")

        else:
            print("❌ Invalid option, choose 1, 2, or 3.")

    except ValueError:
        print("❌ Please enter a valid number.")
