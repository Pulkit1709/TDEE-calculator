import tkinter as tk
from tkinter import ttk
from tkinter import Label
from tkinter import PhotoImage
import matplotlib.pyplot as plt
import os

# Define constants and functions
BMR_CONST_MALE = 88.362
BMR_CONST_FEMALE = 447.593
BMR_CONST_HEIGHT = 3.264
BMR_CONST_WEIGHT = 4.799
BMR_CONST_AGE = 5.677

activity_levels = {
    "Sedentary": 1.2,
    "Lightly Active": 1.375,
    "Moderately Active": 1.55,
    "Very Active": 1.725,
    "Super Active": 1.9
}


def calculate_bmr(gender, weight_kg, height_cm, age_years):
    if gender == "Male":
        bmr = BMR_CONST_MALE + (BMR_CONST_WEIGHT * weight_kg) + (BMR_CONST_HEIGHT * height_cm) - (BMR_CONST_AGE * age_years)
    else:
        bmr = BMR_CONST_FEMALE + (BMR_CONST_WEIGHT * weight_kg) + (BMR_CONST_HEIGHT * height_cm) - (BMR_CONST_AGE * age_years)
    return bmr

def calculate_tdee(bmr, activity_level):
    if activity_level in activity_levels:
        tdee = bmr * activity_levels[activity_level]
    else:
        raise ValueError("Invalid activity level")
    return tdee

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

def assess_health_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25.0 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Function to open the result window
def open_result_window(bmr, tdee, bmi, health_status):
    result_window = tk.Toplevel()
    result_window.title("Result")
    result_window.configure(bg="#EDD0FF")  # Set the background color

    # Create labels to display the results
    bmr_label = ttk.Label(result_window, text=f"BMR: {bmr:.2f} calories per day", font=("Bold", 35), background="#EDD0FF")
    tdee_label = ttk.Label(result_window, text=f"TDEE: {tdee:.2f} calories per day", font=("Bold", 35), background="#EDD0FF")
    bmi_label = ttk.Label(result_window, text=f"BMI: {bmi:.2f}", font=("Bold", 35), background="#EDD0FF")
    health_status_label = ttk.Label(result_window, text=f"Health Status: {health_status}", font=("Bold", 35), background="#EDD0FF")


    bmr_label.pack(pady=10)
    tdee_label.pack(pady=10)
    bmi_label.pack(pady=10)
    health_status_label.pack(pady=10)

    # Create a bar graph showing the distribution of activity levels
    plt.figure(figsize=(8, 6))
    activity_labels = list(activity_levels.keys())
    activity_values = [activity_levels[level] for level in activity_labels]

    plt.bar(activity_labels, activity_values, color='red')
    plt.xlabel('Activity Level', fontsize=16)
    plt.ylabel('TDEE Multiplier', fontsize=16)
    plt.title('Distribution of Activity Levels', fontsize=20)
    plt.xticks(rotation=15)  # Rotate the x-axis labels for better readability

    # Save the plot to an image file
    plt.savefig('activity_levels.png', bbox_inches='tight')

    # Display the plot in the result window
    activity_plot_label = ttk.Label(result_window, text="Distribution of Activity Levels:", font=("Bold", 25), background="Silver")
    activity_plot_label.pack(pady=10)

    # Load the saved plot image and display it
    activity_plot_image = tk.PhotoImage(file='activity_levels.png')
    activity_plot_label = ttk.Label(result_window, image=activity_plot_image, background="#EDD0FF")
    activity_plot_label.image = activity_plot_image  # Keep a reference to the image to avoid garbage collection
    activity_plot_label.pack(pady=10)

    # Remove the temporary plot image file
    os.remove('activity_levels.png')





# Function to open the "About Us" window
def open_about_us():
    about_us_window = tk.Toplevel()
    about_us_window.title("About Us")
    
    # Create a label with information about your team or application
    about_us_label = ttk.Label(about_us_window, text="ABOUT US\n\nThis application was created by the \'Tech Gurus\' team.\n\nWe are dedicated to providing useful tools for a healthier lifestyle.\n\nOUR TEAM\n\n1. Pulkit Gambhir-E23CSEU0382\n2. Shivank Bhardwaj-E23CSEU0388\n3. Akshat Tyagi-E23CSEU0363", font=("Bold", 20), wraplength=500,background="#EDA3FF",foreground="Black")
    about_us_label.pack(padx=20, pady=20)
    
    about_us_window.mainloop()

# Function to open the "Contact Us" window
def open_contact_us():
    contact_us_window = tk.Toplevel()
    contact_us_window.title("Contact Us")
    
    # Create labels with contact information
    email_label = ttk.Label(contact_us_window, text="Contact Us:\n\n1.Pulkit Gambhir\ne23cseu0382@bennett.edu.in\n9359946496\n\n2.Shivank Bhardwaj\ne23cseu0388@bennett.edu.in\n7417197576\n\n3.Akshat Tyagi\ne23cseu0363@bennett.edu.in\n7457864704", font=("Bold", 30),background="#EDA3FF",foreground="Black")
    #phone_label = ttk.Label(contact_us_window, text="Phone:\n+91-9359946496\n+91-7417197576\n+91-7457864704", font=("Bold", 30),background="#EDA3FF",foreground="Black")
    
    email_label.pack(padx=20, pady=10)
    #phone_label.pack(padx=20, pady=10)
    
    contact_us_window.mainloop()

