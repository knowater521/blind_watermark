from blind_watermark import att

# 亮度调高攻击
att.bright_att('output/打上水印的图.png', 'output/亮度调高攻击.png', ratio=1.1)

#%% 提取水印
from blind_watermark import WaterMark

bwm1 = WaterMark(4399, 2333, 36, 20, wm_shape=(128, 128))
bwm1.extract('output/亮度调高攻击.png', 'output/亮度调高攻击_提取水印.png')
