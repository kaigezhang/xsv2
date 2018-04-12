from scholar.settings.base import *

DEBUG = False

DATABASES = {
    'default': env.db()
}

# 节省流量，使用内网
# 但不是下面的这个方法，下面的方法会造成数据无法上传
# ALIYUN_OSS_END_POINT = env.str('ALIYUN_OSS_ENV_INTERNAL_POINT', 'oss-cn-beijing.aliyuncs.com')