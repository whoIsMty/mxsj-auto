from pypinyin import pinyin, lazy_pinyin, Style


class PinYinUtils:


    @staticmethod
    def chinese_to_pinyin(text, with_tone=False, tone_marks=False):
        """
        将中文字符串转换为拼音。

        :param text: 中文字符串
        :param with_tone: 是否包含声调（默认不包含）
        :param tone_marks: 是否使用声调符号（默认使用数字）
        :return: 拼音字符串
        """
        if with_tone:
            if tone_marks:
                # 返回包含声调符号的拼音
                pinyin_result = pinyin(text, style=Style.TONE3)
            else:
                # 返回包含声调的拼音，声调用数字表示
                pinyin_result = pinyin(text, style=Style.TONE)
        else:
            # 返回不包含声调的拼音
            pinyin_result = lazy_pinyin(text)

        # 将拼音结果列表转为字符串
        return ''.join([''.join(syllable) for syllable in pinyin_result])

if __name__ == '__main__':
        print(PinYinUtils.chinese_to_pinyin("你好"))
