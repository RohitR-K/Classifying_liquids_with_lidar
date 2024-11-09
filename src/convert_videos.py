# Loop through each liquid type
for liquid in liquids:
    # Path to the liquid folder
    liquid_folder = os.path.join(base_dir, liquid)

    # Loop through each video file for the liquid
    for i in range(1, 6):
        # Create the input file path
        input_file = os.path.join(liquid_folder, f"ubq_{liquid}{i}.h264")
        # Create the output file path
        output_file = os.path.join(liquid_folder, f"ubq_{liquid}{i}.mp4")

        # Construct the FFmpeg command to convert video
        command = f'ffmpeg -i "{input_file}" -c:v copy "{output_file}" -v debug'

        # Run the command
        result = os.system(command)

        # Check the result and print a message
        if result == 0:
            print(f"Conversion successful for {input_file}. Output saved as: {output_file}")
        else:
            print(f"Conversion failed for {input_file} with error code: {result}")
