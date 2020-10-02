// Search:
	void	SendClickItemPacket(DWORD dwIID);

// Add below:
#ifdef ENABLE_DROPLIST_WINDOW
	void	SendClickItemPacketDropList(DWORD dwIID);
#endif

// Search:
		void	ClearSkillDict();

// Add below:
#ifdef ENABLE_DROPLIST_WINDOW
		void	DropListAppend(DWORD VID, string Item_Name);
		void	DropListOwn(DWORD VID);
		void	RemoveFromOwnList(DWORD VID);
#endif