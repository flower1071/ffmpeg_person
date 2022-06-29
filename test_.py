import os,time
"""
函数teansition()新增speed参数
"""


def transition(v_p, o_p, bit_rate, ffmpeg_path, speed):
    """v_p:源文件位置;o_p:输出目录;bitspeed:码率"""
    f_n = ''.join(v_p.split('\\')[-1].split('.')[0:-1])  # 文件名
    f_m = v_p.split('\\')[-1].split('.')[-1]  # 文件扩展名
    o_p = o_p + '\\' + f_n + "[NEW]." + f_m
    t1 = time.time()
    os.system(f'{ffmpeg_path} -i "{v_p}" -vcodec libvpx-vp9 -c:a copy -b:v {bit_rate} -speed {speed} -pass 1 -an -sn "{o_p}"')
    os.system(f'{ffmpeg_path} -i "{v_p}" -vcodec libvpx-vp9 -c:a copy -b:v {bit_rate} -speed {speed}  -pass 2 -y "{o_p}"')
    t2 = time.time()
    print(f"用时{t2 - t1}")

def get_definition(f_t):
    pass




def main_method():
    """仅支持处理当前目录下的视频，二级目录无法处理，且1级目录下的MP4后缀文件会被全部处理"""
    ffmpeg_path = f"D:\pychram_project\youtube_download\\ffmpeg\\bin\\ffmpeg"
    s_p = input("请输入文件所在的目录：") + '\\'
    out_p = input("请指定输出目录：")
    f_l = []
    a_f = os.listdir(s_p)
    for i in a_f:
        if i.split('.')[-1] == 'mp4' or i.split('.')[-1] == 'MP4' or i.split('.')[-1] == 'Mp4':
            f_l.append(s_p + i)
    if f_l == 0:
        pass
    else:
        for i in f_l:
            transition(i, out_p, '1500k', ffmpeg_path, 5)
    end_ = input("end!")

if __name__ == "__main__":
    main_method()
else:
    pass
