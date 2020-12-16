# coding=utf-8

import normalization
import unicodedata

'''
text = "tai mažas testas, taip vaikinaiūy ĖŠ aąbcčdeęėfghiįyjklmnoprsštuųūvzž"
text = "Мен мұны қатты жақсы көремін. Бұл өте қызықты және жігерлендіргіш."
'''

text = "Мен мұны 222 қатты жақсы көремін. Бұл өте қызықты жәнеó жiгерлендіргішш' '' ' .  ثّأبنى 私の息子 Мен abcdf a'b ....@! ^ & * 21312312 ї nnANn"

print('\nPunctuation')
print(text)
normalized_text = normalization.process("KK", text, letters_to_keep='', letters_to_remove='', lowercase=False, remove_repetitions_count=-1, remove_punct=True, remove_digits=False, remove_vowels=False, remove_diacritics=False, remove_spaces=False, remove_apostrophe=False, copy_through= True, keep_romanized_text=True)
print(normalized_text)

print('\nDigits')
print(text)
normalized_text = normalization.process("KK", text, letters_to_keep='', letters_to_remove='', lowercase=False, remove_repetitions_count=-1, remove_punct=False, remove_digits=True, remove_vowels=False, remove_diacritics=False, remove_spaces=False, remove_apostrophe=False, copy_through= True, keep_romanized_text=True)
print(normalized_text)

print('\nVowels')
print(text)
normalized_text = normalization.process("KK", text, letters_to_keep='', letters_to_remove='', lowercase=False, remove_repetitions_count=-1, remove_punct=False, remove_digits=False, remove_vowels=True, remove_diacritics=False, remove_spaces=False, remove_apostrophe=False, copy_through= True, keep_romanized_text=True)
print(normalized_text)

print('\nVowels and Do not keep Romanized')
print(text)
normalized_text = normalization.process("KK", text, letters_to_keep='', letters_to_remove='', lowercase=False, remove_repetitions_count=-1, remove_punct=False, remove_digits=False, remove_vowels=True, remove_diacritics=False, remove_spaces=False, remove_apostrophe=False, copy_through= True, keep_romanized_text=False)
print(normalized_text)

print('\nDiacs')
print(text)
normalized_text = normalization.process("KK", text, letters_to_keep='', letters_to_remove='', lowercase=False, remove_repetitions_count=-1, remove_punct=False, remove_digits=False, remove_vowels=False, remove_diacritics=True, remove_spaces=False, remove_apostrophe=False, copy_through= True, keep_romanized_text=True)
print(normalized_text)

print('\nDiacs and Do not keep Romanized')
print(text)
normalized_text = normalization.process("KK", text, letters_to_keep='', letters_to_remove='', lowercase=False, remove_repetitions_count=-1, remove_punct=False, remove_digits=False, remove_vowels=False, remove_diacritics=True, remove_spaces=False, remove_apostrophe=False, copy_through= True, keep_romanized_text=False)
print(normalized_text)

print('\nApostrphes')
print(text)
normalized_text = normalization.process("KK", text, letters_to_keep='', letters_to_remove='', lowercase=False, remove_repetitions_count=-1, remove_punct=False, remove_digits=False, remove_vowels=False, remove_diacritics=False, remove_spaces=False, remove_apostrophe=True, copy_through= True, keep_romanized_text=True)
print(normalized_text)

print('\nDo not CopyThrough')
print(text)
normalized_text = normalization.process("KK", text, letters_to_keep='', letters_to_remove='', lowercase=False, remove_repetitions_count=-1, remove_punct=False, remove_digits=False, remove_vowels=False, remove_diacritics=False, remove_spaces=False, remove_apostrophe=False, copy_through= False, keep_romanized_text=True)
print(normalized_text)

print('\nDo not keep Romanized')
print(text)
normalized_text = normalization.process("KK", text, letters_to_keep='', letters_to_remove='', lowercase=False, remove_repetitions_count=-1, remove_punct=False, remove_digits=False, remove_vowels=False, remove_diacritics=False, remove_spaces=False, remove_apostrophe=False, copy_through= True, keep_romanized_text=False)
print(normalized_text)