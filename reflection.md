# Reflection

Student Name:  name
Sudent Email:  email

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`

Working on this assignment helped me learn how to use Python and Streamlit to build interactive web apps. At first, I struggled with understanding how Streamlit works because it reloads the page every time you make a change, which was confusing. But after completing the different parts of the assignment, I started to get the hang of it. The first task was simple—just processing a single input—but the second and third tasks were harder because I had to work with file uploads and keep track of data between sessions.  

One big challenge was handling Excel files. My code kept failing because I didn’t have the right library installed. After some research, I realized I needed to install `openpyxl` using pip. Once I did that, the code worked, and I learned how important it is to check for dependencies. I also improved my error handling so the app gives clear messages when something goes wrong, like telling the user to install missing packages.  

Overall, this project taught me how to build a functional web app, debug problems, and handle different file types. The most valuable lesson was learning to persist data across sessions using `st.session_state`, which will be useful for future projects. Next time, I’d like to add more features, like better data filtering or visualizations, to make the app even more user-friendly. Even though it was frustrating at times, solving these problems helped me grow as a programmer.