

translate_dict = { "а":"a", "б":"b", "в":"v", "г":"g", "д":"d", "е": "ye", "ё":"yo", "ж": "j", "з":"z", "и":"i", "й":"y", "к":"k", "л":"l", "м":"m", "н":"n", "о":"o", "п":"p", "р":"r", "с":"s", "т":"t", "у":"u", "ф":"f", "х":"h", "ц":"ts", "ч":"tch", "ш":"sh", "щ":"shch", "ъ":"'", "ы":"y", "ь":"'", "э":"e", "ю":"yu", "я":"ya", " ":"_", "А":"A", "Б":"B", "В":"V", "Г":"G", "Д":"D", "Е": "Ye", "Ё":"Yo", "Ж": "J", "З":"Z", "И":"I", "Й":"Y", "К":"K", "Л":"L", "М":"M", "Н":"N", "О":"O", "П":"P", "Р":"R", "С":"S", "Т":"T", "У":"U", "Ф":"F", "Х":"H", "Ц":"Ts", "Ч":"Tch", "Ш":"Sh", "Щ":"Shch", "Ъ":"'", "Ы":"y", "Ь":"'", "Э":"E", "Ю":"Yu", "Я":"Ya" }


#Текст с сохранением заглавных букв
def translit(text):
	out = ""
	for char in text:
		if char in translate_dict:
			out += translate_dict[char]
		else:
			out += char
	return out


#Текст в нижнем регистре
def translit_low(text):
	out = ""
	for char in text:
		if char in translate_dict:
			out += translate_dict[char.lower()]
		else:
			out += char
	return out.lower()


#Текст в верхнем регистре
def translit_up(text):
	out = ""
	for char in text:
		if char in translate_dict:
			out += translate_dict[char.lower()]
		else:
			out += char
	return out.upper()