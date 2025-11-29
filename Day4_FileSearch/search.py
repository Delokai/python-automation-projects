import os

def search_files(keyword):
    keyword = keyword.lower()
    files = os.listdir(".")

    matches = [f for f in files if keyword in f.lower()]

    if matches:
        print("\nFiles found:")
        for file in matches:
            print(f"- {file}")
    else:
        print("\nNo files found matching your search.")

if __name__ == "__main__":
    term = input("Enter a word to search for: ")
    search_files(term)

