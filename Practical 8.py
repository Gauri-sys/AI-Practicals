import re


class AdvancedAIChatbot:
    def __init__(self):
        self.history = []
        # Predefined rule-base for automated pattern matching (NLP simulation)
        self.rules = {
            r'\b(hi|hello|hey)\b': "Hello! Welcome to your AI & Python Assistant. How can I help you learn today?",
            r'\b(capabilities|what can you do)\b': "I can assist with AI concepts (BFS, DFS, ML), Python programming FAQs, conversation memory management, and interactive prompts.",
            r'\b(bfs|dfs|difference)\b': (
                "BFS explores level-by-level using a Queue (FIFO) and guarantees\n"
                "the shortest path in unweighted graphs. DFS explores depth-first\n"
                "using a Stack (LIFO) / recursion and uses less memory."
            ),
            r'\b(machine learning|ml)\b': (
                "Machine Learning is a subset of AI where systems learn from data\n"
                "to improve performance without explicit programming."
            ),
            r'\b(help|usage)\b': "Select any menu option from 1 to 10. Type numbers corresponding to the menu or use option 7 for custom text queries."
        }

    def display_menu(self):
        print("\n============================================================")
        print("        ADVANCED AI & PYTHON ASSISTANT CHATBOT")
        print("============================================================")
        print("MAIN MENU:")
        print("    1. Greetings & Introduction      6. Help & Usage")
        print("    2. Bot Capabilities              7. Custom NLP Pattern Match")
        print("    3. AI & Python Study Help        8. View Conversation History")
        print("    4. General Knowledge FAQ         9. Reset History")
        print("    5. Interactive Quiz Mode        10. Exit")
        print("------------------------------------------------------------")

    def process_pattern(self, text):
        for pattern, response in self.rules.items():
            if re.search(pattern, text, re.IGNORECASE):
                return response
        return "I haven't been programmed with a rule for that specific pattern yet."

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter Choice (1-10): ").strip()
            print("------------------------------------------------------------")

            if choice == '1':
                print("User: Hello")
                res = self.process_pattern("hello")
                print(f"Bot:    {res}")
                self.history.append(f"[{len(self.history)+1}] Choice 1: Greeting provided.")

            elif choice == '2':
                print("User: What are your capabilities?")
                res = self.process_pattern("capabilities")
                print(f"Bot:    {res}")
                self.history.append(f"[{len(self.history)+1}] Choice 2: Capabilities explained.")

            elif choice == '3':
                print("User: Explain the difference between BFS and DFS.")
                res = self.process_pattern("bfs dfs")
                print(f"Bot:    {res}")
                self.history.append(f"[{len(self.history)+1}] Choice 3: BFS vs DFS explanation provided.")

            elif choice == '4':
                print("User: What is Machine Learning?")
                res = self.process_pattern("machine learning")
                print(f"Bot:    {res}")
                self.history.append(f"[{len(self.history)+1}] Choice 4: General FAQ answered.")

            elif choice == '5':
                print("Quiz Mode: Which graph search algorithm uses a FIFO queue?")
                print("Options: (A) Depth-First Search (DFS)     (B) Breadth-First Search (BFS)")
                ans = input("Your Answer (A/B): ").strip().upper()
                if ans == 'B':
                    print("Bot:    Correct! BFS utilizes a FIFO queue.")
                else:
                    print("Bot:    Incorrect. BFS uses a FIFO queue, whereas DFS uses a LIFO stack.")
                self.history.append(f"[{len(self.history)+1}] Choice 5: Interactive quiz completed.")

            elif choice == '6':
                print("User: How do I use this chat assistant?")
                res = self.process_pattern("help")
                print(f"Bot:    {res}")
                self.history.append(f"[{len(self.history)+1}] Choice 6: Help info displayed.")

            elif choice == '7':
                query = input("Enter Custom Query: ").strip()
                print(f"User: {query}")
                res = self.process_pattern(query)
                print(f"Bot:    [Pattern Matched] {res}")
                self.history.append(f"[{len(self.history)+1}] Choice 7: Custom Query -> '{query}'")

            elif choice == '8':
                print("--- CONVERSATION HISTORY ---")
                if not self.history:
                    print("    [No conversation history recorded yet.]")
                else:
                    for item in self.history:
                        print(f"    {item}")

                print("============================================================")

            elif choice == '9':
                self.history.clear()
                print("Bot: Conversation history has been reset successfully.")

            elif choice == '10':
                print("Bot: Exiting chatbot session. Thank you!")
                print("============================================================")
                break

            else:
                print("ERROR: Invalid selection! Please enter a valid number between 1 and 10.")

            input("\nPress Enter to return to the Main Menu...")


if __name__ == "__main__":
    chatbot = AdvancedAIChatbot()
    chatbot.run()