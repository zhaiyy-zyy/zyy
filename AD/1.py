import os
from moviepy import VideoFileClip

def get_mp4_durations(folder_path):
    """
    获取指定文件夹内所有 mp4 视频的时长，并返回按照文件名字典序排序后的列表。
    :param folder_path: 存放 mp4 文件的文件夹路径
    :return: [(video_name, duration), ...] 按字典序排序
    """
    results = []
    
    # 列举文件夹内所有文件
    for filename in os.listdir(folder_path):
        # 只处理 mp4 文件
        if filename.lower().endswith(".mp4"):
            full_path = os.path.join(folder_path, filename)
            
            # 使用 moviepy 读取视频并获取时长
            with VideoFileClip(full_path) as video:
                duration = video.duration  # 单位为秒
                results.append((filename, duration))
    
    # 按照文件名字典序排序
    results.sort(key=lambda x: x[0])
    
    return results

# 使用示例
if __name__ == "__main__":
    folder = "videos"
    durations = get_mp4_durations(folder)
    for video_name, duration in durations:
        print(f"视频: {video_name}, 时长: {duration:.2f} 秒")  # 保留两位小数