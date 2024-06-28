def minion_game():
    string = input("Enter the string for the game: ").strip().upper()

    vowels = 'AEIOU'
    length = len(string)
    minh_score = 0
    an_score = 0
    minh_substrings = {}
    an_substrings = {}

    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = string[i:j]
            if string[i] in vowels:
                minh_score += 1
                if substring in minh_substrings:
                    minh_substrings[substring] += 1
                else:
                    minh_substrings[substring] = 1
            else:
                an_score += 1
                if substring in an_substrings:
                    an_substrings[substring] += 1
                else:
                    an_substrings[substring] = 1

    print("Minh's substrings and scores:")
    for substring, score in minh_substrings.items():
        print(f"{substring}: {score}")
    print(f"Total score: {minh_score}")

    print("\nAn's substrings and scores:")
    for substring, score in an_substrings.items():
        print(f"{substring}: {score}")
    print(f"Total score: {an_score}")

    if minh_score > an_score:
        print(f"\nMinh wins with {minh_score} points")
    elif an_score > minh_score:
        print(f"\nAn wins with {an_score} points")
    else:
        print("\nIt's a draw!")

# Example usage
minion_game()