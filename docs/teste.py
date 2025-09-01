from ipywidgets import FloatText, Dropdown, VBox, HBox, Button, Output, Layout
from IPython.display import display

# Define the available units
available_units = ['g', 'mg', 'ug', 'L', 'ml', 'gota']

# Create input widgets for package units with adjusted layout
# Increasing the width of the description area specifically with a fixed value
package_value_input = FloatText(description='Valor da Embalagem:', layout=Layout(description_width='200px'))
package_numerator_unit_dropdown = Dropdown(options=available_units, description='Unidade Numerador:', layout=Layout(description_width='150px'))
package_denominator_unit_dropdown = Dropdown(options=available_units, description='Unidade Denominador:', layout=Layout(description_width='150px'))

# Create input widgets for patient receipt with adjusted layout
# Increasing the width of the description area specifically with a fixed value
receipt_value_input = FloatText(description='Valor da Receita:', layout=Layout(description_width='200px'))
receipt_unit_dropdown = Dropdown(options=available_units, description='Unidade da Receita:', layout=Layout(description_width='1500px'))

# Create a button to trigger the conversion
convert_button = Button(description='Converter')

# Create an output widget to display the result
output_area = Output()

# Arrange the widgets in HBoxes and a VBox
# Adjusting the layout of HBoxes to allow widgets to take necessary space
input_widgets = VBox([
    HBox([package_value_input, package_numerator_unit_dropdown, package_denominator_unit_dropdown], layout=Layout(width='100%')),
    HBox([receipt_value_input, receipt_unit_dropdown], layout=Layout(width='100%')),
    convert_button
])

display(input_widgets, output_area)