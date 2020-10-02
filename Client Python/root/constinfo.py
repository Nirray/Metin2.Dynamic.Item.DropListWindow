# Search:
PVPMODE_PROTECTED_LEVEL = 15

# Add below:
DROPLIST_VID_AND_ITEM_NAME = {}
OWN_ITEM_VID = []
DROP_LIST_REFRESH = 0
DROP_LIST_LAST = ""
DROP_LIST_DOUBLE = 0
DROP_LIST_SLIDER = 0

# Search def:
def SET_TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE():
	global TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE
	app.SetTwoHandedWeaponAttSpeedDecreaseValue(TWO_HANDED_WEAPON_ATT_SPEED_DECREASE_VALUE)

# Add below:
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