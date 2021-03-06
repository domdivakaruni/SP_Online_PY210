#!/usr/bin/env python3

"""
Lesson 4: Mail Room Part 4
Course: UW PY210
Author: Jason Jenkins
"""
import pathlib
import sys


def send_thanks():
    """
    Method used to probt donor name or list out donors
    """

    global donor_dict

    response = ""

    while True:
        response = input('Input donors name, "list", or "exit": ').lower()

        if(response == "exit"):
            break
        elif response == "list":
            print_donor_dict()
            print()
        else:
            break

    # For dict
    if(response != "exit"):
        donate(response)


def thank_you_email(donor):
    """
    Thank donor for donation
    """

    print(f"Thank you {donor} for your donation.")


def print_donor_dict():
    """
    Print out the donor list
    """

    global donor_dict

    print("List of donors")
    print("--------------")

    for k in donor_dict.keys():
        print(k)


def donate(donor):
    """
    Prompt donor to donate
    """

    response = 0

    try:
        response = float(input('Input amount to donate or "0" to exit: '))
    except ValueError:
        print("Must input a valid float")
    else:
        if response > 0:
            if donor in donor_dict:
                donor_dict[donor].append(response)
            else:
                donor_dict.update({donor: [response]})
            thank_you_email(donor)


def create_report():
    """
    Create a table like view of donors
    Includes donor name, donation total, total gifts, average gift amount

    Sorted by donation total
    """

    global donor_dict

    # Create new dict sorted by total donated
    sorted_dict = dict(sorted(donor_dict.items(),
                              key=lambda i: sum(i[1]),
                              reverse=True))

    print(f"{'Donor Name':30}|{'Total Given':^16}|", end='')
    print(f"{'Num Gifts':^14}|{'Average Gift':^16}")
    print(f"{'-'*79}")

    for k, v in sorted_dict.items():
        donor_name = k
        donor_total = sum(v)
        donar_count = len(v)
        donor_ave = 0

        if donar_count != 0:
            donor_ave = donor_total / donar_count

        donor_output = f"{donor_name:30}"
        donor_output += f" ${donor_total:15.2f}"
        donor_output += f"{donar_count:15}"
        donor_output += f" ${donor_ave:15.2f}"
        print(donor_output)


def quit_program():
    """
    Method used to quit the program
    """

    sys.exit()


def send_all_thanks():
    """
    Method used to print a letter to the donors
    """

    global donor_dict

    p = pathlib.Path("emails/")
    try:
        p.mkdir(parents=True, exist_ok=True)
    except NameError:
        print("Director not found")
    else:
        for k, v in donor_dict.items():
            dest = f"{p / k}.txt"
            dest = dest.replace(" ", "_").replace(",", "")
            with open(dest, 'w') as outfile:
                outfile.write(f"Dear {k}\n")
                outfile.write(f"\tThank you for your donation of ${sum(v):.2f}.\n")
                outfile.write(f"\tIt will be put to very good use.\n")
                outfile.write(f"Sincerely,\n")
                outfile.write(f"-The Team\n")


def startup_prompt():
    """
    Prombt user for action they what to take
    """
    global menu_dict

    print()
    print("Do you want to:")
    print('   1 - Send a Thank You to a single donor.')
    print('   2 - Create a Report.')
    print('   3 - Send letters to all donors.')
    print('   4 - Quit.')

    response = input("Input numbered option you wish to do: ").strip()

    if response in menu_dict:
        menu_dict[response]()
    else:
        print(f"{response} is not a valid input.")


# Global Variables
donor_dict = dict()
menu_dict = {
    "1": send_thanks,
    "2": create_report,
    "3": send_all_thanks,
    "4": quit_program
}


if __name__ == "__main__":
    # Initial Setup
    donor_dict.update({"william gates": [1345.462]})
    donor_dict.update({"mark zuckerberg": [12546.124, 13445.124]})
    donor_dict.update({"jeff bezos": [1234.123, 12341431.12]})
    donor_dict.update({"paul allen": [734.12, 124.41, 10000]})
    donor_dict.update({"jason jenkins": [10, 20, 30, 40, 50, 60]})

    while True:
        startup_prompt()
