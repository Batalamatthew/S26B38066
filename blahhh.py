"""Clinic patient registration program."""

GENERAL_FEE = 15000
EMERGENCY_FEE = 40000
FOLLOWUP_FEE = 10000
FOLLOWUP_MIN_AGE = 60


def is_followup_allowed(age):
    """Follow-up visits are only allowed for patients aged 60 or above."""
    return age >= FOLLOWUP_MIN_AGE


def get_fee(visit_type, age):
    """Return the consultation fee for the visit type, or -1 if not allowed."""
    visit_type = visit_type.strip().lower()

    if visit_type == "general":
        return GENERAL_FEE
    elif visit_type == "emergency":
        return EMERGENCY_FEE
    elif visit_type in ("follow-up", "followup", "follow up"):
        if is_followup_allowed(age):
            return FOLLOWUP_FEE
        return -1
    return -1  # unknown visit type


def read_positive_int(prompt, minimum, maximum=None):
    """Keep asking until the user enters a valid whole number in range."""
    while True:
        try:
            value = int(input(prompt))
            if value < minimum:
                print(f"  Please enter a number that is at least {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"  Please enter a number that is at most {maximum}.")
                continue
            return value
        except ValueError:
            print("  Invalid input. Please enter a whole number (digits only).")


def main():
    print("=== Clinic Patient Registration ===")

    # 1. Ask how many patients (with try/except via helper)
    num_patients = read_positive_int(
        "How many patients will be registered today? ", minimum=1
    )

    registered = 0
    total_fees = 0

    # 2. for loop over the number of patients
    for i in range(1, num_patients + 1):
        print(f"\n--- Patient {i} of {num_patients} ---")

        name = input("Name: ").strip()
        while not name:
            print("  Name cannot be empty.")
            name = input("Name: ").strip()

        # 5. try/except when reading age
        age = read_positive_int("Age: ", minimum=0, maximum=120)

        visit_type = input("Visit type (General / Emergency / Follow-up): ")

        fee = get_fee(visit_type, age)

        if fee == -1:
            if visit_type.strip().lower() in ("follow-up", "followup", "follow up"):
                print(f"  REJECTED: Follow-up visits are only for age "
                      f"{FOLLOWUP_MIN_AGE}+. {name} is {age}.")
            else:
                print("  REJECTED: Unknown visit type.")
            continue

        registered += 1
        total_fees += fee
        print(f"  Registered: {name}, age {age}, "
              f"{visit_type.strip().title()} visit. Fee: {fee:,} UGX")

    # 6. Final summary
    print("\n=== End of Session Summary ===")
    print(f"Patients successfully registered: {registered}")
    print(f"Total fees collected: {total_fees:,} UGX")


if __name__ == "__main__":
    main()