import uiScriptLocale

window = {
	"name" : "DropListWindow",

	"x" : SCREEN_WIDTH - 170,
	"y" : SCREEN_HEIGHT - 400 - 50,

	"style" : ("movable", "float",),

	"width" : 270,
	"height" : 300,

	"children" :
	(

		{
			"name" : "board",
			"type" : "board_with_titlebar",

			"x" : 0,
			"y" : 0,

			"width" : 270,
			"height" : 300,
			"title" : uiScriptLocale.DROP_LIST_TITLE,
		},

		{
			"name" : "ScrollBar",
			"type" : "scrollbar",

			"x" : 27,
			"y" : 40,
			"size" : 220,
			"horizontal_align" : "right",
		},

		{
			"name" : "ok",
			"type" : "button",

			"x" : 0,
			"y" : 265,

			"width" : 61,
			"height" : 21,

			"text" : uiScriptLocale.DROP_LIST_PICKUP,
			"horizontal_align" : "center",
			"default_image" : "d:/ymir work/ui/public/large_button_01.sub",
			"over_image" : "d:/ymir work/ui/public/large_button_02.sub",
			"down_image" : "d:/ymir work/ui/public/large_button_03.sub",
		},

		{
			"name" : "refresh",
			"type" : "button",

			"x" : 27+5,
			"y" : 265,
			"horizontal_align" : "right",
			
			"width" : 41,
			"height" : 21,


			"default_image" : "d:/ymir work/ui/game/guild/Refresh_Button_01.sub",
			"over_image" : "d:/ymir work/ui/game/guild/Refresh_Button_02.sub",
			"down_image" : "d:/ymir work/ui/game/guild/Refresh_Button_03.sub",
			"tooltip_text" : uiScriptLocale.MARKLIST_REFRESH,
		},
	)
}
