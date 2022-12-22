# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
# Class MyFrame1
###########################################################################


class MyFrame1 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            556, 706), style=wx.CAPTION | wx.CLOSE_BOX | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(
            self, wx.ID_ANY, u"电阻分压计算器", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        self.m_staticText2.SetFont(wx.Font(
            40, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        bSizer3.Add(self.m_staticText2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        sbSizer1 = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, u"目标值"), wx.VERTICAL)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(sbSizer1.GetStaticBox(
        ), wx.ID_ANY, u"目标分压比 ： ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        bSizer4.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(sbSizer1.GetStaticBox(
        ), wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER | wx.TE_PROCESS_TAB)
        bSizer4.Add(self.m_textCtrl1, 1, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(sbSizer1.GetStaticBox(
        ), wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size(100, -1), 0 | wx.BORDER_SIMPLE)
        self.m_staticText4.Wrap(-1)

        bSizer4.Add(self.m_staticText4, 0, wx.ALL, 5)

        sbSizer1.Add(bSizer4, 1, wx.EXPAND, 5)

        bSizer3.Add(sbSizer1, 0, wx.EXPAND, 5)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(
            self, wx.ID_ANY, u"上臂电阻"), wx.VERTICAL)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5 = wx.StaticText(sbSizer3.GetStaticBox(
        ), wx.ID_ANY, u"电阻连接类型 ： ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText5.Wrap(-1)

        bSizer5.Add(self.m_staticText5, 1, wx.ALL, 5)

        m_choice1Choices = [u"单电阻", u"双电阻串联", u"双电阻并联"]
        self.m_choice1 = wx.Choice(sbSizer3.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        bSizer5.Add(self.m_choice1, 0, wx.ALL, 5)

        sbSizer3.Add(bSizer5, 0, wx.EXPAND, 5)

        bSizer51 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText51 = wx.StaticText(sbSizer3.GetStaticBox(
        ), wx.ID_ANY, u"IEC电阻标准 ： ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText51.Wrap(-1)

        bSizer51.Add(self.m_staticText51, 1, wx.ALL, 5)

        m_choice11Choices = [u"E6", u"E12", u"E24", u"E48", u"E96", u"E192"]
        self.m_choice11 = wx.Choice(sbSizer3.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_choice11Choices, 0)
        self.m_choice11.SetSelection(0)
        bSizer51.Add(self.m_choice11, 0, wx.ALL, 5)

        sbSizer3.Add(bSizer51, 0, wx.EXPAND, 5)

        bSizer3.Add(sbSizer3, 0, wx.EXPAND, 5)

        sbSizer31 = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, u"下臂电阻"), wx.VERTICAL)

        bSizer52 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText52 = wx.StaticText(sbSizer31.GetStaticBox(
        ), wx.ID_ANY, u"电阻连接类型 ： ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText52.Wrap(-1)

        bSizer52.Add(self.m_staticText52, 1, wx.ALL, 5)

        m_choice12Choices = [u"单电阻", u"双电阻串联", u"双电阻并联"]
        self.m_choice12 = wx.Choice(sbSizer31.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_choice12Choices, 0)
        self.m_choice12.SetSelection(0)
        bSizer52.Add(self.m_choice12, 0, wx.ALL, 5)

        sbSizer31.Add(bSizer52, 0, wx.EXPAND, 5)

        bSizer511 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText511 = wx.StaticText(sbSizer31.GetStaticBox(
        ), wx.ID_ANY, u"IEC电阻标准 ： ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText511.Wrap(-1)

        bSizer511.Add(self.m_staticText511, 1, wx.ALL, 5)

        m_choice111Choices = [u"E6", u"E12", u"E24", u"E48", u"E96", u"E192"]
        self.m_choice111 = wx.Choice(sbSizer31.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(100, -1), m_choice111Choices, 0)
        self.m_choice111.SetSelection(0)
        bSizer511.Add(self.m_choice111, 0, wx.ALL, 5)

        sbSizer31.Add(bSizer511, 0, wx.EXPAND, 5)

        bSizer3.Add(sbSizer31, 0, wx.EXPAND, 5)

        sbSizer15 = wx.StaticBoxSizer(
            wx.StaticBox(self, wx.ID_ANY, u"结果"), wx.VERTICAL)

        bSizer18 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid3 = wx.grid.Grid(sbSizer15.GetStaticBox(
        ), wx.ID_ANY, wx.DefaultPosition, wx.Size(520, -1), 0)

        # Grid
        self.m_grid3.CreateGrid(10, 5)
        self.m_grid3.EnableEditing(False)
        self.m_grid3.EnableGridLines(True)
        self.m_grid3.EnableDragGridSize(False)
        self.m_grid3.SetMargins(0, 0)

        # Columns
        self.m_grid3.SetColSize(0, 80)
        self.m_grid3.SetColSize(1, 80)
        self.m_grid3.SetColSize(2, 80)
        self.m_grid3.SetColSize(3, 80)
        self.m_grid3.SetColSize(4, 167)
        self.m_grid3.EnableDragColMove(False)
        self.m_grid3.EnableDragColSize(True)
        self.m_grid3.SetColLabelSize(30)
        self.m_grid3.SetColLabelValue(0, u"Rup_1")
        self.m_grid3.SetColLabelValue(1, u"Rup_2")
        self.m_grid3.SetColLabelValue(2, u"Rd1")
        self.m_grid3.SetColLabelValue(3, u"Rd2")
        self.m_grid3.SetColLabelValue(4, u"Result")
        self.m_grid3.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_grid3.EnableDragRowSize(True)
        self.m_grid3.SetRowLabelSize(30)
        self.m_grid3.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid3.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer18.Add(self.m_grid3, 0, wx.ALL, 5)

        self.m_button1 = wx.Button(sbSizer15.GetStaticBox(
        ), wx.ID_ANY, u"开始计算", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer18.Add(self.m_button1, 1, wx.ALL | wx.EXPAND, 5)

        sbSizer15.Add(bSizer18, 1, wx.EXPAND, 5)

        self.m_staticText8 = wx.StaticText(sbSizer15.GetStaticBox(
        ), wx.ID_ANY, u"Writen by coulson@mail.ustc.edu.cn", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        sbSizer15.Add(self.m_staticText8, 0, wx.ALL, 5)

        bSizer3.Add(sbSizer15, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_textCtrl1.Bind(wx.EVT_TEXT_ENTER, self.CalculateRatio)
        self.m_button1.Bind(wx.EVT_BUTTON, self.Calculate)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def CalculateRatio(self, event):
        event.Skip()

    def Calculate(self, event):
        event.Skip()
