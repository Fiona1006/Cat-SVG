import tkinter as tk
import svgwrite
import math

def generate_svg():
    # Get values from entry widgets
    body_width = int(body_width_entry.get())
    body_length = int(body_length_entry.get())
    length = int(head_radius_entry.get())
    head_width = int(width.get())
    ear_height = int(ear_height_entry.get())
    eye_radius = int(eye_radius_entry.get())
    nose_size = int(nose_size_entry.get())
    mouth_width = int(mouth_width_entry.get())
    tail_length = int(tail_length_entry.get())

    # Create an SVG drawing
    dwg = svgwrite.Drawing('realistic_cat.svg', profile='full')

    # Calculate center of the screen
    center_x = 500
    center_y = 500

    # Draw the cat body (ellipse)
    cat_body = dwg.ellipse(center=(center_x, center_y), r=(body_width / 2, body_length / 2),
                           stroke=svgwrite.rgb(0, 0, 0, '%'), fill='white')
    dwg.add(cat_body)

    # Draw the cat head (circle)
    cat_head = dwg.rect((center_x-head_width/2, center_y - body_length / 2 - length), size=(head_width, length),stroke=svgwrite.rgb(0, 0, 0, '%'), fill='white')
    dwg.add(cat_head)

    # Draw the cat ears (triangles)
    left_ear = dwg.polygon(points=[(center_x - head_width/4, center_y - body_length / 2 - length - ear_height),
                                   (center_x - head_width/ 4+ ear_height*math.sqrt(3)/4, center_y - body_length / 2 - length),
                                   (center_x-head_width/4 - ear_height*math.sqrt(3)/4, center_y - body_length / 2 - length)],
                           stroke=svgwrite.rgb(0, 0, 0, '%'), fill='white')
    right_ear = dwg.polygon(points=[(center_x + head_width/4, center_y - body_length / 2 - length - ear_height),
                                    (center_x + head_width/ 4+ ear_height*math.sqrt(3)/4, center_y - body_length / 2 - length),
                                    (center_x+head_width/ 4- ear_height*math.sqrt(3)/4, center_y - body_length / 2 - length)],
                            stroke=svgwrite.rgb(0, 0, 0, '%'), fill='white')
    dwg.add(left_ear)
    dwg.add(right_ear)

    # Draw the cat eyes (ellipses)
    left_eye = dwg.ellipse(center=(center_x - head_width / 4, center_y - body_length / 2 - length / 2),
                           r=(eye_radius/2, eye_radius/2),
                           stroke=svgwrite.rgb(0, 0, 0, '%'), fill='white')
    right_eye = dwg.ellipse(center=(center_x + head_width / 4, center_y - body_length / 2 - length / 2),
                            r=(eye_radius/2, eye_radius/2),
                            stroke=svgwrite.rgb(0, 0, 0, '%'), fill='white')
    dwg.add(left_eye)
    dwg.add(right_eye)

    # Draw the cat nose (triangle)
    cat_nose = dwg.polygon(points=[(center_x, center_y - body_length / 2 - length / 2),
                                   (center_x - nose_size, center_y - body_length / 2 - length / 2 + nose_size),
                                   (center_x + nose_size, center_y - body_length / 2 - length / 2 + nose_size)],
                           stroke=svgwrite.rgb(0, 0, 0, '%'), fill='white')
    dwg.add(cat_nose)

    # Draw the cat mouth (path)
    mouth_path = dwg.path(d="M {} {} Q {} {} {} {}".format(center_x - mouth_width / 2,
                                                            center_y - body_length / 2 - length/4,
                                                            center_x, center_y - body_length / 2 - length / 4 + mouth_width,
                                                            center_x + mouth_width / 2, center_y - body_length / 2 - length / 4),
                          stroke=svgwrite.rgb(0, 0, 0, '%'), fill='white')
    dwg.add(mouth_path)

    # Draw the cat tail (line)
    tail_start = (center_x + body_width / 2, center_y)
    tail_end = (center_x + body_width / 2 + tail_length, center_y - tail_length)
    cat_tail = dwg.line(start=tail_start, end=tail_end, stroke=svgwrite.rgb(0, 0, 0, '%'))
    dwg.add(cat_tail)

    # Save the SVG file
    dwg.save()
    result_label.config(text="SVG generated successfully!")

# Create the main window
window = tk.Tk()
window.title("Realistic Cat Generator")

# Create entry widgets for cat parts sizes
body_width_label = tk.Label(window, text="Body Width:")
body_width_label.grid(row=0, column=0, padx=10, pady=10)
body_width_entry = tk.Entry(window)
body_width_entry.grid(row=0, column=1, padx=10, pady=10)

body_length_label = tk.Label(window, text="Body Length:")
body_length_label.grid(row=1, column=0, padx=10, pady=10)
body_length_entry = tk.Entry(window)
body_length_entry.grid(row=1, column=1, padx=10, pady=10)

head_radius_label = tk.Label(window, text="Head_length:")
head_radius_label.grid(row=2, column=0, padx=10, pady=10)
head_radius_entry = tk.Entry(window)
head_radius_entry.grid(row=2, column=1, padx=10, pady=10)

width = tk.Label(window, text="Head width:")
width.grid(row=3, column=0, padx=10, pady=10)
width = tk.Entry(window)
width.grid(row=3, column=1, padx=10, pady=10)

ear_height_label = tk.Label(window, text="Ear Height:")
ear_height_label.grid(row=4, column=0, padx=10, pady=10)
ear_height_entry = tk.Entry(window)
ear_height_entry.grid(row=4, column=1, padx=10, pady=10)

eye_radius_label = tk.Label(window, text="Eye Radius:")
eye_radius_label.grid(row=5, column=0, padx=10, pady=10)
eye_radius_entry = tk.Entry(window)
eye_radius_entry.grid(row=5, column=1, padx=10, pady=10)

nose_size_label = tk.Label(window, text="Nose Size:")
nose_size_label.grid(row=6, column=0, padx=10, pady=10)
nose_size_entry = tk.Entry(window)
nose_size_entry.grid(row=6, column=1, padx=10, pady=10)

mouth_width_label = tk.Label(window, text="Mouth Width:")
mouth_width_label.grid(row=7, column=0, padx=10, pady=10)
mouth_width_entry = tk.Entry(window)
mouth_width_entry.grid(row=7, column=1, padx=10, pady=10)

tail_length_label = tk.Label(window, text="Tail Length:")
tail_length_label.grid(row=8, column=0, padx=10, pady=10)
tail_length_entry = tk.Entry(window)
tail_length_entry.grid(row=8, column=1, padx=10, pady=10)

# Create a button to generate SVG
generate_button = tk.Button(window, text="Generate Cat", command=generate_svg)
generate_button.grid(row=9, column=0, columnspan=2, pady=10)

# Display result label
result_label = tk.Label(window, text="")
result_label.grid(row=10, column=0, columnspan=2, pady=10)

# Start the GUI main loop
window.mainloop()
