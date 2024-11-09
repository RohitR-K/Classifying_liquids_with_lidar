# Loop through each liquid type
for liquid in liquids:
    for i in range(1, 6):
        video_name = f'ubq_{liquid}{i}.mp4'
        video_path = os.path.join(base_dir, liquid, video_name)

        # Create a 'frames' folder if it doesn't exist
        frames_folder = os.path.join(base_dir, liquid, f'blue_frames_{i}')
        os.makedirs(frames_folder, exist_ok=True)

        # Open the video file
        cap = cv2.VideoCapture(video_path)

        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Extract the blue channel
            blue_channel = frame[:, :, 0]

            # Create a new image with only the blue channel containing data
            blue_image = np.zeros_like(frame)
            blue_image[:, :, 0] = blue_channel  # Only populate the blue channel

            # Save the frame as an image file
            frame_filename = os.path.join(frames_folder, f'frame_{frame_count:04d}.png')
            cv2.imwrite(frame_filename, blue_image)

            frame_count += 1

        # Release the video capture object
        cap.release()

        print(f"Processed {video_name}: {frame_count} blue channel frames extracted")

print("All videos processed successfully!")
