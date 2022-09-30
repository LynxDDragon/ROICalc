Invest = 4000
Rent = 700
Loss = 100

def ROI(Invest, Rent, Loss):
    NetProfit = Rent * 12 - Loss
    ROI = (NetProfit/Invest) * 100
    print(ROI)

ROI(Invest, Rent, Loss)