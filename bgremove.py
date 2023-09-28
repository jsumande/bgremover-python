from rembg import remove
from PIL import Image

input_path = 'shirt.png' # input file path
output_path = 'output.png' # output file 
# for guidelines 
input = Image.open(input_path)
output = remove(input)
output.save(output_path)