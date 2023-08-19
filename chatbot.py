import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def process_input(user_input):
    # Process user input using natural language processing techniques
    # Generate appropriate responses based on the input and UI/UX design knowledge
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(user_input)
    filtered_input = [w for w in word_tokens if not w in stop_words]
    processed_input = ' '.join(filtered_input)
    return processed_input

def main():
    print("Welcome to the UI/UX Design Chatbot!")
    print("Ask me anything related to UI/UX design and I'll provide insights and suggestions.")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("User: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        processed_input = process_input(user_input)
        print("Chatbot:", processed_input)

if __name__ == "__main__":
    main()

