import bpy
import bmesh
import math
import os
import random
from math import pi
from math import radians
import time
#import cv2
import numpy as np
import re
##################################################################################




def listFiles(dir, ext):
    fileList = []

    # for file in os.listdir(currentDir):
    for file in os.listdir(dir):
        if file[-len(ext):] == ext:
            fileList.append(file)
#    print("File List: ")
#    print(fileList)
    return fileList


def getvars(resx, resy):
    # Martin made function randmoze the head position and keep it inbounds, automartically changes with resolution
    x = random.randrange(-int(resx * .45), int(resx * .45))
    y = random.randrange(-int(resy * .45), int(resy * .45))
    rx = random.randrange(-40, 41, 1)
    ry = random.randrange(0, 181, 10)
    rz = random.randrange(-5, 6, 1)
    scaleFactor = random.uniform(0.0002, 0.0005)
    #scaleFactor = 0.0002
    numList = [x, y, rx, ry, rz, scaleFactor]

    return numList


# Martin - turned the old script into the function that generates camo head and camo background
def camo_images(x, y, rx, ry, rz, infile, fore_head_object_path, log_path, path, negative_enabled, renderRes_x,
                renderRes_y, scaleFactor, start):

    original_img_path = path + "/outputFiles/"
    negative_img_path = path + "/outputFilesneg/"

    objs = bpy.data.objects

    f = open(path + '/imglog.txt', 'a')

    imgNum = start  # + len(listFiles(dir=path + "/outputFiles/", ext='.jpg'))
    print(imgNum)
    f.write("img" + str(imgNum) + " ")
    whichBG = random.randint(0, 1)
    if whichBG == 0:
        backgrTexPath = path + "/background1/"
        foregroundTextures = path + "/foreground1/"

        f.write("fruit ")
    else:
        backgrTexPath = path + "/background2/"
        foregroundTextures = path + "/foreground2/"

        f.write("tree ")

    ################################################################################
    # Select a random background
    backgroundsList = listFiles(dir=backgrTexPath, ext='.jpg')
    randFile = random.randint(0, len(backgroundsList) - 1)
    backgrTexName = backgroundsList[randFile]  # Randomly select a background texture

    f.write("bg" + str(randFile) + " ")

    #################################################################################################################
    # Select a random foreground(object) texture
    objTexName = backgrTexName  # set equal to make sure we definitely fall into the while loop and randomly select a foreground
    foregroundsList = listFiles(dir=foregroundTextures, ext='.jpg')

    while objTexName == backgrTexName:
        randFile = random.randint(0, len(foregroundsList) - 1)
        objTexName = foregroundsList[
            randFile]  # randomly select a foreground texture that is NOT named the same as the background (i.e. not the same image)
    f.write("fg" + str(randFile) + " ")
    outfiletype = ".png"

