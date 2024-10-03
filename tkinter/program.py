#! /usr/bin/env python3

import customtkinter
import json
import os

customtkinter.set_appearance_mode("dark")
app = customtkinter.CTk()
app.title("Alpha")
app.geometry("600x600")

poses = {}
amclPose = "test post"

if os.path.isfile('./poses.json') and os.access('./poses.json', os.R_OK):
    with open('poses.json') as file:
        poses = json.load(file)

def save_location():
    locationName = entry.get()
    poses[locationName] = locationName + ' ' + amclPose
    with open('poses.json', 'w') as file:
        json.dump(poses, file)
    get_goal_buttons()

def send_goal(goalPose):
    print(poses[goalPose])

def get_goal_buttons():
    if os.path.isfile('./poses.json') and os.access('./poses.json', os.R_OK):
        with open('poses.json') as file:
            poses = json.load(file)
            i = 1
            for pose in poses:
                customtkinter.CTkButton(app, text=pose, command=lambda goalPose=pose: send_goal(goalPose)).grid(row=i, column=0, padx=20, pady=20)
                i+=1

button = customtkinter.CTkButton(app, text="Save Location", command=save_location)
button.grid(row=0, column=0, padx=20, pady=20)

entry = customtkinter.CTkEntry(app, placeholder_text="location name")
entry.grid(row=0, column=1, padx=20, pady=20)

get_goal_buttons()

app.mainloop()