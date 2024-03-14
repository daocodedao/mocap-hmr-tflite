import bpy
import csv
import os
import math
import mathutils

def convert_csv_to_bvh(csv_file, bvh_file):
    """
    This function converts a CSV file to a BVH (BioVision Hierarchy) file.
    The CSV file should contain motion capture data.
    The function first reads the CSV file and determines the rotation type.
    It then writes the corresponding BVH file with the motion capture data.
    """
    # CSV Data
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if 'Rotation Type' in row:
                rotation_type_index = row.index('Rotation Type')
                if rotation_type_index < len(row) - 1: 
                    rotation_type = row[rotation_type_index + 1]
                break

        csv_data = list(reader)[8:]
        
    print(f"Rotation Type: {rotation_type}")
    
    frames = csv_data[len(csv_data)-1][0]

    # BVH Data
    with open(bvh_file, 'w') as f:
        f.write("HIERARCHY\n")
        f.write("ROOT Hips\n")
        f.write("{\n")
        f.write("   OFFSET 0.00 0.00 0.00\n")
        f.write("   CHANNELS 6 Xposition Yposition Zposition Xrotation Yrotation Zrotation\n")
        f.write("}\n")
        f.write('MOTION\n')
        f.write('Frames: ' + str(frames) + '\n')
        f.write('Frame Time: 0.100000\n')
        for row in csv_data:
            f.write(str(row[5])+' '+str(row[6])+' '+str(row[7])+' ')
            if rotation_type == 'ZXY':
                f.write(str(row[4])+' '+str(row[2])+' '+str(row[3])+'\n')
            elif rotation_type == 'XYZ':
                f.write(str(row[2])+' '+str(row[3])+' '+str(row[4])+'\n')
            elif rotation_type == 'ZYX':
                f.write(str(row[4])+' '+str(row[3])+' '+str(row[2])+' '+'\n')
            elif rotation_type == 'YXZ':
                f.write(str(row[3])+' '+str(row[2])+' '+str(row[4])+' '+'\n')
            elif rotation_type == 'XZY':
                f.write(str(row[2])+' '+str(row[4])+' '+str(row[3])+' '+'\n')
            elif rotation_type == 'YZX':
                f.write(str(row[3])+' '+str(row[4])+' '+str(row[2])+' '+'\n')
            elif rotation_type == 'Quaternion':
                x = float(row[2])
                y = float(row[3])
                z = float(row[4])
                w = float(row[5])
                quaternion = mathutils.Quaternion((w, x, y, z))
                euler = quaternion.to_euler('XYZ')
                x_rotation = math.degrees(euler.x)
                y_rotation = math.degrees(euler.y)
                z_rotation = math.degrees(euler.z)
                f.write(str(x_rotation)+' '+str(y_rotation)+' '+str(z_rotation)+' '+'\n')

def open_bvh(bvh_file_path):
    """
    This function imports a BVH (BioVision Hierarchy) file into the current Blender scene.
    The BVH file should contain motion capture data.
    """
    bpy.ops.import_anim.bvh(filepath=bvh_file_path)