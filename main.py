import wx
import ui
import numpy as np
from math import *
resistor_standard = {
    "E6": np.array([1.0, 1.5, 2.2, 3.3, 4.7, 6.8]),
    "E12": np.array([1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]),
    "E24": np.array([1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]),
    "E48": np.array([1.00, 1.05, 1.10, 1.15, 1.21, 1.27, 1.33, 1.40, 1.47, 1.54, 1.62, 1.69, 1.78, 1.87, 1.91, 1.96, 2.05, 2.15, 2.26,
                     2.37, 2.49, 2.61, 2.74, 2.80, 2.87, 3.01, 3.16, 3.32, 3.48, 3.57, 3.65, 3.83, 4.02, 4.22, 4.42, 4.64, 4.87, 5.11, 5.36, 5.62, 5.90, 6.19, 6.34, 6.49, 6.81, 7.15, 7.50, 7.87, 8.25, 8.66, 9.09, 9.53]),
    "E96": np.array([1.00, 1.02, 1.05, 1.07, 1.10, 1.13, 1.15, 1.18, 1.21, 1.24, 1.27, 1.30, 1.33, 1.37,
                     1.40, 1.43, 1.47, 1.50, 1.54, 1.58, 1.62, 1.65, 1.69, 1.74, 1.78, 1.82, 1.87, 1.91,
                     1.96, 2.00, 2.05, 2.10, 2.15, 2.21, 2.26, 2.32, 2.37, 2.43, 2.49, 2.55, 2.61, 2.67,
                     2.74, 2.80, 2.87, 2.94, 3.01, 3.09, 3.16, 3.24, 3.32, 3.40, 3.48, 3.57, 3.65, 3.74,
                     3.83, 3.92, 4.02, 4.12, 4.22, 4.32, 4.42, 4.53, 4.64, 4.75, 4.87, 4.99, 5.11, 5.23,
                     5.36, 5.49, 5.62, 5.76, 5.90, 6.04, 6.19, 6.34, 6.49, 6.65, 6.81, 6.98, 7.15, 7.32,
                     7.50, 7.68, 7.87, 8.06, 8.25, 8.45, 8.66, 8.87, 9.09, 9.31, 9.53, 9.76]),
    "E192": np.array([1.00, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.09, 1.10, 1.11, 1.13,
                      1.14, 1.15, 1.17, 1.18, 1.20, 1.21, 1.23, 1.24, 1.26, 1.27, 1.29, 1.30,
                      1.32, 1.33, 1.35, 1.37, 1.38, 1.40, 1.42, 1.43, 1.45, 1.47, 1.49, 1.50,
                      1.52, 1.54, 1.56, 1.58, 1.60, 1.62, 1.64, 1.65, 1.67, 1.69, 1.72, 1.74,
                      1.76, 1.78, 1.80, 1.82, 1.84, 1.87, 1.89, 1.91, 1.93, 1.96, 1.98, 2.00,
                      2.03, 2.05, 2.08, 2.10, 2.13, 2.15, 2.18, 2.21, 2.23, 2.26, 2.29, 2.32,
                      2.34, 2.37, 2.40, 2.43, 2.46, 2.49, 2.52, 2.55, 2.58, 2.61, 2.64, 2.67,
                      2.71, 2.74, 2.77, 2.80, 2.84, 2.87, 2.91, 2.94, 2.98, 3.01, 3.05, 3.09,
                      3.12, 3.16, 3.20, 3.24, 3.28, 3.32, 3.36, 3.40, 3.44, 3.48, 3.52, 3.57,
                      3.61, 3.65, 3.70, 3.74, 3.79, 3.83, 3.88, 3.97, 4.02, 4.07, 4.12, 4.17,
                      4.22, 4.27, 4.32, 4.37, 4.42, 4.48, 4.53, 4.59, 4.64, 4.70, 4.75, 4.81,
                      4.87, 4.93, 4.99, 5.05, 5.11, 5.17, 5.23, 5.30, 5.36, 5.42, 5.49, 5.56,
                      5.62, 5.69, 5.76, 5.83, 5.90, 5.97, 6.04, 6.12, 6.19, 6.26, 6.34, 6.42,
                      6.49, 6.57, 6.65, 6.73, 6.81, 6.90, 6.98, 7.06, 7.15, 7.23, 7.32, 7.41,
                      7.50, 7.59, 7.68, 7.77, 7.87, 7.96, 8.06, 8.16, 8.25, 8.35, 8.45, 8.56,
                      8.66, 8.76, 8.87, 8.98, 9.09, 9.20, 9.31, 9.42, 9.53, 9.65, 9.76, 9.88])
}


