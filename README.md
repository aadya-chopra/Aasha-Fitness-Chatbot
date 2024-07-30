# Aasha: Your Fitness Guidance Buddy

Aasha is a Streamlit-based chatbot that provides answers to queries about fitness and nutrition. It uses natural language processing (NLP) techniques to understand user inputs and respond appropriately. Aasha also includes a BMI calculator to help users assess their weight category.

# Features

- *Interactive Chat Interface*: Aasha can engage in conversations with users, providing responses to common fitness and nutrition-related questions.
- *BMI Calculator*: Users can calculate their Body Mass Index (BMI) by providing their height and weight.
- *Customizable Intents*: The chatbot's responses are based on defined intents and patterns, which can be easily customized by modifying the `intents.json` file.

# Installation

To run Aasha on your local machine, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/aadya-chopra/aasha-fitness-chatbot.git
   cd aasha-fitness-chatbot
   ```

2. **Install the Required Packages**:

   Make sure you have Python installed. Then, install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Chatbot**:

   Start the Streamlit app:

   ```bash
   streamlit run app.py
   ```

# Usage

Once the application is running, you can interact with Aasha through the chat interface. Simply type your question or request, and Aasha will respond. To use the BMI calculator, follow the prompts to enter your height and weight.

# Customization

The chatbot's responses are determined by the `intents.json` file. You can customize the intents and responses by editing this file. The structure of the file is as follows:

```json
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hello", "Hi", "Hey"],
      "responses": ["Hello!", "Hi there!", "Greetings!"]
    },
    ...
  ]
}
```

# Requirements

- Python 3.7+
- Streamlit
- scikit-learn
- NLTK
- NumPy

# Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.

# Acknowledgements

- [Streamlit](https://streamlit.io/) - Web framework for creating data apps
- [scikit-learn](https://scikit-learn.org/) - Machine learning library
- [NLTK](https://www.nltk.org/) - Natural Language Toolkit
- [NumPy](https://numpy.org/) - Numerical computing library


