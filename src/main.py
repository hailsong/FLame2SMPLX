'''
Date: 2022-02-25 16:48:06
LastEditors: cvhadessun
LastEditTime: 2022-03-10 14:45:51
FilePath: /FLame2SMPLX/src/main.py
'''
import cv2
from utils.texture_match import flame_smplx_texture_combine



def transform(filename):
    smplx_obj = "../data/smplx-addon.obj"
    flame_obj = "../data/head_template.obj"
    smplx_2_flame = "../data/SMPL-X__FLAME_vertex_ids.npy"
    smplx_texture = f"../data/input/smplx_{filename}"
    flame_texture = f"../data/input/{filename}"

    # only face (not head)
    face_vertex_ids = "../data/face_vertex_ids.npy"


    tex_output = flame_smplx_texture_combine(flame_obj,smplx_obj,flame_texture,smplx_texture,smplx_2_flame,None)

    output_filename = 'converted_' + filename
    cv2.imwrite(f'../data/output/{output_filename}',tex_output)

transform('han_1.png')
transform('han_2.png')
transform('han_3.png')