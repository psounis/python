# default.values.order.py
def func(par1, par2, par3 = 0, par4 = 0):
    print(f"par1={par1} par2={par2} par3={par3} par4={par4}")

func(1,2,3,4)
func(1,2,3)
func(1,2)