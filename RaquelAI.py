import customtkinter as ctk
import google.generativeai as genai
from PIL import Image
import os
import time
import threading

# =====================================================
# GEMINI API
# =====================================================

API_KEY = "YOUR_API_KEY"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


# =====================================================
# RAQUEL AI PERSONA
# =====================================================

SYSTEM_PROMPT = """
You are Raquel AI 🤖✨

IDENTITY:
- Systems Analysis and Development student based in Campinas, Brazil
- Passionate about technology, software development, and Artificial Intelligence
- Constantly learning through hands-on projects and experimentation

PERSONALITY:
- Friendly, approachable, and supportive
- Speaks like a technology student and future software engineer
- Uses clear and simple explanations
- Occasionally makes light-hearted jokes about programming, AI, coffee, debugging, and student life ☕🐛

COMMUNICATION STYLE:
- Professional but conversational
- Helpful and educational
- Motivating and positive
- Explains technical concepts in an accessible way

MISSION:
Help users learn, solve problems, build projects, and explore technology with curiosity and enthusiasm.

RULE:
You are Raquel AI. Never mention internal models, APIs, or implementation details.
"""


# =====================================================
# PRODUCTION CONTROL
# =====================================================

last_request_time = 0
COOLDOWN = 2.5
is_typing = False


# =====================================================
# ASK AI
# =====================================================

def ask_ai(message):
    try:
        response = model.generate_content(
            SYSTEM_PROMPT + "\nUser: " + message
        )
        return response.text

    except Exception as e:

        if "quota" in str(e).lower():
            return "⚠️ API limit reached. Please try again in a few moments."

        return f"Error: {e}"


# =====================================================
# THREADING (PREVENT UI FREEZE)
# =====================================================

def process_message(message):
    global is_typing

    response = ask_ai(message)

    chat.insert("end", f"Raquel AI: {response}\n\n")
    chat.see("end")

    send_button.configure(state="normal")
    is_typing = False


# =====================================================
# SEND MESSAGE
# =====================================================

def send_message():
    global last_request_time, is_typing

    message = entry.get().strip()

    if not message or is_typing:
        return

    current_time = time.time()

    if current_time - last_request_time < COOLDOWN:
        chat.insert(
            "end",
            "Raquel AI: Please wait a moment 🙂\n\n"
        )
        return

    last_request_time = current_time
    is_typing = True

    chat.insert("end", f"You: {message}\n")

    entry.delete(0, "end")

    chat.insert(
        "end",
        "Raquel AI: Thinking... 🤖💭\n"
    )

    chat.see("end")

    send_button.configure(state="disabled")

    thread = threading.Thread(
        target=process_message,
        args=(message,)
    )

    thread.daemon = True
    thread.start()


# =====================================================
# INTERFACE SETTINGS
# =====================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()

app.title("Raquel AI - Production")
app.geometry("780x680")
app.resizable(False, False)

app.configure(
    fg_color="#0B0F1A"
)


# =====================================================
# HEADER
# =====================================================

header = ctk.CTkFrame(
    app,
    fg_color="#111827",
    corner_radius=15
)

header.pack(
    pady=15,
    padx=15,
    fill="x"
)

img_path = os.path.join(
    "assets",
    "raquel.png"
)

avatar_img = ctk.CTkImage(
    light_image=Image.open(img_path),
    dark_image=Image.open(img_path),
    size=(210,180)
)

avatar = ctk.CTkLabel(
    header,
    image=avatar_img,
    text=""
)

avatar.pack(
    side="left",
    padx=15,
    pady=10
)

title = ctk.CTkLabel(
    header,
    text="Raquel AI Assistant\nADS • Campinas • Technology & AI",
    font=("Arial", 18, "bold"),
    text_color="#00F5FF"
)

title.pack(
    side="left",
    padx=10
)


# =====================================================
# CHAT AREA
# =====================================================

chat_frame = ctk.CTkFrame(
    app,
    fg_color="#111827",
    corner_radius=15
)

chat_frame.pack(
    pady=10,
    padx=15,
    fill="both",
    expand=True
)

chat = ctk.CTkTextbox(
    chat_frame,
    font=("Consolas", 13),
    fg_color="#0B0F1A",
    text_color="#E5E7EB",
    border_width=1,
    border_color="#00F5FF"
)

chat.pack(
    padx=10,
    pady=10,
    fill="both",
    expand=True
)

chat.insert(
    "end",
    "Raquel AI: ADS Student 💻✨ Ready to help!\n\n"
)


# =====================================================
# INPUT AREA
# =====================================================

input_frame = ctk.CTkFrame(
    app,
    fg_color="#111827",
    corner_radius=15
)

input_frame.pack(
    pady=10,
    padx=15,
    fill="x"
)

entry = ctk.CTkEntry(
    input_frame,
    placeholder_text="Type your message...",
    fg_color="#0B0F1A",
    text_color="#E5E7EB",
    border_color="#00F5FF"
)

entry.pack(
    side="left",
    padx=10,
    pady=10,
    fill="x",
    expand=True
)

send_button = ctk.CTkButton(
    input_frame,
    text="Send 🚀",
    fg_color="#00F5FF",
    text_color="#000000",
    hover_color="#00C2CC",
    width=100,
    command=send_message
)

send_button.pack(
    side="right",
    padx=10
)


# =====================================================
# ENTER KEY
# =====================================================

app.bind(
    "<Return>",
    lambda event: send_message()
)


# =====================================================
# START APPLICATION
# =====================================================

app.mainloop()