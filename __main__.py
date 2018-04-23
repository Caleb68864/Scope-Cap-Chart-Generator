from ImageGen import ImageGen
from Ballistics import Ballistics
import wx
from GUI import FrmMain
from GUI import dlSave
from DataTable import DataTable


class Main(wx.Frame):
    def __init__(self, parent):
        FrmMain.__init__(self, parent)

        self.ballistics = Ballistics()
        self.table = DataTable(self.ballistics.ballistics)
        self.ig = ""
        self.cbs = []
        self.cols = []

        ico = wx.Icon('sccg.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

        gsz = self.panelBallistics.GetSizer()
        self.szSelects = wx.BoxSizer(wx.HORIZONTAL)
        gsz.Add(self.szSelects, wx.GBPosition(3, 0), wx.GBSpan(1, 6), wx.EXPAND, 5)
        self.gridBallistics.Refresh()
        self.panelBallistics.Layout()

        self.refresh()
        self.Show(True)

    def refresh(self,instance=None):
        if self.spinCtrl_Min_Range.GetValue() > self.spinCtrl_Max_Range.GetValue():
            self.spinCtrl_Max_Range.SetValue(self.spinCtrl_Min_Range.GetValue())

        self.ballistics.reset()
        self.ballistics.setrangecol(self.cboxRangeCol.GetStringSelection())
        self.ballistics.setrange(self.spinCtrl_Min_Range.GetValue(), self.spinCtrl_Max_Range.GetValue(), self.spinCtrl_Step.GetValue())
        self.ballistics.selectcolumns(self.cols)
        self.table = DataTable(self.ballistics.ballistics)
        self.gridBallistics.SetTable(self.table, True)
        self.gridBallistics.AutoSizeColumns()
        self.gridBallistics.AutoSizeRows()
        self.gridBallistics.Refresh()

        self.panelBallistics.Layout()

    def setstatus(self, msg):
        self.statusBar.PushStatusText(msg)

    def genimage(self):
        self.ig = ImageGen(self.ballistics.ballistics, self.setstatus)
        self.ig.setheadercolor(self.cpHeader.GetColour())
        self.ig.setrowcolor(self.cpRow.GetColour())
        self.ig.setaltrowcolor(self.cpAltRow.GetColour())
        self.ig.setheaderfontcolor(self.cpHeaderFont.GetColour())
        self.ig.setfontcolor(self.cpFont.GetColour())
        self.ig.setlinecolor(self.cpLine.GetColour())
        self.ig.genimage()

    def gencols(self):
        self.cbs = []
        for child in self.szSelects.GetChildren():
            child.DeleteWindows()

        cbSelectAll = wx.CheckBox(self.panelBallistics, wx.ID_ANY, u"Select All", wx.DefaultPosition,
                                  wx.DefaultSize, 0)
        cbSelectAll.SetValue(True)
        cbSelectAll.Bind(wx.EVT_CHECKBOX, self.cbSelectAll_Click)
        self.szSelects.Add(cbSelectAll, 0, wx.ALL, 5)

        for column in list(self.ballistics.orig_ballistics.columns.values):
            # print(column)
            cb = wx.CheckBox(self.panelBallistics, wx.ID_ANY, column, wx.DefaultPosition, wx.DefaultSize, 0)
            cb.SetName(column)
            cb.SetValue(True)
            cb.Bind(wx.EVT_CHECKBOX, self.cbSelect_Click)
            self.cbs.append(cb)
            self.szSelects.Add(cb, 0, wx.ALL, 5)

        self.cboxRangeCol.SetItems(self.ballistics.orig_ballistics.columns.values)
        self.cboxRangeCol.SetSelection(0)

        self.gridBallistics.Refresh()
        self.panelBallistics.Layout()

    def btnPreview_Click(self, instance):
        if not self.ballistics.ballistics.empty:
            orig_size = self.imgPreview.GetSize()
            # print(orig_size)
            self.genimage()
            img = self.ig.getwximage()
            s = min(float(s) for s in orig_size)
            bmap = wx.Bitmap(self.ig.getwximage().Scale(s, s, wx.IMAGE_QUALITY_HIGH))
            self.imgPreview.SetBitmap(bmap)
            self.imgPreview.Refresh()
            self.imgPreview.Layout()
            self.setstatus("Preview Loaded.")
            # print("BitMap Set")
        else:
            self.setstatus("Data Empty Please Load A Ballistics File.")

        #print(self.imgPreview.GetBestSize())

    def btnExport_Click(self, instance):
        dl = dlSave(self)
        dl.btnDlSave.SetId(wx.ID_OK)
        dl.btnDlCancel.SetId(wx.ID_CANCEL)
        d = dl.ShowModal()

        if d == wx.ID_OK:
            self.genimage()
            self.ig.imgsave(dl.fpDlSave.GetPath())
            dl.Destroy()

    def btnRefresh_Click(self,instance):
        self.refresh()

    def btnClear_Click(self, instance):
        self.cbs = []
        for child in self.szSelects.GetChildren():
            child.DeleteWindows()
        self.cboxRangeCol.Clear()
        self.spinCtrl_Min_Range.SetValue(0)
        self.spinCtrl_Max_Range.SetValue(0)
        self.spinCtrl_Step.SetValue(0)
        self.m_filePicker1.SetPath("")
        self.setstatus("")
        self.ballistics = Ballistics()
        self.refresh()

    def btnReset_Click(self, instance):
        self.cboxRangeCol.SetSelection(0)
        self.spinCtrl_Min_Range.SetValue(0)
        self.spinCtrl_Max_Range.SetValue(0)
        self.spinCtrl_Step.SetValue(0)
        self.setstatus("")
        self.refresh()

    def btnLoad_Click(self, instance):
        if self.m_filePicker1.GetPath() != "":
            self.ballistics = Ballistics(self.m_filePicker1.GetPath())
            self.gencols()
            self.refresh()
        else:
            print("No File Selected")
            self.setstatus("No File Selected.")

    def cbSelectAll_Click(self, instance):
        if instance.GetEventObject().IsChecked():
            for cb in self.cbs:
                cb.SetValue(True)
        else:
            for cb in self.cbs:
                cb.SetValue(False)
        self.cbSelect_Click(instance)

    def cbSelect_Click(self, instance):
        self.cols = []
        for index, cb in enumerate(self.cbs):
            if cb.IsChecked():
                #print(cb.GetName(), index)
                self.cols.append(index)
        #print(self.cols)
        self.refresh()

    def cboxRangeCol_Change(self, instance):
        print(instance.GetEventObject().GetStringSelection())
        self.refresh()


if __name__ == "__main__":
    app = wx.App(False)
    frame = Main(None)
    app.MainLoop()