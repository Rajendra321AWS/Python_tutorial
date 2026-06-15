"""Program to denonstrate the split() method."""

def main():
    """Read a sentence and split it into words."""
    text = input("Enter a sentence: ")

    words = text.split()

    print("words:", words)
    print("Number of words: ", len(words))

if __name__ == "__main__":
    main()