class Frame(ui.MyFrame1):
    def __init__(self, parent):
        ui.MyFrame1.__init__(self, parent)
        self.ratio = None

    def CalculateRatio(self, event):
        try:
            ratio = eval(self.m_textCtrl1.GetValue())
        except Exception:
            self.m_staticText4.SetLabel("求值错误")
            self.ratio = None
        else:
            if isinstance(ratio, (float, int)):
                self.ratio = ratio
                if ratio > 0:
                    self.m_staticText4.SetLabel(str(ratio))
                else:
                    self.m_staticText4.SetLabel("比例小于0！")
            else:
                self.m_staticText4.SetLabel("求值错误")
                self.ratio = None
        event.Skip()

    def Calculate(self, event):
        self.CalculateRatio(event)
        if self.ratio:
            RupType = self.m_choice1.GetSelection()
            RupStandard = self.m_choice11.GetSelection()
            RdownType = self.m_choice12.GetSelection()
            RdownStandard = self.m_choice111.GetSelection()

            if RupType == 0:
                RupSet = resistor_standard[self.m_choice11.GetString(
                    RupStandard)]
                Rups = RupSet
            if RupType == 1:
                RupSet = resistor_standard[self.m_choice11.GetString(
                    RupStandard)]
                RupSet = np.array(np.meshgrid(RupSet, RupSet)).T.reshape(-1, 2)
                Rups = RupSet[:, 0]+RupSet[:, 1]
            if RupType == 2:
                RupSet = resistor_standard[self.m_choice11.GetString(
                    RupStandard)]
                RupSet = np.array(np.meshgrid(RupSet, RupSet)).T.reshape(-1, 2)
                Rups = (RupSet[:, 0]**-1+RupSet[:, 1]**-1)**-1

            if RdownType == 0:
                RdownSet = resistor_standard[self.m_choice111.GetString(
                    RdownStandard)]
                Rdowns = RdownSet
            if RdownType == 1:
                RdownSet = resistor_standard[self.m_choice111.GetString(
                    RdownStandard)]
                RdownSet = np.array(np.meshgrid(
                    RdownSet, RdownSet)).T.reshape(-1, 2)
                Rdowns = RdownSet[:, 0]+RdownSet[:, 1]
            if RdownType == 2:
                RdownSet = resistor_standard[self.m_choice111.GetString(
                    RdownStandard)]
                RdownSet = np.array(np.meshgrid(
                    RdownSet, RdownSet)).T.reshape(-1, 2)
                Rdowns = (RdownSet[:, 0]**-1+RdownSet[:, 1]**-1)**-1
            tarUP = Rdowns*self.ratio
            tarUP_uni = tarUP/10.**(np.log10(tarUP) -
                                    np.where(tarUP < 1, 1-1e-7, 0)).astype(np.int)

            Rups_sorted = np.sort(Rups)
            Rups_sortIndex = np.argsort(Rups)
            Tops = []
            for i in range(len(tarUP_uni)):
                center = InsertIndex(Rups_sorted, tarUP_uni[i])
                js = np.arange(center-1, center+2)
                js = js[np.logical_and(js >= 0, js < len(Rups_sorted))]
                js = Rups_sortIndex[js]
                ijs = [[i, j] for j in js]
                Tops += ijs

            ratio = [Rups[t[1]] * (tarUP[t[0]]/tarUP_uni[t[0]]) /
                     Rdowns[t[0]] for t in Tops]
            indexs = np.argsort(np.abs(np.array(ratio)-self.ratio))
            for i in range(10):
                t = Tops[indexs[i]]
                k = (tarUP[t[0]]/tarUP_uni[t[0]])
                if RupType == 0:
                    self.m_grid3.SetCellValue(
                        i, 0, strRes(RupSet[Tops[indexs[i]][1]]*k))
                    self.m_grid3.SetCellValue(i, 1, '')
                else:
                    self.m_grid3.SetCellValue(
                        i, 0, strRes(RupSet[Tops[indexs[i]][1], 0]*k))
                    self.m_grid3.SetCellValue(
                        i, 1, strRes(RupSet[Tops[indexs[i]][1], 1]*k))

                if RdownType == 0:
                    self.m_grid3.SetCellValue(
                        i, 2, strRes(RdownSet[Tops[indexs[i]][0]]))
                    self.m_grid3.SetCellValue(i, 3, '')
                else:
                    self.m_grid3.SetCellValue(
                        i, 2, strRes(RdownSet[Tops[indexs[i]][0], 0]))
                    self.m_grid3.SetCellValue(
                        i, 3, strRes(RdownSet[Tops[indexs[i]][0], 1]))
                self.m_grid3.SetCellValue(
                    i, 4, "%.5e @%.2f %%" % (ratio[indexs[i]], (ratio[indexs[i]]-self.ratio)/self.ratio*100))

        event.Skip()


def strRes(R, acc=4):
    if R < 1:
        R = R*1e3
        unit = 'm'
    elif R < 1e3:
        unit = ''
    elif R < 1e6:
        R = R*1e-3
        unit = 'k'
    elif R < 1e9:
        R = R*1e-6
        unit = "M"
    elif R < 1e12:
        R = R*1e-9
        unit = "G"
    else:
        R = R*1e-12
        unit = "T"
    return str(round(R, acc))+unit


def InsertIndex(arr, value):
    Range = [0, len(arr)]
    while Range[1]-Range[0] > 1:
        i = round((Range[1]+Range[0])/2)
        if arr[i] > value:
            Range[1] = i
        elif arr[i] == value:
            return i
        else:
            Range[0] = i
    return Range[1]


app = wx.App(False)
frame = Frame(None)
frame.Show(True)
app.MainLoop()
