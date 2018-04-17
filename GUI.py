# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class FrmMain
###########################################################################

class FrmMain ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Scope Cap Chart Generator", pos = wx.DefaultPosition, size = wx.Size( 675,675 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 675,675 ), wx.DefaultSize )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelBallistics = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		gbSizer4 = wx.GridBagSizer( 0, 0 )
		gbSizer4.SetFlexibleDirection( wx.BOTH )
		gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( self.panelBallistics, wx.ID_ANY, u"Load File:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gbSizer4.Add( self.m_staticText4, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self.panelBallistics, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gbSizer4.Add( self.m_filePicker1, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnLoad = wx.Button( self.panelBallistics, wx.ID_ANY, u"Load", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer4.Add( self.btnLoad, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gbSizer4.AddGrowableCol( 1 )
		
		gbSizer3.Add( gbSizer4, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 6 ), wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self.panelBallistics, wx.ID_ANY, u"Min Range:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gbSizer3.Add( self.m_staticText1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrl_Min_Range = wx.SpinCtrl( self.panelBallistics, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0 )
		gbSizer3.Add( self.spinCtrl_Min_Range, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.panelBallistics, wx.ID_ANY, u"Max Range:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gbSizer3.Add( self.m_staticText2, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrl_Max_Range = wx.SpinCtrl( self.panelBallistics, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0 )
		gbSizer3.Add( self.spinCtrl_Max_Range, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText3 = wx.StaticText( self.panelBallistics, wx.ID_ANY, u"Step:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gbSizer3.Add( self.m_staticText3, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrl_Step = wx.SpinCtrl( self.panelBallistics, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10000, 0 )
		gbSizer3.Add( self.spinCtrl_Step, wx.GBPosition( 1, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnRefresh = wx.Button( self.panelBallistics, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btnRefresh, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnReset = wx.Button( self.panelBallistics, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btnReset, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.btnClear = wx.Button( self.panelBallistics, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.btnClear, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gbSizer3.Add( bSizer1, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 6 ), wx.EXPAND, 5 )
		
		self.gridBallistics = wx.grid.Grid( self.panelBallistics, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.ALWAYS_SHOW_SB|wx.HSCROLL|wx.VSCROLL )
		
		# Grid
		self.gridBallistics.CreateGrid( 5, 5 )
		self.gridBallistics.EnableEditing( True )
		self.gridBallistics.EnableGridLines( True )
		self.gridBallistics.EnableDragGridSize( False )
		self.gridBallistics.SetMargins( 0, 0 )
		
		# Columns
		self.gridBallistics.SetColSize( 0, 29 )
		self.gridBallistics.SetColSize( 1, 28 )
		self.gridBallistics.SetColSize( 2, 29 )
		self.gridBallistics.SetColSize( 3, 29 )
		self.gridBallistics.SetColSize( 4, 356 )
		self.gridBallistics.AutoSizeColumns()
		self.gridBallistics.EnableDragColMove( False )
		self.gridBallistics.EnableDragColSize( True )
		self.gridBallistics.SetColLabelSize( 30 )
		self.gridBallistics.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gridBallistics.SetRowSize( 0, 5 )
		self.gridBallistics.AutoSizeRows()
		self.gridBallistics.EnableDragRowSize( True )
		self.gridBallistics.SetRowLabelSize( 1 )
		self.gridBallistics.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.gridBallistics.SetDefaultCellAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		gbSizer3.Add( self.gridBallistics, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 6 ), wx.ALL|wx.EXPAND, 5 )
		
		
		gbSizer3.AddGrowableCol( 1 )
		gbSizer3.AddGrowableCol( 3 )
		gbSizer3.AddGrowableCol( 5 )
		gbSizer3.AddGrowableRow( 3 )
		
		self.panelBallistics.SetSizer( gbSizer3 )
		self.panelBallistics.Layout()
		gbSizer3.Fit( self.panelBallistics )
		self.m_notebook1.AddPage( self.panelBallistics, u"Ballistics", True )
		self.panelPreview = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.btnPreview = wx.Button( self.panelPreview, wx.ID_ANY, u"Preview", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.btnPreview, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnExport = wx.Button( self.panelPreview, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.btnExport, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticText6 = wx.StaticText( self.panelPreview, wx.ID_ANY, u"Header Color:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gbSizer2.Add( self.m_staticText6, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.cpHeader = wx.ColourPickerCtrl( self.panelPreview, wx.ID_ANY, wx.Colour( 255, 255, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		gbSizer2.Add( self.cpHeader, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.panelPreview, wx.ID_ANY, u"Row Color:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gbSizer2.Add( self.m_staticText5, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.cpRow = wx.ColourPickerCtrl( self.panelPreview, wx.ID_ANY, wx.Colour( 255, 255, 255 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		gbSizer2.Add( self.cpRow, wx.GBPosition( 1, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.m_staticText7 = wx.StaticText( self.panelPreview, wx.ID_ANY, u"Alt Row Color:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gbSizer2.Add( self.m_staticText7, wx.GBPosition( 1, 4 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		self.cpAltRow = wx.ColourPickerCtrl( self.panelPreview, wx.ID_ANY, wx.Colour( 0, 255, 0 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		gbSizer2.Add( self.cpAltRow, wx.GBPosition( 1, 5 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		self.imgPreview = wx.StaticBitmap( self.panelPreview, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.imgPreview, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 6 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		gbSizer2.AddGrowableRow( 2 )
		
		self.panelPreview.SetSizer( gbSizer2 )
		self.panelPreview.Layout()
		gbSizer2.Fit( self.panelPreview )
		self.m_notebook1.AddPage( self.panelPreview, u"Preview", False )
		
		gbSizer1.Add( self.m_notebook1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 4 ), wx.EXPAND, 5 )
		
		
		gbSizer1.AddGrowableCol( 0 )
		gbSizer1.AddGrowableRow( 0 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 1, 0, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.btnLoad_Click )
		self.btnLoad.Bind( wx.EVT_BUTTON, self.btnLoad_Click )
		self.spinCtrl_Min_Range.Bind( wx.EVT_SPINCTRL, self.refresh )
		self.spinCtrl_Min_Range.Bind( wx.EVT_TEXT, self.refresh )
		self.spinCtrl_Min_Range.Bind( wx.EVT_TEXT_ENTER, self.refresh )
		self.spinCtrl_Max_Range.Bind( wx.EVT_SPINCTRL, self.refresh )
		self.spinCtrl_Max_Range.Bind( wx.EVT_TEXT, self.refresh )
		self.spinCtrl_Max_Range.Bind( wx.EVT_TEXT_ENTER, self.refresh )
		self.spinCtrl_Step.Bind( wx.EVT_SPINCTRL, self.refresh )
		self.spinCtrl_Step.Bind( wx.EVT_TEXT, self.refresh )
		self.spinCtrl_Step.Bind( wx.EVT_TEXT_ENTER, self.refresh )
		self.btnRefresh.Bind( wx.EVT_BUTTON, self.btnRefresh_Click )
		self.btnReset.Bind( wx.EVT_BUTTON, self.btnReset_Click )
		self.btnClear.Bind( wx.EVT_BUTTON, self.btnClear_Click )
		self.btnPreview.Bind( wx.EVT_BUTTON, self.btnPreview_Click )
		self.btnExport.Bind( wx.EVT_BUTTON, self.btnExport_Click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def btnLoad_Click( self, event ):
		event.Skip()
	
	
	def refresh( self, event ):
		event.Skip()
	
	
	
	
	
	
	
	
	
	def btnRefresh_Click( self, event ):
		event.Skip()
	
	def btnReset_Click( self, event ):
		event.Skip()
	
	def btnClear_Click( self, event ):
		event.Skip()
	
	def btnPreview_Click( self, event ):
		event.Skip()
	
	def btnExport_Click( self, event ):
		event.Skip()
	

###########################################################################
## Class dlSave
###########################################################################

class dlSave ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Save Chart", pos = wx.DefaultPosition, size = wx.Size( 575,125 ), style = wx.CAPTION )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		gbSizer5 = wx.GridBagSizer( 0, 0 )
		gbSizer5.SetFlexibleDirection( wx.BOTH )
		gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.fpDlSave = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gbSizer5.Add( self.fpDlSave, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.btnDlSave = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.btnDlSave, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.btnDlCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer5.Add( self.btnDlCancel, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		
		gbSizer5.AddGrowableCol( 0 )
		
		self.SetSizer( gbSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

