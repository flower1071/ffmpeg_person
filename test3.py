import os, time

"""通过对象处理文件"""
"""need 输出不需要执行的文件"""


class EditVideo:
    def __init__(self, ffprobe_p, ffmpeg_p, speed, s_p, o_p):
        """ffprobe_p为ffprobe二进制文件的路径，ffmpeg_p为ffmpeg文件路径,speed为speed参数,s_p为源文件路径，o_p为输出目录路径"""
        self.i_l = None
        self.ffprobe = ffprobe_p
        self.ffmpeg = ffmpeg_p
        self.speed = speed
        self.s_p = s_p
        self.o_p = o_p

    def get_video_info(self):
        """b_p为ffprobe文件的路径，f_p为视频文件的路径，结果会return一个包含三个元素的元组，例如
    ('vp9', 1920, 24 , 600)
    分别是
    文件的视频编码类型，str
    文件的横向分辨率，int
    文件的平均帧率，int
    文件的视频码率，单位k. int
        """
        try:
            g_i = os.popen(f'{self.ffprobe} "{self.s_p}" -show_streams -print_format json')
            info_list = eval(g_i.read())['streams']
            g_i.close()
            for i in info_list:
                if 'video' in str(i):
                    # bit_rate =
                    self.i_l = (i['codec_name'], i['coded_width'], int(eval(i['avg_frame_rate'])), int(int(i['bit_rate']) / 1000))
                    return self.i_l
        except:
            print(f"文件{self.s_p}打开错误###################################################################")
            exit()

    def pt(self):
        """测试get_video_info()函数"""
        s_i = self.get_video_info()
        print(s_i)

    def judge_video_mat(self):
        """匹配帧率，分辨率，码率来return 需要输出的 编码，帧率，码率信息"""
        s_i = self.get_video_info()  # 源文件的元组信息，内容包括 编码类型 横向分辨率 平均帧率float
        if s_i[0] == 'vp9':
            if s_i[2] > 35:
                m_b = s_i[1] / 0.96  # 输出码率
                return 'vp9', '30', m_b
            else:
                w_b = s_i[1] / 0.96 + s_i[1] / 12
                if s_i[3] <= w_b:
                    return ('w')
                else:
                    return 'vp9', '30', s_i[1] / 0.96
        else:
            return 'vp9', '30', s_i[1] / 0.96

    def transition(self):
        info = self.judge_video_mat()  # 编码，帧率，码率信息
        f_n = ''.join(self.s_p.split('\\')[-1].split('.')[0:-1])  # 文件名
        f_m = self.s_p.split('\\')[-1].split('.')[-1]  # 文件扩展名
        o_p = self.o_p + '\\' + f_n + "[NEW]." + f_m
        t1 = time.time()
        os.system(
            f'{self.ffmpeg} -i "{self.s_p}" -vcodec libvpx-vp9 -c:a copy -b:v {info[2]}k -speed {self.speed} -r {info[1]} -pass 1 -an -sn "{o_p}"')
        os.system(
            f'{self.ffmpeg} -i "{self.s_p}" -vcodec libvpx-vp9 -c:a copy -b:v {info[2]}k -speed {self.speed} -r {info[1]} -pass 2 -y "{o_p}"')
        t2 = time.time()
        print(f"用时{t2 - t1}")

    def mian_(self):
        """主流程"""
        try:
            result = self.judge_video_mat()
            if result[0] == 'w':
                print(f'文件“{self.s_p}”不需要转码')
            else:
                self.transition()
        except:
            pass



aa = EditVideo(r'D:\pychram_project\youtube_download\ffmpeg_project\bin\ffmpeg\bin\ffprobe.exe', r'D:\pychram_project\youtube_download\ffmpeg_project\bin\ffmpeg\bin\ffmpeg.exe', 0, r'D:\addons\test\1s.mp4', r'D:\addons\test\old')
aa.mian_()
