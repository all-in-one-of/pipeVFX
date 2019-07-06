CONTAINER AINODE_ALTRIPLANAR
{
	NAME ainode_alTriplanar;

	INCLUDE GVbase;

	GROUP C4DAI_ALTRIPLANAR_MAIN_GRP
	{
		DEFAULT 1;

		AIPARAM C4DAIP_ALTRIPLANAR_INPUT {}
		AIPARAM C4DAIP_ALTRIPLANAR_TEXTURE {}
		AIPARAM C4DAIP_ALTRIPLANAR_SPACE {}
		AIPARAM C4DAIP_ALTRIPLANAR_NORMAL {}
		AIPARAM C4DAIP_ALTRIPLANAR_TILING {}
		AIPARAM C4DAIP_ALTRIPLANAR_FREQUENCY {}
		AIPARAM C4DAIP_ALTRIPLANAR_MIPMAPBIAS {}
		GROUP C4DAI_ALTRIPLANAR_BLENDING_GRP
		{
			DEFAULT 1;

			AIPARAM C4DAIP_ALTRIPLANAR_BLENDSOFTNESS {}
			AIPARAM C4DAIP_ALTRIPLANAR_CELLSOFTNESS {}
		}

		GROUP C4DAI_ALTRIPLANAR_POSITIONING_GRP
		{
			AIPARAM C4DAIP_ALTRIPLANAR_SCALEX {}
			AIPARAM C4DAIP_ALTRIPLANAR_SCALEY {}
			AIPARAM C4DAIP_ALTRIPLANAR_SCALEZ {}
			AIPARAM C4DAIP_ALTRIPLANAR_OFFSETX {}
			AIPARAM C4DAIP_ALTRIPLANAR_OFFSETY {}
			AIPARAM C4DAIP_ALTRIPLANAR_OFFSETZ {}
			AIPARAM C4DAIP_ALTRIPLANAR_ROTX {}
			AIPARAM C4DAIP_ALTRIPLANAR_ROTY {}
			AIPARAM C4DAIP_ALTRIPLANAR_ROTZ {}
			AIPARAM C4DAIP_ALTRIPLANAR_ROTJITTERX {}
			AIPARAM C4DAIP_ALTRIPLANAR_ROTJITTERY {}
			AIPARAM C4DAIP_ALTRIPLANAR_ROTJITTERZ {}
		}

	}
}
