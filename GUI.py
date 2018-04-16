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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Scope Cap Chart Generator", pos = wx.DefaultPosition, size = wx.Size( 475,475 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 475,475 ), wx.DefaultSize )
		
		gbSizer1 = wx.GridBagSizer( 0, 0 )
		gbSizer1.SetFlexibleDirection( wx.BOTH )
		gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.panelBallistics = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self.panelBallistics, wx.ID_ANY, u"Min Range:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gbSizer3.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrl_Min_Range = wx.SpinCtrl( self.panelBallistics, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 5000, 0 )
		gbSizer3.Add( self.spinCtrl_Min_Range, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.panelBallistics, wx.ID_ANY, u"Max Range:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gbSizer3.Add( self.m_staticText2, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.spinCtrl_Max_Range = wx.SpinCtrl( self.panelBallistics, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 5000, 0 )
		gbSizer3.Add( self.spinCtrl_Max_Range, wx.GBPosition( 0, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnRefresh = wx.Button( self.panelBallistics, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.btnRefresh, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.btnClear = wx.Button( self.panelBallistics, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer3.Add( self.btnClear, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
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
		gbSizer3.Add( self.gridBallistics, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND, 5 )
		
		
		gbSizer3.AddGrowableCol( 1 )
		gbSizer3.AddGrowableCol( 3 )
		gbSizer3.AddGrowableRow( 2 )
		
		self.panelBallistics.SetSizer( gbSizer3 )
		self.panelBallistics.Layout()
		gbSizer3.Fit( self.panelBallistics )
		self.m_notebook1.AddPage( self.panelBallistics, u"Ballistics", True )
		self.panelPreview = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer2 = wx.GridBagSizer( 0, 0 )
		gbSizer2.SetFlexibleDirection( wx.BOTH )
		gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.imgPreview = wx.StaticBitmap( self.panelPreview, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.imgPreview, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
		
		self.btnExport = wx.Button( self.panelPreview, wx.ID_ANY, u"Export", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.btnExport, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.btnPreview = wx.Button( self.panelPreview, wx.ID_ANY, u"Preview", wx.DefaultPosition, wx.DefaultSize, 0 )
		gbSizer2.Add( self.btnPreview, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		
		gbSizer2.AddGrowableCol( 0 )
		gbSizer2.AddGrowableRow( 1 )
		
		self.panelPreview.SetSizer( gbSizer2 )
		self.panelPreview.Layout()
		gbSizer2.Fit( self.panelPreview )
		self.m_notebook1.AddPage( self.panelPreview, u"Preview", False )
		
		gbSizer1.Add( self.m_notebook1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 4 ), wx.EXPAND, 5 )
		
		
		gbSizer1.AddGrowableCol( 0 )
		gbSizer1.AddGrowableRow( 0 )
		
		self.SetSizer( gbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.spinCtrl_Min_Range.Bind( wx.EVT_SPINCTRL, self.refresh )
		self.spinCtrl_Min_Range.Bind( wx.EVT_TEXT_ENTER, self.refresh )
		self.spinCtrl_Max_Range.Bind( wx.EVT_SPINCTRL, self.refresh )
		self.spinCtrl_Max_Range.Bind( wx.EVT_TEXT_ENTER, self.refresh )
		self.btnRefresh.Bind( wx.EVT_BUTTON, self.btnRefresh_Click )
		self.btnClear.Bind( wx.EVT_BUTTON, self.btnClear_Click )
		self.btnExport.Bind( wx.EVT_BUTTON, self.btnExport_Click )
		self.btnPreview.Bind( wx.EVT_BUTTON, self.btnPreview_Click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def refresh( self, event ):
		event.Skip()
	
	
	
	
	def btnRefresh_Click( self, event ):
		event.Skip()
	
	def btnClear_Click( self, event ):
		event.Skip()
	
	def btnExport_Click( self, event ):
		event.Skip()
	
	def btnPreview_Click( self, event ):
		event.Skip()
	

