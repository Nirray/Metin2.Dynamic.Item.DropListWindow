# Search:
import interfaceModule
# Add below:
import uidroplist

# Search:
	self.quickSlotPageIndex = 0
# Add below:
	self.dropListDlg = 0

# Search:
	def __BuildKeyDict(self):

# Below:
	onPressKeyDict[app.DIK_F4]	= lambda : self.__PressQuickSlot(7)
# Add:
	onPressKeyDict[app.DIK_F5]	= lambda : self.ScanDropList()
# ~ You can change Key DIK if you want to

# Search:
	def StopRight(self):
		player.SetSingleDIKKeyState(app.DIK_RIGHT, False)

# Add below:
	def ScanDropList(self):
		if not self.dropListDlg:
			self.dropListDlg=uidroplist.FileListDialog()
		self.dropListDlg.Open()

	def DropListUpdate(self, vid, name):
		constInfo.DropListAppend(int(vid), str(name))

	def DropListOwn(self, vid):
		constInfo.DropListMyItem(int(vid))

	def RemoveVidFromList(self, vid):
		constInfo.RemoveFromDropList(int(vid))