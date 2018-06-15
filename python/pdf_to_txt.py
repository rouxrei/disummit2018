import os
import subprocess

cwd = os.getcwd()
in_p = os.path.join(cwd, 'data', 'medicine')
out_p = os.path.join(cwd, 'output', 'medicine_txt')
img_out = os.path.join(cwd, 'output', 'medicine_img')
convert_p = os.path.join(cwd, 'output', 'converted_img')

# http://www.xpdfreader.com/

def pdf_to_text(src_path='.', tgt_path='.', img_path='.', types=['raw', 'layout', 'simple', 'table'], delEmpty=False, verbose=True):
    # get all pdf files from 'scr_path':
    files = os.listdir(src_path)
    files = [f for f in files if f[-4:] == '.pdf']

    # process each file:
    for file in files:
        if verbose: print('Processing: ', file)
        in_f = os.path.join(src_path, file)
        
        out_img = os.path.join(img_path, file[:-4])
        # put all images in a subdir per input file:
#        os.makedirs(out_img, exist_ok=True)
        #pathlib.Path(out_img).mkdir(parents=True, exist_ok=True)
#        pdf_img_command = ["pdfimages", "-j", in_f, os.path.join(out_img, "img")]
#        subprocess.call(pdf_img_command)
#        # make txt file per type
        for typ in types:
            out_f = os.path.join(tgt_path, typ + "_" + file[:-4] + ".txt")
            pdf_txt_command = ["pdftotext", "-"+typ, in_f, out_f]
           # print(pdf_txt_command)
            subprocess.check_output(pdf_txt_command)
        # remove empty subdirs:
        if delEmpty:
            images = os.listdir(out_img)
            if len(images) == 0: os.rmdir(out_img)
            

#for curr, _, img_lst in os.walk(img_out):
#    for img in img_lst:
#        jpg_out = os.path.join(convert_p, img[:-4] + '.jpg')
#        convert_command = ["convert.exe", os.path.join(curr, img), jpg_out]
#        subprocess.check_output(convert_command, shell=True)
#
