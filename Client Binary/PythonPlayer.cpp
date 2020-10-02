// Search:
void CPythonPlayer::ClearSkillDict()
{
	...
}
// Add below:
#ifdef ENABLE_DROPLIST_WINDOW
void CPythonPlayer::DropListAppend(DWORD VID, string Item_Name)
{
	PyCallClassMemberFunc(m_ppyGameWindow, "DropListUpdate", Py_BuildValue("(is)", VID, Item_Name.c_str()));
}
void CPythonPlayer::DropListOwn(DWORD VID)
{
	PyCallClassMemberFunc(m_ppyGameWindow, "DropListOwn", Py_BuildValue("(i)", VID));
}
void CPythonPlayer::RemoveFromOwnList(DWORD VID)
{
	PyCallClassMemberFunc(m_ppyGameWindow, "RemoveVidFromList", Py_BuildValue("(i)", VID));
}
#endif

// Search:
DWORD CPythonPlayer::GetPlayTime()
{
	return m_dwPlayTime;
}

// Add below:
#ifdef ENABLE_DROPLIST_WINDOW
void CPythonPlayer::SendClickItemPacketDropList(DWORD dwIID)
{
	CInstanceBase* pkInstMain = NEW_GetMainActorPtr();
	if (!pkInstMain) 
		return;
	if (IsObserverMode())
		return;
	if (pkInstMain->IsStun())
		return;
	if (pkInstMain->IsDead())
		return;
	CPythonItem& rkIT = CPythonItem::Instance();

	TPixelPosition kPPosPickedItem;
	if (rkIT.GetGroundItemPosition(dwIID, &kPPosPickedItem))
	{
		float distance = 120.0f;
		if (pkInstMain->IsMountingHorse() || pkInstMain->IsNewMount())
			distance = 150.0f;
		if (pkInstMain->NEW_GetDistanceFromDestPixelPosition(kPPosPickedItem) < distance)
		{
			CPythonNetworkStream& rkNetStream = CPythonNetworkStream::Instance();
			TPixelPosition kPPosCur;
			pkInstMain->NEW_GetPixelPosition(&kPPosCur);
			float fCurRot = pkInstMain->GetRotation();
			rkNetStream.SendCharacterStatePacket(kPPosCur, fCurRot, CInstanceBase::FUNC_WAIT, 0);
			pkInstMain->NEW_Stop();
			__ClearReservedAction();
			SendClickItemPacket(dwIID);
		}
		else
		{
			pkInstMain->NEW_MoveToDestPixelPositionDirection(kPPosPickedItem);
			SendClickItemPacket(dwIID);
		}
	}
	else
	{
		__ClearReservedAction();
		SendClickItemPacket(dwIID);
	}
}
#endif