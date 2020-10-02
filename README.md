# Metin2 Dynamic Item DropList Window
What is going on?
Whenever I was playing on any server that had far too many drop items from monsters — I wondered — how am I going to find myself in this pile of scrap?
You click on one item and pick up a completely different one, thus littering your inventory.

With my solution, your players don't have to worry about it anymore.

# As a player
Pros:
* You don't have to worry about items gained by other players
* The alphabetical list will allow you to easily find the acquired item
* The dynamic list cleans and completes itself on a regular basis
* You do not have to worry that your list will be flooded with items that have been lying on the ground for a long time — only the items you have acquired will go to the list
* You can double-click on the name of the item and the character will automatically move towards it with the intention of picking up
* You can refresh the list by yourself
* You can select an item from the list and pick it up from the ground with one button
#real-cool-heading
Min:
* You still need to be close to the item to pick it up — but it's probably fair.
# Gif
>(may be displayed once)

[![1](http://nirray.bplaced.net/Download/Github/m2/1.gif)](http://nirray.bplaced.net/Download/Github/m2/1.gif)
[![2](http://nirray.bplaced.net/Download/Github/m2/2.gif)](http://nirray.bplaced.net/Download/Github/m2/2.gif)


>YouTube video explanation :

[![YouTubeVideo](https://img.youtube.com/vi/M5Se5fqgxkE/0.jpg)](https://www.youtube.com/watch?v=M5Se5fqgxkE)

# Installation
List of edits:
[Client Python uidroplist.py](#uidroplist)
[Client Python constInfo.py](#constInfo)
##### Client part
# uidroplist
1. Place **uidroplist.py** inside *root* directory.
# constInfo
2. Open **constInfo.py** inside *root* directory:
#### Search:
```python
PVPMODE_PROTECTED_LEVEL = 15
```
#### Add below:
```python
DROPLIST_VID_AND_ITEM_NAME = {}
OWN_ITEM_VID = []
DROP_LIST_REFRESH = 0
DROP_LIST_LAST = ""
DROP_LIST_DOUBLE = 0
DROP_LIST_SLIDER = 0
```
#### Search def:
```python
def SET_TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE():
	global TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE
	app.SetTwoHandedWeaponAttSpeedDecreaseValue(TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE)
```
#### Add below:
```python
def DropListAppend(vid, item_name):
	global DROPLIST_VID_AND_ITEM_NAME
	append = {vid : item_name}
	DROPLIST_VID_AND_ITEM_NAME.update(append)

def DropListMyItem(vid):
	global OWN_ITEM_VID
	global DROP_LIST_REFRESH
	OWN_ITEM_VID.append(vid)
	DROP_LIST_REFRESH = 1

def RemoveFromDropList(vid):
	global DROPLIST_VID_AND_ITEM_NAME
	global OWN_ITEM_VID
	global DROP_LIST_REFRESH
	if DROPLIST_VID_AND_ITEM_NAME and OWN_ITEM_VID:
		if vid in DROPLIST_VID_AND_ITEM_NAME:
			del DROPLIST_VID_AND_ITEM_NAME[vid]
			OWN_ITEM_VID.remove(vid)
			DROP_LIST_REFRESH = 1
```

3. Open **game.py** inside *root* directory:

#### Search:
```python
import interfaceModule
```

#### Add below:
```python
import uidroplist
```
#### Search:
```python
	self.quickSlotPageIndex = 0
```
#### Add below:
```python
	self.dropListDlg = 0
```

#### Search:
```python
	def __BuildKeyDict(self):
```
#### Below:
```python
	onPressKeyDict[app.DIK_F4]	= lambda : self.__PressQuickSlot(7)
```
#### Add:
```python
	onPressKeyDict[app.DIK_F5]	= lambda : self.ScanDropList()
```
>You can change Key DIK if you want to

#### Search:
```python
	def StopRight(self):
		player.SetSingleDIKKeyState(app.DIK_RIGHT, False)
```

#### Add below:
```python
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
```
