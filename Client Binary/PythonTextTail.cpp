// If you're using xP3NG3Rx ~ [C++] ItemName reneval on the ground system - if not - scroll down
// Search:
void CPythonTextTail::RegisterItemTextTail(DWORD VirtualID, const char * c_szText, CGraphicObjectInstance * pOwner, bool bHasAttr)
{
...
#ifdef ENABLE_EXTENDED_ITEMNAME_ON_GROUND
		CInstanceBase * pInstance = CPythonCharacterManager::Instance().GetMainInstancePtr();
		if (pInstance)
		{
			if (!strcmp(pInstance->GetNameString(), c_szName))
				pTextTail->pOwnerTextInstance->SetColor(1.0f, 1.0f, 0.0f);
			else
				pTextTail->pOwnerTextInstance->SetColor(1.0f, 0.0f, 0.0f);
		}
#else

// Replace with:
#ifdef ENABLE_EXTENDED_ITEMNAME_ON_GROUND
		CInstanceBase * pInstance = CPythonCharacterManager::Instance().GetMainInstancePtr();
		if (pInstance)
		{
			if (!strcmp(pInstance->GetNameString(), c_szName))
			{
				pTextTail->pOwnerTextInstance->SetColor(1.0f, 1.0f, 0.0f);
#ifdef ENABLE_DROPLIST_WINDOW
				CPythonPlayer::Instance().DropListOwn(pTextTail->dwVirtualID);
#endif
			}
			else
				pTextTail->pOwnerTextInstance->SetColor(1.0f, 0.0f, 0.0f);
		}
#else


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// If not - search:
void CPythonTextTail::SetItemTextTailOwner(DWORD dwVID, const char * c_szName)
{
...
}

// And replace with:
// it's extended item text tail color version but without item attr coloring
void CPythonTextTail::SetItemTextTailOwner(DWORD dwVID, const char * c_szName)
{
	TTextTailMap::iterator itor = m_ItemTextTailMap.find(dwVID);
	if (m_ItemTextTailMap.end() == itor)
		return;
	TTextTail * pTextTail = itor->second;

	if (strlen(c_szName) > 0)
	{
		if (!pTextTail->pOwnerTextInstance)
			pTextTail->pOwnerTextInstance = CGraphicTextInstance::New();
		pTextTail->pOwnerTextInstance->SetTextPointer(ms_pFont);
		pTextTail->pOwnerTextInstance->SetHorizonalAlign(CGraphicTextInstance::HORIZONTAL_ALIGN_CENTER);
		pTextTail->pOwnerTextInstance->SetValue(c_szName);
		CInstanceBase * pInstance = CPythonCharacterManager::Instance().GetMainInstancePtr();
		if (pInstance)
		{
			if (!strcmp(pInstance->GetNameString(), c_szName))
			{
				pTextTail->pOwnerTextInstance->SetColor(1.0f, 1.0f, 0.0f);
#ifdef ENABLE_DROPLIST_WINDOW
				CPythonPlayer::Instance().DropListOwn(pTextTail->dwVirtualID);
#endif
			}
			else
				pTextTail->pOwnerTextInstance->SetColor(1.0f, 0.0f, 0.0f);
		}
		pTextTail->pOwnerTextInstance->Update();

		int xOwnerSize, yOwnerSize;
		pTextTail->pOwnerTextInstance->GetTextSize(&xOwnerSize, &yOwnerSize);
		pTextTail->yStart	= -2.0f;
		pTextTail->yEnd		+= float(yOwnerSize + 4);
		pTextTail->xStart	= fMIN(pTextTail->xStart, float(-xOwnerSize / 2 - 1));
		pTextTail->xEnd		= fMAX(pTextTail->xEnd, float(xOwnerSize / 2 + 1));
	}
	else
	{
		if (pTextTail->pOwnerTextInstance)
		{
			CGraphicTextInstance::Delete(pTextTail->pOwnerTextInstance);
			pTextTail->pOwnerTextInstance = NULL;
		}

		int xSize, ySize;
		pTextTail->pTextInstance->GetTextSize(&xSize, &ySize);
		pTextTail->xStart	= (float) (-xSize / 2 - 2);
		pTextTail->yStart	= -2.0f;
		pTextTail->xEnd		= (float) (xSize / 2 + 2);
		pTextTail->yEnd		= (float) ySize;
	}
}

// Next step
// Search:
void CPythonTextTail::DeleteItemTextTail(DWORD VirtualID)
// And under:
	DeleteTextTail(itor->second);
// Add:
#ifdef ENABLE_DROPLIST_WINDOW
	CPythonPlayer::Instance().RemoveFromOwnList(VirtualID);
#endif

// Search:
void CPythonTextTail::RegisterItemTextTail(DWORD VirtualID, const char * c_szText, CGraphicObjectInstance * pOwner)
// And under:
	TTextTail * pTextTail = RegisterTextTail(VirtualID, c_szText, pOwner, c_TextTail_Name_Position, c_TextTail_Item_Color);
// Add:
#ifdef ENABLE_DROPLIST_WINDOW
	CPythonPlayer::Instance().DropListAppend(VirtualID, c_szText);
#endif
