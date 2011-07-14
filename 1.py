import string
# http://www.pythonchallenge.com/pc/def/map.html
# string.maketrans()
# string.translate()
crypto = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
_from = 'abcdefghijklmnopqrstuvwxyz'
_to = 'cdefghijklmnopqrstuvwxyxab'
table = string.maketrans(_from, _to)


def solve(message):
    return string.translate(message, table)

print solve(crypto)

url = """http://www.pythonchallenge.com/pc/def/map.html"""
print solve(url)

hint = """ynnjw rm rfc dgjclykc md rfgq nyec, zsr lmr rfc cvrclqgml"""
print solve(hint)