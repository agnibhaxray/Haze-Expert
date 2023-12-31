import streamlit as st
import cv2
import numpy as np
import argparse
from PIL import Image
import streamlit.components.v1 as components
import dehaze  # Replace with the name of your image processing script
components.html("""<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>HazeXpert</title>
	<script src="https://cdn.tailwindcss.com"></script>
	<link rel="stylesheet" href="dist/styles.css">
	<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300&display=swap" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300&family=Lexend+Deca:wght@700&display=swap" rel="stylesheet">
	<link rel="icon" href="./favicon_io/favicon.ico">
</head>

<body>
	<div class="bg-gradient-to-b from-skin to-purpleBlue h-71">
		<div>
			<nav class="text-right items-center">
			  <div class="flex justify-between items-center">
				<img class="pt-6 pl-5 w-16 top-0" src="./images/logo-removebg-preview.png" alt="logo">
				<p class="absolute ml-20 text-xl font-semibold mt-6">HazeXpert</p>
				<div class="px-4 cursor-pointer md:hidden z-20" id="burger">
				  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-white" id="menuIcon">
					<path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
				  </svg>
				  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-white hidden" id="crossIcon">
					<path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
				  </svg>
				</div>
			  </div>
			  <ul class="relative -mt-8 hidden md:block text-black text-xl pr-4 z-20" id="menu">
				<li class="md:inline-block my-6 md:my-0 md:mx-6"><a href="#home" class="justify-end hover:bg-mix hover:text-white hover:rounded-full hover:px-3 py-2 transition-all ease-out duration-300 font-normal text-newGray">Home</a></li>
				<li class="md:inline-block my-6 md:my-0 md:mx-6"><a href="about.html" target="_blank" class="justify-end hover:bg-mix hover:text-white hover:rounded-full hover:px-3 py-2 transition-all ease-out duration-300 font-normal text-newGray">About</a></li>
				<li class="md:inline-block my-6 md:my-0 md:mx-6"><a href="#support" class="justify-end hover:bg-mix hover:text-white hover:rounded-full hover:px-3 py-2 transition-all ease-out duration-300 font-normal text-newGray">Support</a></li>
				<li class="md:inline-block my-6 md:my-0 md:mx-6"><a href="#faq" class="justify-end hover:bg-mix hover:text-white hover:rounded-full hover:px-3 py-2 transition-all ease-out duration-300 font-normal text-newGray">FAQ</a></li>
			  </ul>
			  <img class="absolute -top-4 right-0 w-[435px]" src="./images/Ellipse.png" alt="ellipse-img">
			</nav>
		</div>

		<section id="home">
			<h1>
				<div class="relative top-16 left-6 space-x-4">
					<span class="uppercase font-extrabold text-8xl text-black font-lexend-deca">we</span>
  					<span class="uppercase font-extrabold text-8xl text-white font-lexend-deca">desmoke</span>
				</div>
				<div class="relative top-20 left-6 space-x-4">
					<span class="uppercase font-extrabold text-8xl text-white font-lexend-deca">we</span>
					<span class="uppercase font-extrabold text-8xl text-black font-lexend-deca">dehaze</span>
				</div>
			</h1>
			<img class="absolute top-20 right-28.5 w-[330px]" src="./images/Hazed.png" alt="hazed-img">
			<img class="absolute top-36 right-22" src="./images/fluent_arrow-reply-20-regular.png" alt="arrow">
			<img class="absolute top-28 right-12 w-[350px]" src="./images/Dehazed.png" alt="dehazed-img">
			<p class="w-[550px] h-[116px] leading-7 font-dm-sans relative top-24 left-8 text-2xl text-justify">HazeXpert utilises deep learning to dehaze and desmoke images online, restore features in hazy shots and fix the colour of the sky, portraits, mountains, clouds, and emergency spots for much more explicit pictures.</p>
			<img class="relative top-48" src="./images/Rectangle.png" alt="Rectangle">
			<img class="absolute top-45 right-0" src="./images/triangle.png" alt="triangle">
			<div class="absolute top-48.5 right-0 bottom-0 left-0 w-50 h-28.5 m-auto flex items-center justify-center bg-white rounded-2xl cursor-pointer">
				<div id="fileContainer" class="relative space-y-6 text-center border-dashed border-3 rounded-2xl border-gray-400 w-45 h-72 -top-10">
					<img class="relative left-72 right-0 top-12 bottom-0" src="./images/cloud.png" alt="cloud-img">
					<p class="text-gray-700 text-lg relative top-12">Upload your files here! Or<label for="bgfile" title="Upload a file" class="relative z-20 cursor-pointer text-blue-500 hover:text-blue-600 block">Browse</label></p>
					<input accept=".jpg, .jpeg, .png, .svg, .webp, .mp4" class="absolute z-10 opacity-0 cursor-pointer" type="file" name="bgfile" id="bgfile">
				</div>	
				<button class="uppercase bg-orskin text-white text-base font-semibold px-10 py-2 rounded-full border hover:bg-orskin cursor-pointer transform scale-5 transition-all absolute top-23 left-52 hover:scale-125 ease-out duration-300 font-dm-sans">dehaze</button>	
				<button class="uppercase bg-bluePurple text-white text-base font-semibold px-10 py-2 rounded-full border hover:bg-bluePurple cursor-pointer transform scale-5 transition-all absolute top-23 right-52 hover:scale-125 ease-out duration-300 font-dm-sans">download</button>										
			</div>
		</section>
	</div>

	<section class="h-200">
		<section class="bg-white" id="steps">
			<div class="flex justify-center text-6xl font-bold font-lexend-deca relative top-20">
			  <span> Steps To Upload Your File </span>
			</div>
			<div class="flex justify-center items-center mt-48">
				<div class="grid grid-cols-3 gap-24">
					<div class="h-[259px] w-[259px] bg-lightGray text-lg text-white text-center">
						<svg xmlns="http://www.w3.org/2000/svg" width="72" height="72" viewBox="0 0 24 24" style="fill: white; width: 60px; height: 60px;" class="m-1 h-12 w-12 left-0 right-0 mx-auto relative top-6">
							<path d="M13 19v-4h3l-4-5-4 5h3v4z"></path>
							<path d="M7 19h2v-2H7c-1.654 0-3-1.346-3-3 0-1.404 1.199-2.756 2.673-3.015l.581-.102.192-.558C8.149 8.274 9.895 7 12 7c2.757 0 5 2.243 5 5v1h1c1.103 0 2 .897 2 2s-.897 2-2 2h-3v2h3c2.206 0 4-1.794 4-4a4.01 4.01 0 0 0-3.056-3.888C18.507 7.67 15.56 5 12 5 9.244 5 6.85 6.611 5.757 9.15 3.609 9.792 2 11.82 2 14c0 2.757 2.243 5 5 5z"></path>
						</svg>
						<h2 class="font-semibold text-xl mt-6">Upload Hazy/Smoky File</h2>
						<p class="text-sm text-center mt-4 px-5">To submit hazy photographs, click the "Dehaze" option or browse from your files. Hezexpert will remove the smoke and haze from the file</p>
					</div>
					<div class="h-[259px] w-[259px] bg-lightGray text-white text-center">
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="m-1 h-12 w-12 left-0 right-0 mx-auto relative top-8">
							<path stroke-linecap="round" stroke-linejoin="round" d="M6 13.5V3.75m0 9.75a1.5 1.5 0 010 3m0-3a1.5 1.5 0 000 3m0 3.75V16.5m12-3V3.75m0 9.75a1.5 1.5 0 010 3m0-3a1.5 1.5 0 000 3m0 3.75V16.5m-6-9V3.75m0 3.75a1.5 1.5 0 010 3m0-3a1.5 1.5 0 000 3m0 9.75V10.5" />
						  </svg>
					
						<h2 class="font-semibold text-xl mt-10">Desmoke/Dehaze</h2>
						<p class="text-sm text-center mt-4 px-5">Without any manual work, HazeXpert Software will automatically Dehaze/ Desmoke any online or uploaded photo or video using AI.</p>
					</div>
					<div class="h-[259px] w-[259px] bg-lightGray text-white text-center">
						<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="m-1 h-12 w-12 left-0 right-0 mx-auto relative top-8">
							<path stroke-linecap="round" stroke-linejoin="round" d="M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5M16.5 12L12 16.5m0 0L7.5 12m4.5 4.5V3" />
						</svg>                  
						<h2 class="font-semibold text-xl mt-10">Download File</h2>
						<p class="text-sm text-center mt-4 px-5">After being dehaze/desmoke, you may download the appropriate image or photo to your local device using HazeXpert.</p>
					</div>
				</div>
			</div>
			<img class="relative bottom-40 left-34" src="./images/blackArrow.png" alt="arrow-1">
			<img class="relative bottom-14.5 left-56.5" src="./images/blackArrow.png" alt="arrow-2">
			<img class="relative bottom-27 left-56" src="./images/healthicons_1-outline.png" alt="one">
			<img class="relative bottom-29.5 left-37" src="./images/Vector.png" alt="two">
			<img class="relative bottom-32.5 left-59" src="./images/healthicons_3-outline.png" alt="three">
		</section>

		<section class="-mt-32" id="features">
			<div class="flex justify-center text-6xl font-bold font-lexend-deca relative">
				<span>Key Features</span>
			</div>
			<div class="mt-14">
				<div class="w-[550px] h-[240px] bg-feat_1 relative rounded-2xl left-52 top-20 flex flex-col justify-center items-start text-center">
					<div class="items-start relative left-7">
						<h2 class="font-dm-sans font-extrabold text-4xl text-feat_text">Data Authentication</h2>
						<p class="w-[320px] mt-4 text-lg text-feat_text">To submit hazy photographs, click the "Dehaze" option or browse from your files. HezeXpert will remove the smoke and haze from the file</p>
					</div>
					<img class="w-[310px] h-[244px] absolute top-8 -right-24" src="./images/undraw_secure_files_re_6vdh 1.svg" alt="img-1">
				</div>
				
				<div class="w-[550px] h-[240px] bg-feat_2 relative rounded-2xl left-48.5 top-60 flex flex-col justify-center items-start text-center">
					<div class="items-start absolute right-10">
						<h2 class="font-dm-sans font-extrabold text-4xl text-white">Data Authentication</h2>
						<p class="w-[320px] mt-4 text-lg text-white">To submit hazy photographs, click the "Dehaze" option or browse from your files. HezeXpert will remove the smoke and haze from the file</p>
					</div>
					<img class="w-[220px] h-[257px] absolute top-8 -left-16" src="./images/undraw_sync_files_re_ws4c 1.svg" alt="img-2">
				</div>
				
				<div class="w-[550px] h-[240px] bg-feat_3 relative rounded-2xl left-52 top-25 flex flex-col justify-center items-start text-center">
					<div class="items-start relative left-7">
						<h2 class="font-dm-sans font-extrabold text-4xl text-feat_text">Data Authentication</h2>
						<p class="w-[320px] mt-4 text-lg text-feat_text">To submit hazy photographs, click the "Dehaze" option or browse from your files. HezeXpert will remove the smoke and haze from the file</p>
					</div>
					<img class="w-[225px] h-[169px] absolute top-20 -right-10" src="./images/undraw_add_information_j2wg 1.svg" alt="img-3">
				</div>
				<img class="relative bottom-32.5 left-48.5 h-[250px] w-[250px] z-[-20]" src="./images/Ellipse 2.png" alt="ellipse-2">
				<img class="relative bottom-22 left-28.5 h-[250px] w-[250px] z-[-20]" src="./images/Ellipse 3.png" alt="ellipse-3">
				<img class="relative bottom-48 left-42 w-[250px] z-[-20]" src="./images/Ellipse 4.png" alt="ellipse-4">
			</div>
		</section>

		<section id="testimonials">
			<div class="flex justify-center text-6xl font-bold font-lexend-deca relative mb-24">
				<span>Testimonial</span>
			</div>
			<div class="bg-boxbg grid grid-cols-4 pt-14 pb-0 px-14">
				<section class="dark:bg-box h-[30rem] w-[25rem] -mx-10 border-feat_brdr border-4">
				  <div class="mx-auto max-w-screen-xl px-4 py-8 text-center lg:px-6 lg:py-16">
					<figure class="mx-auto max-w-screen-md">
					  <svg class="mx-auto mb-3 h-12 text-gray-400 dark:text-gray-600" viewBox="0 0 24 27" fill="none" xmlns="http://www.w3.org/2000/svg">
						<path d="M14.017 18L14.017 10.609C14.017 4.905 17.748 1.039 23 0L23.995 2.151C21.563 3.068 20 5.789 20 8H24V18H14.017ZM0 18V10.609C0 4.905 3.748 1.038 9 0L9.996 2.151C7.563 3.068 6 5.789 6 8H9.983L9.983 18L0 18Z" fill="currentColor" />
					  </svg>
					  <blockquote>
						<p class="text-lg font-medium text-gray-900 dark:text-white">"I was amazed by the capabilities of this AI-ML de-smoking algorithm. During a recent indoor fire emergency, the real-time video feed became almost useless due to heavy smoke. But this algorithm cleared up the view, allowing rescue teams to navigate and locate trapped individuals swiftly. It's a game-changer for firefighting operations."</p>
					  </blockquote>
					  <figcaption class="mt-6 flex items-center justify-center space-x-3">
						<img class="h-6 w-6 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png" alt="profile picture" />
						<div class="flex items-center divide-x-2 divide-gray-500 dark:divide-gray-700">
						  <div class="pr-3 font-medium text-gray-900 dark:text-white">Micheal Gough</div>
						  <div class="pl-3 text-sm text-blue-950 font-bold">CEO at Google</div>
						</div>
					  </figcaption>
					</figure>
				  </div>
				</section>
				<section class="dark:bg-box col-span-2 h-[30rem] w-[40rem] mx-7 border-feat_brdr border-4">
				  <div class="mx-auto max-w-screen-xl px-4 py-8 text-center lg:px-6 lg:py-16">
					<figure class="mx-auto max-w-screen-md">
					  <svg class="mx-auto mb-3 h-12 text-gray-400 dark:text-gray-600" viewBox="0 0 24 27" fill="none" xmlns="http://www.w3.org/2000/svg">
						<path d="M14.017 18L14.017 10.609C14.017 4.905 17.748 1.039 23 0L23.995 2.151C21.563 3.068 20 5.789 20 8H24V18H14.017ZM0 18V10.609C0 4.905 3.748 1.038 9 0L9.996 2.151C7.563 3.068 6 5.789 6 8H9.983L9.983 18L0 18Z" fill="currentColor" />
					  </svg>
					  <blockquote>
						<p class="text-lg font-medium text-gray-900 dark:text-white">"As a veteran in rescue operations, I must say that this technology is a game-changer. It significantly improves situational awareness during indoor fire incidents. The de-smoking algorithm is incredibly effective, making our tasks much safer and efficient. Kudos to the team behind this innovation!"</p>
					  </blockquote>
					  <figcaption class="mt-6 flex items-center justify-center space-x-3">
						<img class="h-6 w-6 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png" alt="profile picture" />
						<div class="flex items-center divide-x-2 divide-gray-500 dark:divide-gray-700">
						  <div class="pr-3 font-medium text-gray-900 dark:text-white">Micheal Gough</div>
						  <div class="pl-3 text-sm text-blue-950 font-bold">CEO at Google</div>
						</div>
					  </figcaption>
					</figure>
				  </div>
				</section>
				<section class="dark:bg-box h-[30rem] w-[25rem] -mx-4 border-feat_brdr border-4">
				  <div class="mx-auto max-w-screen-xl px-4 py-8 text-center lg:px-6 lg:py-16">
					<figure class="mx-auto max-w-screen-md">
					  <svg class="mx-auto mb-3 h-12 text-gray-400 dark:text-gray-600" viewBox="0 0 24 27" fill="none" xmlns="http://www.w3.org/2000/svg">
						<path d="M14.017 18L14.017 10.609C14.017 4.905 17.748 1.039 23 0L23.995 2.151C21.563 3.068 20 5.789 20 8H24V18H14.017ZM0 18V10.609C0 4.905 3.748 1.038 9 0L9.996 2.151C7.563 3.068 6 5.789 6 8H9.983L9.983 18L0 18Z" fill="currentColor" />
					  </svg>
					  <blockquote>
						<p class="text-lg font-medium text-gray-900 dark:text-white">"I had the opportunity to witness the de-smoking algorithm in action during a live demo. It's a remarkable tool that enhances the safety of both responders and those in distress. The ability to see through smoke and haze in real-time is a lifesaver. This project has immense potential for widespread use"</p>
					  </blockquote>
					  <figcaption class="mt-6 flex items-center justify-center space-x-3">
						<img class="h-6 w-6 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png" alt="profile picture" />
						<div class="flex items-center divide-x-2 divide-gray-500 dark:divide-gray-700">
						  <div class="pr-3 font-medium text-gray-900 dark:text-white">Micheal Gough</div>
						  <div class="pl-3 text-sm text-blue-950 font-bold">CEO at Google</div>
						</div>
					  </figcaption>
					</figure>
				  </div>
				</section>
		
				<section class="dark:bg-box col-span-2 my-16 mx-14 border-feat_brdr border-4">
				  <div class="mx-auto max-w-screen-xl px-4 py-8 text-center lg:px-6 lg:py-16">
					<figure class="mx-auto max-w-screen-md">
					  <svg class="mx-auto mb-3 h-12 text-gray-400 dark:text-gray-600" viewBox="0 0 24 27" fill="none" xmlns="http://www.w3.org/2000/svg">
						<path d="M14.017 18L14.017 10.609C14.017 4.905 17.748 1.039 23 0L23.995 2.151C21.563 3.068 20 5.789 20 8H24V18H14.017ZM0 18V10.609C0 4.905 3.748 1.038 9 0L9.996 2.151C7.563 3.068 6 5.789 6 8H9.983L9.983 18L0 18Z" fill="currentColor" />
					  </svg>
					  <blockquote>
						<p class="text-lg font-medium text-gray-900 dark:text-white">"I've followed the development of this AI-ML de-hazing algorithm closely, and it's a breakthrough in fire safety technology. The algorithm's ability to restore visibility in smoke-filled environments is impressive. It has the potential to revolutionize how we handle indoor fire emergencies"</p>
					  </blockquote>
					  <figcaption class="mt-6 flex items-center justify-center space-x-3">
						<img class="h-6 w-6 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png" alt="profile picture" />
						<div class="flex items-center divide-x-2 divide-gray-500 dark:divide-gray-700">
						  <div class="pr-3 font-medium text-gray-900 dark:text-white">Micheal Gough</div>
						  <div class="pl-3 text-sm text-blue-950 font-bold">CEO at Google</div>
						</div>
					  </figcaption>
					</figure>
				  </div>
				</section>
				<section class="dark:bg-box col-span-2 my-16 mx-10 border-feat_brdr border-4">
				  <div class="mx-auto max-w-screen-xl px-4 py-8 text-center lg:px-6 lg:py-16">
					<figure class="mx-auto max-w-screen-md">
					  <svg class="mx-auto mb-3 h-12 text-gray-400 dark:text-gray-600" viewBox="0 0 24 27" fill="none" xmlns="http://www.w3.org/2000/svg">
						<path d="M14.017 18L14.017 10.609C14.017 4.905 17.748 1.039 23 0L23.995 2.151C21.563 3.068 20 5.789 20 8H24V18H14.017ZM0 18V10.609C0 4.905 3.748 1.038 9 0L9.996 2.151C7.563 3.068 6 5.789 6 8H9.983L9.983 18L0 18Z" fill="currentColor" />
					  </svg>
					  <blockquote>
						<p class="text-lg font-medium text-gray-900 dark:text-white">"This AI-ML de-hazing algorithm is a great example of how technology can be harnessed for public safety. The results are astonishing, and it opens up new possibilities for AI in emergency response. I'm excited to see how this project evolves and becomes an integral part of firefighting operations."</p>
					  </blockquote>
					  <figcaption class="mt-6 flex items-center justify-center space-x-3">
						<img class="h-6 w-6 rounded-full" src="https://flowbite.s3.amazonaws.com/blocks/marketing-ui/avatars/michael-gouch.png" alt="profile picture" />
						<div class="flex items-center divide-x-2 divide-gray-500 dark:divide-gray-700">
						  <div class="pr-3 font-medium text-gray-900 dark:text-white">Micheal Gough</div>
						  <div class="pl-3 text-sm text-blue-950 font-bold">CEO at Google</div>
						</div>
					  </figcaption>
					</figure>
				  </div>
				</section>
			  </div>
			</div>
		  
		</section>
	</section>

	
	<script src="index.js"></script>
</body>

</html>""")
# Title and descriptio