#    print(infile)
    f.write("X" + str(x) + " ")
    f.write("Y" + str(y) + " ")
    ##################################################################################
    # Remove all existing objects in the scene
    scene = bpy.context.scene
    for ob in scene.objects:
        ob.select = True
    bpy.ops.object.delete()

    ##################################################################################
    # Import face .obj file
    full_path_to_file = (fore_head_object_path + infile)

    bpy.ops.import_scene.obj(filepath=full_path_to_file, \
                             filter_glob="*.obj",
                             use_edges=True, \
                             use_smooth_groups=True, \
                             use_split_objects=False, \
                             use_split_groups=False,
                             use_groups_as_vgroups=False, \
                             use_image_search=False, \
                             split_mode='ON', \
                             global_clamp_size=0.0, \
                             axis_forward='-Z', \
                             axis_up='Y')

    #################################################################################
    bpy.data.objects[0].name = 'FaceObject'
    # print(bpy.data.objects[0].name)

    #################################################################################
    face_obj = bpy.data.objects["FaceObject"]

    face_obj.location = (0.0, y / renderRes_y, -x / renderRes_y)

    f.write("sf" + str(scaleFactor) + " ")
    face_obj.scale = (scaleFactor, scaleFactor, scaleFactor)

    ##################################################################################
    # Now the Background imagePlane
    bpy.ops.wm.addon_enable(module='io_import_images_as_planes')
    bpy.ops.import_image.to_plane(files=[{"name": backgrTexName}], directory=backgrTexPath, filter_image=True,
                                  filter_movie=True)
    bpy.data.objects[0].name = 'BackgrImagePlane'
    backimage_obj = bpy.data.objects["BackgrImagePlane"]
    backimage_obj.location = (-2.0, 0.0, 0.0)
    backimage_obj.rotation_euler = (radians(0), radians(90), radians(0))
    bpy.context.object.active_material.use_shadeless = True
    #################################################################################
    # Now the camera
    cam = bpy.data.cameras.new("Camera")
    cam_ob = bpy.data.objects.new("Camera", cam)
    bpy.context.scene.camera = cam_ob
    bpy.context.scene.objects.link(cam_ob)
    bpy.context.scene.objects.active = bpy.context.scene.objects["Camera"]

    obj_camera = bpy.data.objects['Camera']  # bpy.types.Camera
    obj_camera.data.type = 'ORTHO'
    obj_camera.location.x = 10.0
    obj_camera.location.y = 0.0
    obj_camera.location.z = 0.0
    obj_camera.rotation_euler = (radians(0), radians(90), radians(0))  # !!!!!!!!!!!!!!!!

    #################################################################################
    # Create couple of new lamps.  (Using single lamp will create shadows
    # For additional info on lamps, see http://wiki.blender.org/index.php/Dev:2.5/Py/Scripts/Cookbook/Code_snippets/Other_data_types
    lamp1_data = bpy.data.lamps.new(name="Lamp1", type='POINT')
    lamp2_data = bpy.data.lamps.new(name="Lamp2", type='POINT')

    # Create new lamp objects with our lamp datablock
    lamp_obj1 = bpy.data.objects.new(name="Lamp1", object_data=lamp1_data)
    lamp_obj2 = bpy.data.objects.new(name="Lamp2", object_data=lamp2_data)

    # Link lamp objects to the scene so it'll appear in this scene
    scene.objects.link(lamp_obj1)
    scene.objects.link(lamp_obj2)

    # Place lamps in specified locations
    lamp_obj1.location = (6.0, 3.0, 0.0)
    lamp_obj2.location = (6.0, -3.0, 0.0)
    lamp_obj1.data.energy = 3
    lamp_obj2.data.energy = 3

    #################################################################################
    # Render the scene
    bpy.ops.object.select_all(action='DESELECT')
    face_obj.select = True
    bpy.context.scene.objects.active = face_obj
    bpy.context.object.rotation_mode = 'YZX'
    pi = 3.14159265
    face_obj.rotation_euler[0] = rx * (pi / 180.0)
    face_obj.rotation_euler[1] = ry * (pi / 180.0)
    face_obj.rotation_euler[2] = rz * (pi / 180.0)

    f.write("rx" + str(rx) + " ")
    f.write("ry" + str(ry) + " \n")

    # Set the render params
    pi = 3.14159265
    scene = bpy.data.scenes["Scene"]
    # Set render resolution
    scene.render.resolution_x = renderRes_x
    scene.render.resolution_y = renderRes_y
    scene.render.resolution_percentage = 100

    fov = 90.0
    scene.camera.data.angle = fov * (pi / 180.0)
    scene.camera.data.ortho_scale = 1.333

    bpy.ops.object.select_all(action='DESELECT')
    face_obj.select = True
    bpy.context.scene.objects.active = face_obj

    # Add a new texture to material
    for i in range(0, 10, 1):
        bpy.ops.object.material_slot_remove()

    mat = bpy.data.materials.new(name="Material")
    bpy.ops.object.material_slot_add()
    bpy.context.object.data.materials[0] = mat
    bpy.context.object.active_material.specular_intensity = 0
    Tex = bpy.data.textures.new("ObjectTexture", type='IMAGE')
    Img = bpy.data.images.load(foregroundTextures + "\\" + objTexName)
    Tex.image = Img
    bpy.context.object.active_material.specular_intensity = 0
    # uncomment next line for activate shadeless option to object material
    bpy.context.object.active_material.use_shadeless = True
    mtex = bpy.context.object.active_material.texture_slots.add()
    mtex.texture = Tex
    mtex.texture_coords = 'WINDOW'
    mtex.use_map_color_diffuse = True
    mtex.diffuse_color_factor = 1.0
    mtex.blend_type = 'MULTIPLY'
    mtex.offset = (random.randint(0, 10001), random.randint(0, 10000),
                   0)  # THIS IS YOUR texture's OFFSET Martin added this back for texture offset
    #############################################

    # filepath = "somepathtoimage"
    filepath = backgrTexPath + "\\" + backgrTexName
    for a in bpy.context.screen.areas:
        if a.type == 'VIEW_3D':
            break

    if (outfiletype == ".bmp"):
        scene.render.image_settings.file_format = 'BMP'
    elif (outfiletype == ".jpg"):
        # The following code snippet was copied from https://gooseberry.blender.org/simple-python-tips-for-artists/
        # Output to JPEG 100% (for easy test render saving):
        scene.render.image_settings.file_format = 'JPEG'
        scene.render.image_settings.quality = 100
    else:
        scene.render.image_settings.file_format = 'PNG'
        scene.render.image_settings.quality = 100

    face_obj.rotation_euler[1] = ry * (pi / 180.0)

    myFileName = "img" + str(imgNum)  # martin changed the name of files for training teams

    myLogEntry = (myFileName + ", " + backgrTexName + ", " + infile + ", " + objTexName + ", " + str(
        x) + ", " + str(y) + ", " + str(rx) + ", " + str(ry) + ", rz" + "\n")

    myFilePath = (original_img_path + myFileName)

    if not os.path.exists(myFilePath):  # Avoid overwriting
        print(myFilePath)
        if not os.path.exists(path + "/meta.txt"):
            f = open(path + "/meta.txt", "a")
            f.write(
                "FileName, background_texture_name, object_file_name, object_texture_name, X-coord, Y-coord, rotation about X (rx), ry, rz \n\n")  # write a header if meta.txt is new
        else:
            f = open(path + "/meta.txt", "a")
        f.write(myLogEntry)
        f.close()
        bpy.data.scenes['Scene'].render.filepath = myFilePath
        bpy.ops.render.render(write_still=True)
    else:
        print("Render already exists! Moving to next image...")
    filename = myFilePath + ".png"
    
    save = sizechecker(filename)
    
    # coded my Martin uses function to remove files that have no background
    if save is False:
        os.remove(filename)
        return save
        

    if os.path.exists(filename):
        if negative_enabled:
            bpy.ops.object.select_all(action='DESELECT')
            face_obj.select = True
            objs.remove(objs["FaceObject"], do_unlink=True)
            bpy.ops.object.select_all(action='DESELECT')

            myFileName = ("img" + str(imgNum) + "_negative")
            myFilePath = (negative_img_path + myFileName)
            if not os.path.exists(myFilePath):
                bpy.data.scenes['Scene'].render.filepath = myFilePath
                bpy.ops.render.render(write_still=True)
            else:
                print("Render already exists! Moving to next image...")

    bpy.ops.object.delete()

    f.close()
    return save 


