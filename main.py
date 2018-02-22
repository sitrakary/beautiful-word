char_a = [
    ' ***** ',
    '*     *',
    '*******',
    '*     *',
    '*     *',
]

char_b = [
    '****** ',
    '*     *',
    '****** ',
    '*     *',
    '****** ',
]

char_c = [
    '****** ',
    '*     *',
    '*      ',
    '*     *',
    '****** ',
]

char_d = [
    '****** ',
    '*     *',
    '*     *',
    '*     *',
    '****** ',
]

char_e = [
    ' ******',
    '*      ',
    '*******',
    '*      ',
    ' ******',
]

char_f = [
    ' ******',
    '*      ',
    '*******',
    '*      ',
    '*      ',
]

char_g = [
    ' ******',
    '*      ',
    '*  *** ',
    '*     *',
    ' ***** ',
]

char_h = [
    '*     *',
    '*     *',
    '*******',
    '*     *',
    '*     *',
]

char_i = [
    '*******',
    '   *   ',
    '   *   ',
    '   *   ',
    '*******',
]

char_j = [
    '*******',
    '     * ',
    '     * ',
    '*    * ',
    ' ****  ',
]

char_k = [
    '*     *',
    '*   *  ',
    '* *    ',
    '*   *  ',
    '*     *',
]

char_l = [
    '*      ',
    '*      ',
    '*      ',
    '*      ',
    '*******',
]

char_m = [
    '*     *',
    '* * * *',
    '*  *  *',
    '*     *',
    '*     *',
]

char_n = [
    '*     *',
    '* *   *',
    '*  *  *',
    '*   * *',
    '*     *',
]

char_o = [
    ' ***** ',
    '*     *',
    '*     *',
    '*     *',
    ' ***** ',
]

char_p = [
    '****** ',
    '*     *',
    '****** ',
    '*      ',
    '*      ',
]

char_q = [
    ' ***** ',
    '*     *',
    '*     *',
    '*   * *',
    ' **** *',
]

char_r = [
    '****** ',
    '*     *',
    '****** ',
    '*   *  ',
    '*     *',
]

char_s = [
    ' ***** ',
    '*      ',
    ' ***** ',
    '      *',
    ' ***** ',
]

char_t = [
    '*******',
    '   *   ',
    '   *   ',
    '   *   ',
    '   *   ',
]

char_u = [
    '*     *',
    '*     *',
    '*     *',
    '*     *',
    ' ***** ',
]

char_v = [
    '*     *',
    '*     *',
    '*     *',
    ' *   * ',
    '   *   ',
]

char_w = [
    '*     *',
    '*     *',
    '*  *  *',
    '* * * *',
    '*     *',
]

char_x = [
    '*     *',
    ' *   * ',
    '   *   ',
    ' *   * ',
    '*     *',
]

char_y = [
    '*     *',
    ' *   * ',
    '   *   ',
    '   *   ',
    '   *   ',
]

char_z = [
    '*******',
    '     * ',
    '   *   ',
    ' *     ',
    '*******'
]

char_space = [
    '   ''   ',
    '   ''   ',
    '   ''   ',
    '   ''   ',
    '   ''   ',
]

char_map = {
    'a': char_a,
    'b': char_b,
    'c': char_c,
    'd': char_d,
    'e': char_e,
    'f': char_f,
    'g': char_g,
    'h': char_h,
    'i': char_i,
    'j': char_j,
    'k': char_k,
    'l': char_l,
    'm': char_m,
    'n': char_n,
    'o': char_o,
    'p': char_p,
    'q': char_q,
    'r': char_r,
    's': char_s,
    't': char_t,
    'u': char_u,
    'v': char_v,
    'w': char_w,
    'x': char_x,
    'y': char_y,
    'z': char_z,
    ' ': char_space
}


def beautiful_word(word, separator='   '):
    for line in range(len(char_b)):
        for character in word:
            current_char = char_map[character.lower()]
            print(current_char[line], end=separator)
        print()


beautiful_word('beautiful word')
