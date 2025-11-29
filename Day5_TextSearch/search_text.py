import os

def search_in_files(keyword, folder="."):
    keyword = keyword.lower()
    found_any = False

    # Loop through all files in the folder
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    lines = f.readlines()
            except Exception:
                print(f"Could not read {filename}")
                continue

            matches = []
            for i, line in enumerate(lines):
                if keyword in line.lower():
                    matches.append((i + 1, line.strip()))

            if matches:
                found_any = True
                print(f"\n🔍 Found in {filename}:")
                for line_num, content in matches:
                    print(f"  • Line {line_num}: {content}")

    if not found_any:
        print("\nNo matches found in any .txt files.")

if __name__ == "__main__":
    user_keyword = input("Enter a keyword to search inside files: ")
    search_in_files(user_keyword)
    # updated description commit


