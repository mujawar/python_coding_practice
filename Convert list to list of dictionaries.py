color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

resut = [{color:hash} for color,hash in zip(color_name,color_code)]
print(resut)