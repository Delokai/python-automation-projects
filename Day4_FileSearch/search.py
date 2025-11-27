import os

def search_files(keyword):
    files = os.listdir(".")
    keyword = keyword.lower()

    matches = []

    for filename in files:
        if keyword in filename.lower():   # <--- works for PDF, DOCX, PNG, etc.
            matches.append(filename)

    if matches:
        print("\nFiles found:")
        for m in matches:
            print(f"- {m}")
    else:
        print("\nNo files matched your search.")

if __name__ == "__main__":
    term = input("Enter a word to search for: ")
    search_files(term)