def contour_images(x, y, rx, ry, rz, infile, fore_head_object_path, log_path, path, negative_enabled, renderRes_x,
                   renderRes_y, scaleFactor, start=0):
    original_contour_path = path + "/outputFilescontour/"
    negative_contour_path = path + "/outputFilescneg/"

    objs = bpy.data.objects

    contDir = path + "/contour_background"
    blackbg = contDir + "/black.jpg"
    whitebg = contDir + "/white.jpg"

    bpy.context.scene.world.ambient_color = (0, 0, 0)
    bpy.context.scene.world.horizon_color[0] = 0
    bpy.context.scene.world.horizon_color[1] = 0
    bpy.context.scene.world.horizon_color[2] = 0
    bpy.context.scene.world.zenith_color[0] = 0
    bpy.context.scene.world.zenith_color[1] = 0
    bpy.context.scene.world.zenith_color[2] = 0
    ################################################################################
    backgrTexName = blackbg  # Randomly select a background texture
    imgNum = start  # + len(listFiles(dir=original_contour_path, ext='.jpg'))
    #################################################################################################################
    # Select a random foreground(object) texture
    objTexName = whitebg
    outfiletype = '.png'
#    print(infile)
    ##################################################################################
    # Remove all existing objects in the scene
    scene = bpy.context.scene

    for ob in scene.objects:
        ob.select = True
    bpy.ops.object.delete()

    ##################################################################################
    # Import face .obj file
    full_path_to_file = (fore_head_object_path + infile)

    bpy.ops.import_scene.obj(filepath=full_path_to_file, \
                             filter_glob="*.obj",
                             use_edges=True, \
                             use_smooth_groups=True, \
                             use_split_objects=False, \
                             use_split_groups=False,
                             use_groups_as_vgroups=False, \
                             use_image_search=False, \
                             split_mode='ON', \
                             global_clamp_size=0.0, \
                             axis_forward='-Z', \
                             axis_up='Y')

    #################################################################################
    bpy.data.objects[0].name = 'FaceObject'
    # print(bpy.data.objects[0].name)

    #################################################################################
    face_obj = bpy.data.objects["FaceObject"]

    face_obj.location = (0.0, y / renderRes_y, -x / renderRes_y)

    # scale x, y, z
    face_obj.scale = (scaleFactor, scaleFactor, scaleFactor)

    ##################################################################################

    '''
    bpy.ops.import_image.to_plane(shader='SHADELESS', files=[{'name':blackbg}])
    bpy.data.objects[1].name = 'BackgrImagePlane'
    backimage_obj = bpy.data.objects["BackgrImagePlane"]
    backimage_obj.location = (-2.0, 0.0, 0.0)
    backimage_obj.rotation_euler = (radians(0), radians(90), radians(0))
    bpy.context.object.active_material.use_shadeless = True'''
    #################################################################################
    # Now the camera
    cam = bpy.data.cameras.new("Camera")
    cam_ob = bpy.data.objects.new("Camera", cam)
    bpy.context.scene.camera = cam_ob
    bpy.context.scene.objects.link(cam_ob)
    bpy.context.scene.objects.active = bpy.context.scene.objects["Camera"]

    obj_camera = bpy.data.objects['Camera']  # bpy.types.Camera
    obj_camera.data.type = 'ORTHO'
    obj_camera.location.x = 4.0
    obj_camera.location.y = 0.0
    obj_camera.location.z = 0.0
    obj_camera.rotation_euler = (radians(0), radians(90), radians(0))  # !!!!!!!!!!!!!!!!

    #################################################################################
    # Create couple of new lamps.  (Using single lamp will create shadows
    # For additional info on lamps, see http://wiki.blender.org/index.php/Dev:2.5/Py/Scripts/Cookbook/Code_snippets/Other_data_types
    lamp1_data = bpy.data.lamps.new(name="Lamp1", type='POINT')
    lamp2_data = bpy.data.lamps.new(name="Lamp2", type='POINT')

    # Create new lamp objects with our lamp datablock
    lamp_obj1 = bpy.data.objects.new(name="Lamp1", object_data=lamp1_data)
    lamp_obj2 = bpy.data.objects.new(name="Lamp2", object_data=lamp2_data)

    # Link lamp objects to the scene so it'll appear in this scene
    scene.objects.link(lamp_obj1)
    scene.objects.link(lamp_obj2)

    # Place lamps in specified locations
    lamp_obj1.location = (6.0, 3.0, 0.0)
    lamp_obj2.location = (6.0, -3.0, 0.0)
    lamp_obj1.data.energy = 3
    lamp_obj2.data.energy = 3

    #################################################################################
    # Render the scene
    bpy.ops.object.select_all(action='DESELECT')
    face_obj.select = True
    bpy.context.scene.objects.active = face_obj
    bpy.context.object.rotation_mode = 'YZX'
    pi = 3.14159265
    face_obj.rotation_euler[0] = rx * (pi / 180.0)
    face_obj.rotation_euler[1] = ry * (pi / 180.0)
    face_obj.rotation_euler[2] = rz * (pi / 180.0)

    # Set the render params
    pi = 3.14159265
    scene = bpy.data.scenes["Scene"]
    # Set render resolution
    scene.render.resolution_x = renderRes_x
    scene.render.resolution_y = renderRes_y
    scene.render.resolution_percentage = 100

    fov = 90.0
    scene.camera.data.angle = fov * (pi / 180.0)
    scene.camera.data.ortho_scale = 1.333

    bpy.ops.object.select_all(action='DESELECT')
    face_obj.select = True
    bpy.context.scene.objects.active = face_obj

    # Add a new texture to material
    for i in range(0, 10, 1):
        bpy.ops.object.material_slot_remove()
    mat = bpy.data.materials.new(name="Material")
    bpy.ops.object.material_slot_add()
    bpy.context.object.data.materials[0] = mat
    bpy.context.object.active_material.specular_intensity = 0
    Tex = bpy.data.textures.new("ObjectTexture", type='IMAGE')
    Img = bpy.data.images.load(whitebg)  # Martin - here is where the head is turned white instead of camo
    Tex.image = Img
    bpy.context.object.active_material.specular_intensity = 0
    # uncomment next line for activate shadeless option to object material
    bpy.context.object.active_material.use_shadeless = True
    mtex = bpy.context.object.active_material.texture_slots.add()
    mtex.texture = Tex
    mtex.texture_coords = 'WINDOW'
    mtex.use_map_color_diffuse = True
    mtex.diffuse_color_factor = 1.0
    mtex.blend_type = 'MULTIPLY'
    #############################################
    for a in bpy.context.screen.areas:
        if a.type == 'VIEW_3D':
            break

    if (outfiletype == ".bmp"):
        scene.render.image_settings.file_format = 'BMP'
    elif (outfiletype == ".jpg"):

        scene.render.image_settings.file_format = 'JPEG'
        scene.render.image_settings.quality = 100
    else:
        scene.render.image_settings.file_format = 'PNG'
        scene.render.image_settings.quality = 100

    face_obj.rotation_euler[1] = ry * (pi / 180.0)

    myFileName = ("img" + str(imgNum))
    myFilePath = (original_contour_path + myFileName)

    if not os.path.exists(myFilePath):  # Avoid overwriting
        bpy.data.scenes['Scene'].render.filepath = myFilePath
        bpy.ops.render.render(write_still=True)
        
        """
        #Edge not fully implement
        
        isEdge = False
        #get file path
        file_path = myFilePath + outfiletype
        #read the file
        file = cv2.imread(file_path)
        #generate the edge
        if(isEdge == True):
            edge_generator(file, imgNum, outfiletype)
        """
    else:
        print("Render already exists! Moving to next image...")

    bpy.ops.object.select_all(action='DESELECT')
    face_obj.select = True
    objs.remove(objs["FaceObject"], do_unlink=True)
    bpy.ops.object.select_all(action='DESELECT')

    if negative_enabled:
        myFileName = ("img" + str(imgNum) + "_negative")
        myFilePath = (negative_contour_path + myFileName)
        if not os.path.exists(myFilePath):
            bpy.data.scenes['Scene'].render.filepath = myFilePath
            bpy.ops.render.render(write_still=True)
        else:
            print("Render already exists! Moving to next image...")
            
    """
    #Generate edge condition
    #Basically if edge is enable and contour is disable, remove contour
    generate_contour = True 
   
    if generate_contour != True:
        contour_path = "./outputFilesCONTOUR"
        neg_contour_path = "./outputfilescneg"

        if os.path.exists(contour_path):
            for f in os.listdir(contour_path):
                os.remove(os.path.join(contour_path, f))

        if os.path.exists(neg_contour_path):
            for f in os.listdir(neg_contour_path):
                os.remove(os.path.join(neg_contour_path, f))
    """

    bpy.ops.object.delete()


