import app
import ui
import player
import localeInfo
import uiScriptLocale
import constInfo
FILE_NAME_LEN = 54

class Item(ui.ListBoxEx.Item):
	def __init__(self, fileName):
		ui.ListBoxEx.Item.__init__(self)
		self.canLoad=0
		self.text=fileName
		self.textLine=self.__CreateTextLine(fileName[:FILE_NAME_LEN])

	def __del__(self):
		ui.ListBoxEx.Item.__del__(self)

	def GetText(self):
		return self.text

	def OnMouseLeftButtonDoubleClick(self):
		constInfo.DROP_LIST_DOUBLE = 1

	def SetSize(self, width, height):
		ui.ListBoxEx.Item.SetSize(self, 6*30, height)

	def __CreateTextLine(self, fileName):
		textLine=ui.TextLine()
		textLine.SetParent(self)

		if localeInfo.IsARABIC():
			textLine.SetPosition(6*len(fileName) + 6, 0)
		else:
			textLine.SetPosition(0, 0)

		textLine.SetText(fileName)
		textLine.Show()
		return textLine

class PopupDialog(ui.ScriptWindow):
	def __init__(self, parent):
		ui.ScriptWindow.__init__(self)

		self.__Load()
		self.__Bind()

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def __Load(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/PopupDialog.py")
		except:
			import exception
			exception.Abort("PopupDialog.__Load")

	def __Bind(self):
		try:
			self.textLine=self.GetChild("message")
			self.okButton=self.GetChild("accept")
		except:
			import exception
			exception.Abort("PopupDialog.__Bind")

		self.okButton.SAFE_SetEvent(self.__OnOK)

	def Open(self, msg):
		self.textLine.SetText(msg)
		self.SetCenterPosition()
		self.Show()
		self.SetTop()

	def __OnOK(self):
		self.Hide()

class FileListDialog(ui.ScriptWindow):
	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.isLoaded=0
		self.selectEvent=None
		self.fileListBox=None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		if self.isLoaded==0:
			self.isLoaded=1

			self.__Load()

		ui.ScriptWindow.Show(self)

	def Open(self):
		self.Show()

		self.SetCenterPosition()
		self.SetTop()

	def Close(self):
		self.popupDialog.Hide()
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def SAFE_SetSelectEvent(self, event):
		self.selectEvent=ui.__mem_func__(event)

	def __CreateFileListBox(self):
		fileListBox=ui.ListBoxEx()
		fileListBox.SetParent(self)
		
		if localeInfo.IsARABIC():
			fileListBox.SetPosition( self.GetWidth() - fileListBox.GetWidth() - 10, 50)
		else:
			fileListBox.SetPosition(15, 50)

		fileListBox.Show()
		return fileListBox

	def __Load(self):
		self.popupDialog=PopupDialog(self)

		self.__Load_LoadScript("UIScript/droplistwindow.py")

		self.__Load_BindObject()

		self.refreshButton.SetEvent(ui.__mem_func__(self.__OnRefresh))
		self.okButton.SetEvent(ui.__mem_func__(self.__OnOK))
		self.board.SetCloseEvent(ui.__mem_func__(self.__OnCancel))
		self.UpdateRect()

		self.__RefreshFileList()

	def __Load_LoadScript(self, fileName):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, fileName)
		except:
			import exception
			exception.Abort("DropListBox.__Load")

	def __Load_BindObject(self):
		try:
			self.fileListBox=self.__CreateFileListBox()
			self.Scroll = self.GetChild("ScrollBar")
			self.fileListBox.SetScrollBar(self.Scroll)
			self.board=self.GetChild("board")
			self.okButton=self.GetChild("ok")
			self.refreshButton=self.GetChild("refresh")
			self.popupText = self.popupDialog.GetChild("message")
		except:
			import exception
			exception.Abort("DropListBox.__Bind")

	def __PopupMessage(self, msg):
		self.popupDialog.Open(msg)

	def __OnOK(self):
		selItem = self.fileListBox.GetSelectedItem()
		constInfo.DROP_LIST_SLIDER = self.Scroll.GetPos()
		if selItem:
			syntax = selItem.GetText()
			vid = (syntax.split(":")[1])
			player.SendClickItemPacketDropList(int(vid))
		else:
			self.__PopupMessage(localeInfo.DROP_LIST_EMPTY_SELECT)

	def __OnCancel(self):
		self.Hide()

	def __OnRefresh(self):
		self.__RefreshFileList()

	def OnUpdate(self):
		if (constInfo.DROP_LIST_DOUBLE):
			self.__OnOK()
			constInfo.DROP_LIST_DOUBLE = 0
		if constInfo.DROP_LIST_REFRESH:
			self.__RefreshFileList()
			constInfo.DROP_LIST_REFRESH = 0

	def __RefreshFileList(self):
		self.__ClearFileList()
		self.__ApendDropItemList()
		self.Scroll.SetPos(constInfo.DROP_LIST_SLIDER)

	def __ClearFileList(self):
		self.fileListBox.RemoveAllItems()

	def __ApendDropItemList(self):
		for key, value in sorted(constInfo.DROPLIST_VID_AND_ITEM_NAME.items(), key=lambda item: item[1]):
			if key in constInfo.OWN_ITEM_VID:
				self.fileListBox.AppendItem(Item("%s|c00000000:%d" % (constInfo.DROPLIST_VID_AND_ITEM_NAME[key], key)))

	def __ApendDropItem(self, fileName):
		self.fileListBox.AppendItem(Item(fileName))


