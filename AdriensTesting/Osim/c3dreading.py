# Let's update the function `write_trc_file` within the code to ensure that it follows OpenSim's .trc file requirements.
# We will reformat it to guarantee single tab separation and ensure marker names align with the expected OpenSim format.

# Replacing the `write_trc_file` function in the provided code with an updated version for correct formatting

updated_code = """
import ezc3d
import numpy as np

# Load your C3D file
c3d = ezc3d.c3d("C:/Users/goper/Files/vsCode/490R/Walking_C3D_files/C07_C3D/C07_Fast_07.c3d")

# Extract marker data
markers = c3d['data']['points']  # Shape: (4, #markers, #frames)
frame_rate = c3d['header']['points']['frame_rate']  # Extracted from the C3D file
marker_names = c3d['parameters']['POINT']['LABELS']['value']  # Extract marker names
marker_units = c3d['parameters']['POINT']['UNITS']['value'][0]

if marker_units == "m":
    markers *= 1000  # Convert to millimeters if data is in meters

def write_trc_file(filename, markers, frame_rate):
    num_frames = markers.shape[2]
    num_markers = markers.shape[1]
    
    with open(filename, 'w') as f:
        # TRC Header
        f.write("PathFileType\t4\t(X/Y/Z)\t{}\n".format(filename))
        f.write("DataRate\tCameraRate\tNumFrames\tNumMarkers\tUnits\n")
        f.write("{:.1f}\t{:.1f}\t{}\t{}\tmm\n".format(frame_rate, frame_rate, num_frames, num_markers))
        
        # Write the time and marker names in header
        f.write("Frame#\tTime")
        for marker in marker_names:
            f.write("\t{}\t\t".format(marker))  # One tab for X, two for Y and Z columns
        f.write("\n")
        
        f.write("\t\t")
        for _ in marker_names:
            f.write("\tX\tY\tZ")  # X/Y/Z headers for each marker
        f.write("\n")
        
        # Write marker data for each frame
        for frame in range(num_frames):
            f.write("{}\t{:.5f}".format(frame + 1, frame / frame_rate))  # Frame number and time
            for marker in range(num_markers):
                x, y, z = markers[:3, marker, frame]  # X, Y, Z positions
                f.write("\t{:.5f}\t{:.5f}\t{:.5f}".format(x, y, z))
            f.write("\n")

write_trc_file("/mnt/data/updated_output.trc", markers, frame_rate)
"""

# Saving the updated code to a new file
updated_file_path = "updated_c3dreading.py"
with open(updated_file_path, "w") as file:
    file.write(updated_code)

updated_file_path