def generate_image(max, negative_enabled, start=0, resolution_x=800, resolution_y=600):
    ##################################################################################
    # Specify paths and files
    print("Enter Generate Image")
    path = os.getcwd()
    outputpath = path + "/outputFiles/"
    fore_head_object_path = path + "/foregroundObjects/"
    min = 0
    log_path = path + "/imglog/"

    renderRes_x = resolution_x  # Martin fixed X and Y resolution
    renderRes_y = resolution_y

    while min < max:
        for infile in listFiles(dir=fore_head_object_path, ext='.obj'):
#            print("InFile: ")
#            print(infile)
            if min < max:
                vals = getvars(renderRes_x, renderRes_y)

                x = vals[0]
                y = vals[1]
                rx = vals[2]
                ry = vals[3]
                rz = vals[4]
                scaleFactor = vals[5]

                valid_img_print = camo_images(x, y, rx, ry, rz, infile, fore_head_object_path, log_path, path, negative_enabled,
                            renderRes_x, renderRes_y, scaleFactor, start)
                # Option
                # Martin - only generates images if it exists and not filtered
                if valid_img_print:
                    contour_images(x, y, rx, ry, rz, infile, fore_head_object_path, log_path, path, negative_enabled,
                                       renderRes_x, renderRes_y, scaleFactor, start)
                    min += 1
                    start += 1
                
         

