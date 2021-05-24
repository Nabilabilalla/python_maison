chars = "¾ĩpÓ9-©Ñ±áįûyoÚ«ç?ÆbĺĄeĆ´EhVĠÁ)ĀĿ¦]ġùĦ­U¥À¬j$²ğà£í\\ĻÙGa¿ëtTÅ2ċļ¢ÿÉđ'4ĭĐ×ÕÌævĘölÂÐfĒòěĎS:OÇ>Êðz®ê¼ĂÏăW" \
     "Ĝ%Òĵ€þîľÄ[ĲåĽČī¨µIsēX0čõĪ÷»ĳćāĸķ*Ĕéx¡ĶĤNĞ1qãBJı ïĚİ_ì·LDħ+5PmYĴkäwĬÍ6ėĝÎØKŀÞÈdĢĉą\"óĕĮ,HiñÝ8Û`gQür&/ËÜ<ĖFĥu" \
     "@ý!ªú|ø³Ċ¤C\nßc.(â½~}Ĺ3ď¶ę°èM^nĈĨ¯Ã¹ARôģ=¸ZÔ;§#º7{"


def cipher(message: str, key: str, decipher=False) -> str:
    output = ''
    seed = sum([chars.find(char) for char in key])
    for char in message:
        index = chars.find(char)
        output += chars[(index + seed) % len(chars)] if not decipher else chars[(index - seed) % len(chars)]
    return output


if __name__ == '__main__':
    key = "Je suis une clé"
    message = """def cipher(message: str, key: str, decipher=False) -> str:
    output = ''
    seed = sum([chars.find(char) for char in key])
    for char in message:
        index = chars.find(char)
        output += chars[(index + seed) % len(chars)] if not decipher else chars[(index - seed) % len(chars)]
    return output
    """
    print('----- Message chiffré')
    print(cipher(message, key))
