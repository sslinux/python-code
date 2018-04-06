info = {"name":"bangzhang"}

info["age"] = 18
info["QQ"] = 10086    # 若key不存在，则为添加；

info["QQ"] = 10010    # 若key已存在，则为修改；

del info['QQ']      # 删除key为QQ的元素；

# 查询：
info.get("QQ")      # 若有这个键，则返回;若无这个键也不会报错；





