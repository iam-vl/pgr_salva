entries = [
    # {"content": "Today I started learbing programming.", "date": "01-01-2020"},
    # {"content": "I created my first SQLite database!", "date": "02-01-2020"},
    # {"content": "I finished writing my programming diary app.", "date": "03-01-2020"},
    # {"content": "Today I'm gonna continue learning programming!", "date": "04-01-2020"},
]

def add_entry(entry_content, entry_date):
    
    entries.append({"content": entry_content, "date": entry_date})


def get_entries():
    return entries