"""
def edge_generator(mask, n,output_type):

    edge = cv2.Canny(mask, 100, 200)
    cv2.imwrite(os.path.join("./edge","edge" + str(n) + output_type), edge)
"""

max_size = 0



# coded my Martin to filter files that have no background
# Kaney added algorithm to filter out background based on resolution
def sizechecker(file):
    
    global max_size
    convert_string = ""
    flag = True
    filesize = os.path.getsize(file)
    
    
    if max_size < filesize:
        max_size = filesize
#    print("File Size: " + str(filesize))
#    print("Max Size: " + str(max_size))
    convert_string = str(max_size)
#    print("length: " + str(len(convert_string)))
    #If filesize is less than the recommended size
    #don't print

    if int(filesize) <= int(max_size)/int(len(convert_string)):
        flag = False
    return flag

numbersOnlyRegex = re.compile(r'^[0-9]+$')
yesornoRegex = re.compile(r'^[yYnN]{1}$')



userInput = input("Enter Resolution X: ")
while True:
    if bool(re.search(numbersOnlyRegex,userInput) and int(userInput) > 0):
        resolution_x = userInput
        break
    else:
        userInput = input('please enter a number: ')
    
userInput = input("Enter Resolution Y: ")
while True:
    if bool(re.search(numbersOnlyRegex,userInput) and int(userInput) > 0):
        resolution_y = userInput
        break
    else:
        userInput = input('please enter a number: ')

userInput = input("Negative Enable ? Y/N: ")
while True:
    if bool(re.search(yesornoRegex,userInput)):
        negative_input = userInput
        break
    else:
        userInput = input('please enter y or n: ')

if negative_input == 'Y' or negative_input == 'y':
    negative_enabled = True
else:
    negative_enabled = False

userInput = input("Enter amount of images to generate: ")
while True:
    if bool(re.search(numbersOnlyRegex,userInput) and int(userInput) > 0):
        max = userInput
        break
    else:
        userInput = input('please enter a number: ')

userInput = input('which index to start from (images will be overwritten if starting at an already existing index) : ')
while True:
    if bool(re.search(numbersOnlyRegex,userInput)):
        start = userInput
        break
    else:
        userInput = input('please enter a number: ')
        
generate_image(int(max), negative_enabled, int(start), int(resolution_x), int(resolution_y))