# Function to open the main calculator window
def open_calculator():
    cover_window.destroy()  # Close the cover window
    main_window = tk.Tk()
    main_window.title("TDEE Calculator")

   

    # Create a custom color scheme for the main window
    bg_color = "#EDD0FF"
    text_color = "#333333"
    button_color = "red"
    result_color = "#EDD0FF"
    main_window.configure(bg=bg_color)

    # Create input fields and labels with a consistent style
    label_style = ttk.Style()
    label_style.configure("TLabel", background=bg_color, foreground=text_color, font=("Arial", 50))


    gender_label = ttk.Label(main_window, text="Gender (Male/Female):", style="TLabel")
    gender_entry = tk.Entry(main_window, font=("Bold", 40),highlightthickness=4, highlightbackground="black")
    weight_label = ttk.Label(main_window, text="Weight (kg):", style="TLabel")
    weight_entry = tk.Entry(main_window, font=("bold", 40),highlightthickness=4, highlightbackground="black")
    height_label = ttk.Label(main_window, text="Height (cm):", style="TLabel")
    height_entry = tk.Entry(main_window, font=("Bold", 40),highlightthickness=4, highlightbackground="black")
    age_label = ttk.Label(main_window, text="Age (years):", style="TLabel")
    age_entry = tk.Entry(main_window, font=("Bold", 40),highlightthickness=4, highlightbackground="black")
    activity_label = ttk.Label(main_window, text="Activity Level:", style="TLabel")



    


    # Create a custom button style
    button_style = ttk.Style()
    button_style.configure("TButton", background=button_color, font=("Bold", 30, "bold"), relief="raised", borderwidth=3)

    #Create result labels with a custom style
    bmr_result_label = ttk.Label(main_window, text="BMR:", background="#EDA3FF", foreground="Black", font=("Bold", 35))
    tdee_result_label = ttk.Label(main_window, text="TDEE:", background="#EDA3FF", foreground="Black", font=("Bold", 35))
    bmi_result_label = ttk.Label(main_window, text="BMI:", background="#EDA3FF", foreground="Black", font=("Bold", 35))
    health_status_label = ttk.Label(main_window, text="Health Status:", background="#EDA3FF", foreground="Black", font=("Bold",35))


    

    # Function to perform the calculations and open the result window
    def calculate():
        gender = gender_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        activity_level = activity_var.get()

        bmr = calculate_bmr(gender, weight, height, age)
        tdee = calculate_tdee(bmr, activity_level)
        bmi = calculate_bmi(weight, height)
        health_status = assess_health_status(bmi)

        open_result_window(bmr, tdee, bmi, health_status)
        

    # Create a "Calculate" button
    calculate_button = ttk.Button(main_window, text="Calculate", style="TButton", command=calculate)

    # Arrange widgets using the grid layout
    gender_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
    gender_entry.grid(row=0, column=1, padx=10, pady=5)
    weight_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
    weight_entry.grid(row=1, column=1, padx=10, pady=5)
    height_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
    height_entry.grid(row=2, column=1, padx=10, pady=5)
    age_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
    age_entry.grid(row=3, column=1, padx=10, pady=5)
    activity_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

    # Create the activity menu with a larger font size
    activity_var = tk.StringVar(main_window)
    activity_var.set("Sedentary")  # Default value

    # Customize the font style for the menu
 


    activity_var = tk.StringVar(main_window)
    activity_var.set("Sedentary")  # Default value
    activity_menu = ttk.OptionMenu(main_window, activity_var, *activity_levels.keys())
    
    activity_menu.grid(row=4, column=1, padx=20, pady=10)
    activity_menu.config(width=40)
    calculate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)



    # Create buttons to open "About Us" and "Contact Us" windows
    about_us_button = ttk.Button(main_window, text="About Us", style="TButton", command=open_about_us)
    about_us_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    contact_us_button = ttk.Button(main_window, text="Contact Us", style="TButton", command=open_contact_us)
    contact_us_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)



    main_window.mainloop()

# Create the cover window
cover_window = tk.Tk()
cover_window.title("TDEE Calculator")
cover_window.configure(bg="#EDD0FF")


# Create a custom button style for the "START" button
start_button_style = ttk.Style()
start_button_style.configure("TStart.TButton", font=("Bold", 50),foreground="Black",background="white")

# Create a frame for the project name with a 3D effect
project_frame = ttk.Frame(cover_window, relief="raised", borderwidth=10,)
project_frame.pack(pady=10)

# Create a label for the project name
project_label = Label(project_frame, text="Welcome to\nBodyBalance Pro", font=("Bold", 90),foreground="black",background="#EDA3FF")
project_label.pack()

# Create a frame for BY label with a 3D effect
by_frame = ttk.Frame(cover_window, relief="raised", borderwidth=10)
by_frame.pack(pady=10)

# Create a label for BY
by_label = Label(by_frame, text="BY", font=("Bold", 90),foreground="black",background="#EDA3FF")
by_label.pack()

# Create a frame for the team name with a 3D effect
team_frame = ttk.Frame(cover_window, relief="raised", borderwidth=10)
team_frame.pack(pady=10)

# Create a label for the team name
team_label = Label(team_frame, text="TECH GURU'S", font=("Bold", 90),foreground="black",background="#EDA3FF")
team_label.pack()

# Create the "START" button with the custom style
start_button = ttk.Button(cover_window, text="START", command=open_calculator, style="TStart.TButton")
start_button.pack(padx=20, pady=20)



# Start the cover page window
cover_window.mainloop()

cover_window.mainloop()
