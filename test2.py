import os, time
'''获取视频文件的编码，帧率，分辨率信息'''

def get_vedio_info(b_p,f_p):
    """b_p为ffprobe文件的路径，f_p为视频文件的路径，结果会return一个包含三个元素的元组，例如
    ('vp9', 1920, 24.0)
    分别是
        文件的视频编码类型，str
        文件的横向分辨率，int
        文件的平均帧率，float
    """
    try:
        g_i = os.popen(f'{b_p} "{f_p}" -show_streams -print_format json')
        info_list = eval(g_i.read())['streams']
        g_i.close()
        info_list = info_list
        for i in info_list:
            if 'video' in str(i):
                i_l = (i['codec_name'], i['coded_width'], eval(i['avg_frame_rate']))
                return i_l
    except:
        print(f"文件{f_p}打开错误###################################################################")
