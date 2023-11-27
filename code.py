import os
import asyncio
import Converter.create_file
import Converter.converter_code

z=0
current_dir = os.getcwd()
asyncio.run(Converter.create_file.main())
directory_input_path = f"{current_dir}\Input_img"
directory_output_path = f"{current_dir}\Output_img"
for i in os.listdir(directory_input_path):
    z = z + 1
    cr2_path = f'{directory_input_path}\{i}'
    Converter.converter_code.convert_cr2_to_png(cr2_path, directory_output_path, z)