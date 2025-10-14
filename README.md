# pomotoro_focus
⏱️ Pomotoro — A Simple CLI Pomodoro Timer

Pomotoro is a command-line productivity tool designed to help you manage focused work sessions and breaks using the Pomodoro Technique.
I created this as an internal tool to use during my workday as an IT Specialist, where I needed an easy, distraction-free timer to stay focused on deep work tasks right in the terminal.

🚀 Features

✅ Default Focus Session:
Run a standard 25-minute Pomodoro timer.

✅ Custom Focus Session:
Set your own custom duration for focused work.

✅ Break Timer Options:
Choose between a 5-minute default break or define your own custom break time.

✅ Interactive CLI:
Simple text-based menu system with clear prompts and minimal setup.

✅ Seamless Workflow:
Automatically transition between focus and break sessions or choose when to start your break manually.

🧠 What is the Pomodoro Technique?

The Pomodoro Technique is a time management method that uses structured intervals — typically 25 minutes of focused work followed by a 5-minute break — to improve productivity and focus.
After completing four Pomodoros, a longer break (15–30 minutes) is usually taken.

Pomotoro is built around this concept to encourage healthy, consistent work patterns.

⚙️ How to Use

Clone this repository:

git clone https://github.com/achaple0/pomotoro_focus.git
cd pomotoro


Run the program:

python main.py


Follow the prompts:

Choose between running a default focus session or a custom session.

After each session, decide whether to take a break.

You can also launch standalone breaks whenever you like.

💡 Example Workflow
What will you like to do:
1. Run Default Focus Session
2. Run Custom Focus Session
3. Take a break?
4. Quit Program

> 1

[Focus timer begins…]
00:24
...
00:00
Session Completed! Nice work! Would you like to begin your break? y/n

🧩 Project Structure
pomotoro/
├── main.py   # Main CLI script
└── README.md      # Project documentation

🛠️ Built With

Python 3.10+

time — for countdown functionality

divmod() — for clean minute:second conversion

Simple CLI input handling

📈 Possible Future Improvements

🔹 Add sound or notification when a session completes
🔹 Log session history and stats (e.g., total focus time per day)
🔹 Integrate with a task list or productivity tracker
🔹 Add command-line arguments (e.g., --focus 50 --break 10)

👨‍💻 Author

Angel Chaple
💼 IT Specialist | Aspiring Software Developer
📍 Charlotte, NC
🔗 GitHub

🧭 License

This project is open-source under the MIT License.
Feel free to modify and improve it to suit your own workflow.
