import soundfile as sf
from pydub import AudioSegment
import numpy as np
import datetime

# 加载音频文件
audio = AudioSegment.from_wav("audio_file.wav")

# 设置阈值（以分贝为单位）
threshold = 10

# 将PyDub音频片段转换为NumPy数组
audio_array = audio.get_array_of_samples()
sample_rate = audio.frame_rate

# 计算每秒钟的音频片段
segment_length_ms = 1000  # 设置片段长度（以毫秒为单位）
segment_count = int(len(audio) / segment_length_ms)
segments = [audio[i * segment_length_ms:(i + 1) * segment_length_ms] for i in range(segment_count)]

# 计算每个片段的分贝值
for i, segment in enumerate(segments):
    # 将PyDub音频片段转换为NumPy数组
    segment_array = segment.get_array_of_samples()

    # 计算该片段数组的均方根值（root mean square (RMS)）
    rms = np.sqrt(np.mean(np.square(segment_array)))

    # 从RMS计算分贝值
    db = 20 * np.log10(rms)

    # 如果分贝值超过阈值，则输出时间戳
    if db > threshold:
        start_time = i * (segment_length_ms / 1000)
        print(f"时间戳: {str(datetime.timedelta(seconds=start_time))}")
