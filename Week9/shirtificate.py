from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()
        self.add_page()

        # Title
        self.set_font("Arial", "B", 40)
        self.cell(0, 40, "CS50 Shirtificate", ln=True, align="C")

        # Add the shirt image
        self.image("shirtificate.png", x=10, w=190)  # Set x position and width to fit A4

        # User's name on top of the shirt
        self.set_font("Arial", "B", 20)
        self.set_text_color(255, 255, 255)
        self.set_xy(40, 140)  # Set x and y position for the name
        self.cell(0, 10, f"{name} took CS50", ln=True, align="C")  # Center align the name

    def save(self, name):
        self.output(name)

# Prompt for user input
name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")
