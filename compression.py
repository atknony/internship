import colorama
import math

from colorama import Fore

indent = '         '
text = "i am using python"
char_list = list(text)
reduced_text = "".join(dict.fromkeys(text))
bit_width = math.ceil(math.log2(len(reduced_text)))
original_bit_length = len(text) * 8

ascii_list = [ord(i) for i in char_list]
binary_list = [bin(code)[2:].zfill(8) for code in ascii_list]
new_code_table_dic = {ch: i for i, ch in enumerate(reduced_text)}
new_codes_of_original_text_list = [new_code_table_dic[ch] for ch in text]
binary_codes_of_original_text_list = [bin(code)[2:].zfill(bit_width) for code in new_codes_of_original_text_list]

ascii_str =  "|".join(f"{Fore.YELLOW}{i}{Fore.GREEN}" for i in ascii_list)
binary_str =  "|".join(f"{Fore.MAGENTA}{i}{Fore.GREEN}" for i in binary_list)
new_code_table_str = "|".join(f"{Fore.GREEN}{ch}:{Fore.CYAN}{code}{Fore.GREEN}" for  ch, code in new_code_table_dic.items())
new_codes_of_original_text_str = "|".join(f"{Fore.CYAN}{code}{Fore.GREEN}" for code in new_codes_of_original_text_list)
binary_codes_of_original_text_str = "|".join(f"{Fore.MAGENTA}{i}{Fore.GREEN}" for i in binary_codes_of_original_text_list)

compressed_content_str = (
    f"{Fore.RED}{bit_width}{Fore.GREEN}|{reduced_text}|{Fore.MAGENTA}" + "".join(f"{i}" for i in binary_codes_of_original_text_list)  
)



print(f"{indent}{Fore.LIGHTCYAN_EX + '>>> compression operation <<<'}" )
print(f"{indent}{Fore.GREEN + '-----------------------------'}")
print()
print(f"{indent}{'original text':<50}: {text}")
print(f"{indent}{'ascii codes of original text':<50}: {ascii_str}")
print(f"{indent}{'binary codes of original text':<50}: {binary_str}")
print(f"{indent}{'reduced text':<50}: {reduced_text}")
print(f"{indent}{'new code table by reduced text':<50}: {new_code_table_str}")
print(f"{indent}{'new codes of original text':<50}: {new_codes_of_original_text_str}")
print(f"{indent}{'binary codes of original text':<50}: {binary_codes_of_original_text_str}")
print(f"{indent}{'compressed content':<50}: {compressed_content_str}")
print(f"{indent}{Fore.GREEN}{'compression ratio':<50}:")
print()
print(f"{indent}{Fore.RED + '<<< decompression operation >>>'}" )
print(f"{indent}{Fore.GREEN + '-------------------------------'}")
print()
print(f"{indent}{'compressed content':<50}: {compressed_content_str}")
print(f"{indent}{Fore.GREEN}{'guide from compressed content':<50}: {reduced_text}")
print(f"{indent}{'code table by guide':<50}: {new_codes_of_original_text_str}")
print(f"{indent}{'byte lenght from comp. content':<50}: {Fore.RED}{bit_width}")
print(f"{indent}{Fore.GREEN}{'binray codes from comp. content':<50}: {binary_codes_of_original_text_str}")
print(f"{indent}{'original text':<50}: {text}")
