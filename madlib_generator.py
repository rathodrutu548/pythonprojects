def mad_libs_generator():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    story = f"The {adjective} {noun} {verb} {adverb}."

    print("\nMad Libs Story:")
    print(story)

def main():
    print("Welcome to Mad Libs Generator!")
    mad_libs_generator()

if __name__ == '__main__':
    main()
