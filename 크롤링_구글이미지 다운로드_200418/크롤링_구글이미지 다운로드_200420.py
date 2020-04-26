from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images

# from google_images_download import google_images_download
#
# response = google_images_download.googleimagesdownload()
#
# arguments = {
#     "keywords" : "polar bears, baloons",
#     "limit" : 20,
#     "print_url" : True
# }
#
# paths = response.download(arguments)
# print(paths)


