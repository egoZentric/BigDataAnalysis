import gzip

f_Obj = gzip.open("./foo/bar.gz", 'rb')
s_Str = f_Obj.read()
f_Obj.close()

print s_Str
