#--------------------------------------------------------#
#                      MAIN PROGRAM
#--------------------------------------------------------#

# import necessary libraries for GUI
import tkinter as tk
from tkinter import ttk, messagebox

# import custom modules
import contents.calculations
from contents.athlete_class import Athlete
from contents.data import GENDER, TRAINING_PLANS


def main():

    # Main application window
    root = tk.Tk()
    root.title("North Sussex Judo Fee Calculator")

    # Window settings
    root.geometry("450x300")
    root.resizable(False, False)

    # ----------------------------------------------------
    # GUI variables for form
    # ----------------------------------------------------

    name_var = tk.StringVar()
    plan_var = tk.StringVar(value=TRAINING_PLANS[0])
    gender_var = tk.StringVar(value=GENDER[0])
    current_weight_kg_var = tk.StringVar(value="0")
    competitions_entered_var = tk.StringVar(value="0")
    private_coaching_hours_var = tk.StringVar(value="0")

    # ----------------------------------------------------
    # GUI variables for summary
    # ----------------------------------------------------

    summary_name_var = tk.StringVar()
    summary_weight_category_var = tk.StringVar()
    summary_plan_var = tk.StringVar()
    summary_competition_cost_var = tk.StringVar()
    summary_coaching_cost_var = tk.StringVar()
    summary_total_cost_var = tk.StringVar()

    # ----------------------------------------------------
    # Widget lists for hide/show
    # ----------------------------------------------------

    form_widgets = []
    summary_widgets = []

    # ----------------------------------------------------
    # Screen switching
    # ----------------------------------------------------

    def hide_form():
        for widget in form_widgets:
            widget.grid_remove()

    def hide_summary():
        for widget in summary_widgets:
            widget.grid_remove()

    def show_form():
        hide_summary()
        for widget in form_widgets:
            widget.grid()
        root.update_idletasks()

    def show_summary():
        hide_form()
        for widget in summary_widgets:
            widget.grid()
        root.update_idletasks()

    def save_placeholder():
        messagebox.showinfo("Save", "Save functionality not implemented yet.")

    # ----------------------------------------------------
    # Calculation
    # ----------------------------------------------------

    def calculate():

        name = name_var.get()
        if not name:
            messagebox.showerror("Requires name", "Please enter athlete's name.")
            return
        
        try:
            current_weight_kg = float(current_weight_kg_var.get())
            if current_weight_kg <= 0:
                messagebox.showerror("Requires positive number", "Please enter a valid weight.")
                return
        except ValueError:
            messagebox.showerror("Requires a number", "Weight requires a number.")
            return
        
        try:
            competitions_entered = int(competitions_entered_var.get())
            if competitions_entered < 0:
                messagebox.showerror("Requires non-negative number", "Competitions entered cannot be negative.")
                return
        except ValueError:
            messagebox.showerror("Requires a number", "Competitions entered requires a number.")
            return
        
        try:
            private_coaching_hours = float(private_coaching_hours_var.get())
            if private_coaching_hours < 0:
                messagebox.showerror("Requires non-negative number", "Private coaching hours cannot be negative.")
                return
        except ValueError:
            messagebox.showerror("Requires a number", "Private coaching hours requires a number.")
            return
            

        athlete = Athlete(
            name=name_var.get(),
            training_plan=plan_var.get(),
            gender=gender_var.get(),
            current_weight_kg=float(current_weight_kg_var.get()),
            competitions_entered=int(competitions_entered_var.get()),
            private_coaching_hours=float(private_coaching_hours_var.get())
        )

        athlete.plan_fee = contents.calculations.lookup_training_plan(
            athlete.training_plan
        )

        athlete.weight_category = contents.calculations.determine_weight_category(
            contents.calculations.lookup_category_table(athlete.gender),
            athlete.current_weight_kg
        )

        athlete.competition_cost = contents.calculations.calculate_competition_cost(
            athlete.competitions_entered
        )

        athlete.coaching_cost = contents.calculations.calculate_private_coaching(
            athlete.private_coaching_hours
        )

        athlete.total_cost = contents.calculations.calculate_total_cost(
            athlete.plan_fee,
            athlete.competition_cost,
            athlete.coaching_cost
        )

        summary_name_var.set(athlete.name)
        summary_weight_category_var.set(athlete.weight_category)
        summary_plan_var.set(f"£{athlete.plan_fee} ({athlete.training_plan})")
        summary_competition_cost_var.set(
            f"£{athlete.competition_cost} ({athlete.competitions_entered} competitions)"
        )
        summary_coaching_cost_var.set(
            f"£{athlete.coaching_cost} ({athlete.private_coaching_hours} hours)"
        )
        summary_total_cost_var.set(f"£{athlete.total_cost}")

        show_summary()


    # ----------------------------------------------------
    # FORM WIDGETS
    # ----------------------------------------------------

    label_name = ttk.Label(root, text="Name:")
    entry_name = ttk.Entry(root, textvariable=name_var)

    label_gender = ttk.Label(root, text="Gender:")
    optionmenu_gender = ttk.OptionMenu(root, gender_var, gender_var.get(), *GENDER)

    label_weight = ttk.Label(root, text="Current Weight (kg):")
    entry_weight = ttk.Entry(root, textvariable=current_weight_kg_var)

    label_plan = ttk.Label(root, text="Training Plan:")
    optionmenu_plan = ttk.OptionMenu(root, plan_var, plan_var.get(), *TRAINING_PLANS)

    label_comp = ttk.Label(root, text="Competitions Entered:")
    entry_comp = ttk.Entry(root, textvariable=competitions_entered_var)

    label_coach = ttk.Label(root, text="Private Coaching Hours:")
    entry_coach = ttk.Entry(root, textvariable=private_coaching_hours_var)

    button_calculate = ttk.Button(root, text="Calculate", command=calculate)

    # Grid positions
    label_name.grid(row=0, column=0, padx=10, pady=2, sticky="w")
    entry_name.grid(row=0, column=1, padx=10, pady=2)

    label_gender.grid(row=1, column=0, padx=10, pady=2, sticky="w")
    optionmenu_gender.grid(row=1, column=1, padx=10, pady=2)

    label_weight.grid(row=2, column=0, padx=10, pady=2, sticky="w")
    entry_weight.grid(row=2, column=1, padx=10, pady=2)

    label_plan.grid(row=3, column=0, padx=10, pady=2, sticky="w")
    optionmenu_plan.grid(row=3, column=1, padx=10, pady=2)

    label_comp.grid(row=4, column=0, padx=10, pady=2, sticky="w")
    entry_comp.grid(row=4, column=1, padx=10, pady=2)

    label_coach.grid(row=5, column=0, padx=10, pady=2, sticky="w")
    entry_coach.grid(row=5, column=1, padx=10, pady=2)

    button_calculate.grid(row=6, column=0, columnspan=2, pady=10)

    form_widgets.extend([
        label_name, entry_name,
        label_gender, optionmenu_gender,
        label_weight, entry_weight,
        label_plan, optionmenu_plan,
        label_comp, entry_comp,
        label_coach, entry_coach,
        button_calculate
    ])

    # ----------------------------------------------------
    # SUMMARY WIDGETS
    # ----------------------------------------------------

    label_title = ttk.Label(root, text="Summary")

    label_name_title = ttk.Label(root, text="Name:")
    label_name_value = ttk.Label(root, textvariable=summary_name_var)

    label_weight_title = ttk.Label(root, text="Weight Category:")
    label_weight_value = ttk.Label(root, textvariable=summary_weight_category_var)

    label_plan_title = ttk.Label(root, text="Training Plan Cost:")
    label_plan_value = ttk.Label(root, textvariable=summary_plan_var)

    label_comp_title = ttk.Label(root, text="Competition Cost:")
    label_comp_value = ttk.Label(root, textvariable=summary_competition_cost_var)

    label_coach_title = ttk.Label(root, text="Coaching Cost:")
    label_coach_value = ttk.Label(root, textvariable=summary_coaching_cost_var)

    label_total_title = ttk.Label(root, text="Total Cost:")
    label_total_value = ttk.Label(root, textvariable=summary_total_cost_var)

    button_back = ttk.Button(root, text="Go Back", command=show_form)
    button_save = ttk.Button(root, text="Save", command=save_placeholder)

    # Grid summary
    label_title.grid(row=0, column=0, columnspan=2, pady=10)

    label_name_title.grid(row=1, column=0, sticky="w", padx=10)
    label_name_value.grid(row=1, column=1, sticky="w", padx=10)

    label_weight_title.grid(row=2, column=0, sticky="w", padx=10)
    label_weight_value.grid(row=2, column=1, sticky="w", padx=10)

    label_plan_title.grid(row=3, column=0, sticky="w", padx=10)
    label_plan_value.grid(row=3, column=1, sticky="w", padx=10)

    label_comp_title.grid(row=4, column=0, sticky="w", padx=10)
    label_comp_value.grid(row=4, column=1, sticky="w", padx=10)

    label_coach_title.grid(row=5, column=0, sticky="w", padx=10)
    label_coach_value.grid(row=5, column=1, sticky="w", padx=10)

    label_total_title.grid(row=6, column=0, sticky="w", padx=10)
    label_total_value.grid(row=6, column=1, sticky="w", padx=10)

    button_back.grid(row=7, column=0, pady=10)
    button_save.grid(row=7, column=1, pady=10)

    summary_widgets.extend([
        label_title,
        label_name_title, label_name_value,
        label_weight_title, label_weight_value,
        label_plan_title, label_plan_value,
        label_comp_title, label_comp_value,
        label_coach_title, label_coach_value,
        label_total_title, label_total_value,
        button_back, button_save
    ])

    # Start with summary hidden
    hide_summary()

    root.mainloop()


if __name__ == "__main__":
    main()