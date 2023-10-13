import random

def gen_pass(pass_length):
    character = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    length = int(input('Masukkan panjang sandi:'))
    password = ""

    for i in range(pass_length):
        password += random.choice(character)

    print (password)

def flipcoin():
    coin = random.randint(1, 2)
    if coin == 1:
        return 'Heads'
    else:
        return 'Tails'

def sampah_anorganik():
    sampah = ['botol plastik', 'kantong plastik', 'kertas', 'kabel', 'gadget rusak', 'kaca', 'besi rusak']

    return random.choice(sampah)

def sampah_organik():
    sampah = ['daun', 'kulit buah', 'sisa makanan', 'sayur', 'tai hewan', 'tulang']

    return random.choice(sampah)
