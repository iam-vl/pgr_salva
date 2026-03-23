from dbase import add_entry, get_entries


menu = """Select one of the following: 
1) Add a new entry. 
2) View the entries. 
3) Quit.  

Your selection: """

def prompt_new_entry():
    entry_content = input("what have you learned today? ")
    entry_date = input("Enter the date: ")
    add_entry(entry_content, entry_date)

def view_entries(entries):
    for entry in entries:
        print(f"{entry['date']}\n{entry['date']}\n\n")


welcome = "Welcome to the programming diary!" 

# user_input = input(menu)  
while (user_input := input(menu)) != "3": 
    if user_input == "1":
        prompt_new_entry()
    if user_input == "2":
        entries = get_entries()
        view_entries(entries)
    else:
        print("Invalid option. Please start again.")


# entries = [
#     {"content": "Today I started learbing programming.", "date": "01-01-2020"},
#     {"content": "I created my first SQLite database!", "date": "02-01-2020"},
#     {"content": "I finished writing my programming diary app.", "date": "03-01-2020"},
#     {"content": "Today I'm gonna continue learning programming!", "date": "04-01-2020"},
# ]