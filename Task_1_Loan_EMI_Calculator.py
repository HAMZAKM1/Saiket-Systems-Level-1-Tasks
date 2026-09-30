def calculate_emi(principal: float, annual_rate_percent: float, tenure_months: int) -> float:
    """
    Calculates the Equated Monthly Installment (EMI) for a loan.
    Formula: EMI = P * R * (1 + R)^N / ((1 + R)^N - 1)
    """
    if principal <= 0 or tenure_months <= 0:
        raise ValueError("Principal and tenure must be strictly greater than zero.")
    
    if annual_rate_percent == 0:
        return principal / tenure_months

    r = (annual_rate_percent / 12) / 100
    n = tenure_months

    emi = (principal * r * ((1 + r) ** n)) / (((1 + r) ** n) - 1)
    return emi


def main():
    print("=" * 45)
    print("        LOAN EMI CALCULATOR (LEVEL 1)        ")
    print("=" * 45)

    try:
        principal = float(input("Enter Principal Amount (P) [e.g., 500000]: "))
        annual_rate = float(input("Enter Annual Interest Rate (%) [e.g., 8.5]: "))
        tenure_months = int(input("Enter Loan Tenure in Months (N) [e.g., 60]: "))

        emi = calculate_emi(principal, annual_rate, tenure_months)
        total_payment = emi * tenure_months
        total_interest = total_payment - principal

        print("\n" + "-" * 45)
        print("                LOAN SUMMARY                 ")
        print("-" * 45)
        print(f"Principal Loan Amount : ₹{principal:,.2f}")
        print(f"Annual Interest Rate  : {annual_rate:.2f}%")
        print(f"Tenure                : {tenure_months} months ({tenure_months / 12:.1f} years)")
        print(f"Monthly EMI           : ₹{emi:,.2f}")
        print(f"Total Interest Payable: ₹{total_interest:,.2f}")
        print(f"Total Amount Payable  : ₹{total_payment:,.2f}")
        print("-" * 45)

    except ValueError as e:
        print(f"\nError: Invalid input! {e}")

if __name__ == "__main__":
    main()