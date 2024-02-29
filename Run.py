from APMA import APMA
import os
import glob
import traceback

# fetch email
email_list = []
f = open("/home/wangjingran/APMA/data/email.txt")
lines = f.readlines()
for i in lines:
    line = i.strip("\n")
    email_list.append(line)
f.close()

# fetch pdb file
def print_pdb_files(folder_path):
    # 使用 glob 模块列出文件夹中所有的 .pdb 文件
    pdb_files = glob.glob(os.path.join(folder_path, '*.pdb'))
    for i in pdb_files:
        user_pdb_file = i
    return user_pdb_file

folder_path = '/home/wangjingran/APMA/data'
user_pdb = print_pdb_files(folder_path)
user_protein_name = user_pdb.split("/")[-1].rstrip(".pdb")

try:

    APMA(
    Protein_name = user_protein_name,
    file_path = "/home/wangjingran/APMA/data/position.txt",
    WT_PDB = user_pdb
    )

    from ML.figure import plot_roc_for_disease_pairs
    plot_roc_for_disease_pairs("/home/wangjingran/APMA/data/paras.txt","/home/wangjingran/APMA/Outcome/Figure/ROC/Feature")

    from ML.figure import plot_box
    plot_box("/home/wangjingran/APMA/data/paras.txt","/home/wangjingran/APMA/Outcome/Figure/Box_Violin")

    from ML.figure import plot_spearman
    plot_spearman("/home/wangjingran/APMA/data/paras.txt","/home/wangjingran/APMA/Outcome/Figure")

    from Email.zip import zip_folder
    zip_folder('/home/wangjingran/APMA/Outcome','/home/wangjingran/APMA/Email/APMA_outcome.zip')
    
    from Email.send import send_email
    send_email(email_list)

except Exception as e:
    print(str(e))
    traceback_info = traceback.format_exc()
    print(traceback_info)
    from Email.send import send_error_email
    send_error_email(email_list)


import os

def delete_files_in_directory(directory):
    # 遍历目录中的所有文件和子目录
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        # 如果是文件，则删除
        if os.path.isfile(item_path):
            os.remove(item_path)
        
        # 如果是目录，则递归调用该函数
        elif os.path.isdir(item_path):
            delete_files_in_directory(item_path)

delete_files_in_directory("/home/wangjingran/APMA/Outcome")
delete_files_in_directory("/home/wangjingran/APMA/data")

folder_path = '/home/wangjingran/APMA/FoldX'
files = os.listdir(folder_path)

for file_name in files:
    
    if file_name != 'foldx4' and file_name != 'rotabase.txt':
        file_path = os.path.join(folder_path, file_name)

        os.remove(file_path)

