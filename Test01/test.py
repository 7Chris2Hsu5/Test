def calculate_bmi(weight, height):
    """
    計算 BMI（身體質量指數）
    
    參數:
        weight: 體重（公斤）
        height: 身高（公尺）
    
    回傳:
        BMI 值
    """
    if height <= 0 or weight <= 0:
        return "錯誤：體重和身高必須大於 0"
    
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def get_bmi_category(bmi):
    """
    根據 BMI 值分類
    """
    if bmi < 18.5:
        return "體重不足"
    elif 18.5 <= bmi < 25:
        return "正常體重"
    elif 25 <= bmi < 30:
        return "過重"
    else:
        return "肥胖"


# 使用範例
if __name__ == "__main__":
    weight = 70  # 公斤
    height = 1.75  # 公尺
    
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    
    print(f'體重: {weight} kg')
    print(f'身高: {height} m')
    print(f'BMI: {bmi}')
    print(f'分類: {category}')
