CONTAINER AINODE_ALCELLNOISE
{
	NAME ainode_alCellNoise;

	INCLUDE GVbase;

	GROUP C4DAI_ALCELLNOISE_MAIN_GRP
	{
		DEFAULT 1;

		AIPARAM C4DAIP_ALCELLNOISE_SPACE {}
		AIPARAM C4DAIP_ALCELLNOISE_FREQUENCY {}
		AIPARAM C4DAIP_ALCELLNOISE_MODE {}
		AIPARAM C4DAIP_ALCELLNOISE_RANDOMNESS {}
		GROUP C4DAI_ALCELLNOISE_FEATURES_GRP
		{
			DEFAULT 1;

			AIPARAM C4DAIP_ALCELLNOISE_OCTAVES {}
			AIPARAM C4DAIP_ALCELLNOISE_LACUNARITY {}
			GROUP C4DAI_ALCELLNOISE_REMAP_GRP
			{
				AIPARAM C4DAIP_ALCELLNOISE_RMPINPUTMIN {}
				AIPARAM C4DAIP_ALCELLNOISE_RMPINPUTMAX {}
				GROUP C4DAI_ALCELLNOISE_CONTRAST_GRP
				{
					DEFAULT 1;

					AIPARAM C4DAIP_ALCELLNOISE_RMPCONTRAST {}
					AIPARAM C4DAIP_ALCELLNOISE_RMPCONTRASTPIVOT {}
				}

				GROUP C4DAI_ALCELLNOISE_BIAS_AND_GAIN_GRP
				{
					DEFAULT 1;

					AIPARAM C4DAIP_ALCELLNOISE_RMPBIAS {}
					AIPARAM C4DAIP_ALCELLNOISE_RMPGAIN {}
				}

				AIPARAM C4DAIP_ALCELLNOISE_RMPOUTPUTMIN {}
				AIPARAM C4DAIP_ALCELLNOISE_RMPOUTPUTMAX {}
				GROUP C4DAI_ALCELLNOISE_CLAMP_GRP
				{
					DEFAULT 1;

					AIPARAM C4DAIP_ALCELLNOISE_RMPCLAMPENABLE {}
					AIPARAM C4DAIP_ALCELLNOISE_RMPTHRESHOLD {}
					AIPARAM C4DAIP_ALCELLNOISE_RMPCLAMPMIN {}
					AIPARAM C4DAIP_ALCELLNOISE_RMPCLAMPMAX {}
				}

			}

			AIPARAM C4DAIP_ALCELLNOISE_COLOR1 {}
			AIPARAM C4DAIP_ALCELLNOISE_COLOR2 {}
		}

		GROUP C4DAI_ALCELLNOISE_CHIPS_GRP
		{
			DEFAULT 1;

			AIPARAM C4DAIP_ALCELLNOISE_SMOOTHCHIPS {}
			AIPARAM C4DAIP_ALCELLNOISE_RANDOMCHIPS {}
			AIPARAM C4DAIP_ALCELLNOISE_CHIPCOLOR1 {}
			AIPARAM C4DAIP_ALCELLNOISE_CHIPPROB1 {}
			AIPARAM C4DAIP_ALCELLNOISE_CHIPCOLOR2 {}
			AIPARAM C4DAIP_ALCELLNOISE_CHIPPROB2 {}
			AIPARAM C4DAIP_ALCELLNOISE_CHIPCOLOR3 {}
			AIPARAM C4DAIP_ALCELLNOISE_CHIPPROB3 {}
			AIPARAM C4DAIP_ALCELLNOISE_CHIPCOLOR4 {}
			AIPARAM C4DAIP_ALCELLNOISE_CHIPPROB4 {}
			AIPARAM C4DAIP_ALCELLNOISE_CHIPCOLOR5 {}
			AIPARAM C4DAIP_ALCELLNOISE_CHIPPROB5 {}
		}

		AIPARAM C4DAIP_ALCELLNOISE_P {}
	}
}
