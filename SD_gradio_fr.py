from gradio_client import Client

client = Client("https://segmind-segmind-stable-diffusion.hf.space/--replicas/8c76w/")

result = client.predict(
		"Howdy!",	# str  in 'Prompt' Textbox component
		"Howdy!",	# str  in 'Negative prompt' Textbox component
		"(No style)",	# str  in 'Image Style' Radio component
		"Howdy!",	# str  in 'Prompt 2' Textbox component
		"Howdy!",	# str  in 'Negative prompt 2' Textbox component
		True,	# bool  in 'Use negative prompt' Checkbox component
		True,	# bool  in 'Use prompt 2' Checkbox component
		True,	# bool  in 'Use negative prompt 2' Checkbox component
		0,	# int | float (numeric value between 0 and 2147483647) in 'Seed' Slider component
		256,	# int | float (numeric value between 256 and 1024) in 'Width' Slider component
		256,	# int | float (numeric value between 256 and 1024) in 'Height' Slider component
		1,	# int | float (numeric value between 1 and 20) in 'Guidance scale for base' Slider component
		1,	# int | float (numeric value between 1 and 20) in 'Guidance scale for refiner' Slider component
		10,	# int | float (numeric value between 10 and 100) in 'Number of inference steps for base' Slider component
		10,	# int | float (numeric value between 10 and 100) in 'Number of inference steps for refiner' Slider component
		True,	# bool  in 'Apply refiner' Checkbox component
		True,	# bool  in 'Randomize seed' Checkbox component
		api_name="/run"
)
print(result)


# client = Client("https://hysts-sd-xl.hf.space/")
#
# result = client.predict(
# 		"two naked women walk on a beach back view",	# str  in 'Prompt' Textbox component
# 		"3d, cartoon, anime, (deformed eyes, nose, ears, nose), bad anatomy, ugly",	# str  in 'Negative prompt' Textbox component
# 		"Howdy!",	# str  in 'Prompt 2' Textbox component
# 		"Howdy!",	# str  in 'Negative prompt 2' Textbox component
# 		True,	# bool  in 'Use negative prompt' Checkbox component
# 		True,	# bool  in 'Use prompt 2' Checkbox component
# 		True,	# bool  in 'Use negative prompt 2' Checkbox component
# 		0,	# int | float (numeric value between 0 and 2147483647) in 'Seed' Slider component
# 		1024,	# int | float (numeric value between 256 and 1024) in 'Width' Slider component
# 		1024,	# int | float (numeric value between 256 and 1024) in 'Height' Slider component
# 		5,	# int | float (numeric value between 1 and 20) in 'Guidance scale for base' Slider component
# 		5,	# int | float (numeric value between 1 and 20) in 'Guidance scale for refiner' Slider component
# 		25,	# int | float (numeric value between 10 and 100) in 'Number of inference steps for base' Slider component
# 		25,	# int | float (numeric value between 10 and 100) in 'Number of inference steps for refiner' Slider component
# 		True,	# bool  in 'Apply refiner' Checkbox component
# 		api_name="/run"
# )
# print(result)

