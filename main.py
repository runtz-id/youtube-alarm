import datetime
import random
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class YouTubeAlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Alarm Clock")

        self.label_time = ttk.Label(root, text="Set Alarm Time (HH:MM):")
        self.label_time.pack(pady=10)

        self.entry_time = ttk.Entry(root)
        self.entry_time.pack(pady=10)

        self.label_urls = ttk.Label(root, text="Paste YouTube URLs (one per line):")
        self.label_urls.pack(pady=10)

        self.text_urls = tk.Text(root, height=5, width=40)
        self.text_urls.pack(pady=10)

        self.set_alarm_button = ttk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_alarm_button.pack(pady=10)

        self.save_urls_button = ttk.Button(root, text="Save URLs", command=self.save_urls_to_file)
        self.save_urls_button.pack(pady=10)

        self.alarm_time = None
        self.youtube_urls = []

    def set_alarm(self):
        alarm_time_str = self.entry_time.get()
        try:
            self.alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")
            self.youtube_urls = self.text_urls.get("1.0", tk.END).splitlines()
            self.run_alarm_clock()
        except ValueError:
            self.show_error("Invalid time format. Please use HH:MM.")

    def run_alarm_clock(self):
        current_time = datetime.datetime.now().time()
        alarm_datetime = datetime.datetime.combine(datetime.date.today(), self.alarm_time.time())

        while current_time < self.alarm_time.time():
            current_time = datetime.datetime.now().time()

        self.show_message("Alarm triggered!")
        self.play_random_video()

    def play_random_video(self):
        if not self.youtube_urls:
            self.show_error("No YouTube URLs provided.")
            return

        random_video_url = random.choice(self.youtube_urls)
        webbrowser.open(random_video_url)

    def save_urls_to_file(self):
        file_path = "youtubelinks .txt"  # Replace with your desired file path
        with open(file_path, "w") as file:
            file.write("\n".join(self.youtube_urls))
        self.show_message(f"URLs saved to {file_path}")

    def show_message(self, message):
        messagebox.showinfo("Alarm Notification", message)

    def show_error(self, message):
        messagebox.showerror("Error", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeAlarmClock(root)
    root.mainloop()
