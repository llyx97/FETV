instruction_qg_yesno = """Given a video description and extracted elements, 
                generate two yes-no questions about each element. The answer of one question should be yes, and the answer of another question should be no.
                Ensure that the question can be answered based on information in the video description. 
                Please ensure that the response follows the format of the following examples."""

example_qg_yesno = """
Description: kids are learning how to wrestle
Elements: kids, learning, wrestle
About kids:
Q: are there kids?
A: yes
Q: are there cats?
A: no
About learning:
Q: are the kids learning wrestling?
A: yes
Q: are the kids teaching wrestling?
A: no
About wrestle:
Q: are the kids wrestling?
A: yes
Q: are the kids playing basketball?
A: no

Description: Close up of white dog running forward in the park
Elements: close up, white, dog, running
About close up:
Q: is this a close up?
A: yes
Q: is this a wide shot?
A: no
About white:
Q: is the color of the dog white?
A: yes
Q: is the color of the dog black?
A: no
About dog:
Q: is there a dog?
A: yes
Q: is there a fox?
A: no
About running:
Q: is the dog running?
A: yes
Q: is the dog sitting?
A: no

Description: two men covered with snow hugging each other
Elements: two, men, covered, snow, hugging
About two:
Q: are there two men?
A: yes
Q: are there three men?
A: no
About men:
Q: are there men in the video?
A: yes
Q: are there girls in the video?
A: no
About covered:
Q: are the men covered with snow?
A: yes
Q: are the men covered with coal?
A: no
About snow:
Q: is the video showing snow?
A: yes
Q: is the video showing ocean?
A: no
About hugging:
Q: are the men hugging each other?
A: yes
Q: are the men fighting each other?
A: no

Description: Backside view of woman butt in black leather skirt walking on street, close up, slow motion.
Elements: Backside view, woman, butt, black, leather skirt, walking, street, close up, slow motion
About Backside view:
Q: is this a backside view?
A: yes
Q: is this a front view?
A: no
About woman:
Q: is there a woman in the video?
A: yes
Q: is there a boy in the video?
A: no
About butt:
Q: is the video focusing on butt?
A: yes
Q: is the video focusing on hands?
A: no
About black:
Q: is the leather skirt black?
A: yes
Q: is the leather skirt yellow?
A: no
About leather skirt:
Q: is the woman wearing a leather skirt?
A: yes
Q: is the woman wearing a dress?
A: no
About walking:
Q: is the woman walking?
A: yes
Q: is the woman running?
A: no
About street:
Q: is the video shot on a street?
A: yes
Q: is the video shot on a desert?
A: no
About close up:
Q: is this a close up?
A: yes
Q: is this a long shot?
A: no
About slow motion:
Q: is this a slow motion?
A: yes
Q: is this a timelapse?
A: no

Description: Timelapse of a cityspace at sunset, aerial view
Elements: Timelapse, cityspace, sunset, aerial view
About Timelapse:
Q: is this a timelapse?
A: yes
Q: is this a slow motion?
A: no
About cityspace:
Q: is the video about cityspace?
A: yes
Q: is the video about forest?
A: no
About sunset: 
Q: is this video captured during sunset?
A: yes
Q: is this video captured at night?
A: no
About aerial view:
Q: is this an aerial view?
A: yes
Q: is this video shot on ground?
A: no

Description: A small car driving to the right side of the road.
Elements: small, car, driving, right side, road
About small:
Q: is the car small?
A: yes
Q: is the car huge?
A: no
About car:
Q: is there a car?
A: yes
Q: is this video about a bike?
A: no
About driving:
Q: is the car driving?
A: yes
Q: is the car stationary??
A: no
About right side:
Q: is the car driving to the right side of the road?
A: yes
Q: is the car driving to the left side of the road?
A: no
About road:
Q: is the video shot on a road?
A: yes
Q: is the video shot on the sky?
A: no
"""


instruction_element = """Extract all key elements from the video description. 
                Please ensure that your response contains extracted elements and follows the format of the following examples. 
                If a phrase involves an object and an attribute, extract it as two elements. 
                For example, extract white dog as white and dog."""

example_element = """
Description: kids are learning how to wrestle
Elements: kids, learning, wrestle

Description: A white dog is running
Elements: white, dog, running

Description: two men covered with snow hugging each other
Elements: two, men, covered, snow, hugging

Description: Backside view of woman butt in black leather skirt walking on street, close up, slow motion.
Elements: Backside view, woman, butt, black, leather skirt, walking, street, close up, slow motion

Description: Timelapse of a cityspace at sunset, aerial view
Elements: Timelapse, cityspace, sunset, aerial view

Description: A small car driving to the right side of the road.
Elements: small, car, driving, right side, road

Description: """