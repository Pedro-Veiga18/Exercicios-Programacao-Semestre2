def func():
    minhavar = [1, 2, 3]
    
    def func2(minhavar):
        minhavar[0] = 4
        
    func2(minhavar)
    return minhavar

print(func())